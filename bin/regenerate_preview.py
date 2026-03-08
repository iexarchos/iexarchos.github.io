from __future__ import annotations

import argparse
import asyncio
import json
import re
from datetime import date, datetime
from pathlib import Path

import markdown
import yaml
from playwright.async_api import async_playwright


def _format_date_for_preview(value: object) -> str:
    if isinstance(value, datetime):
        return f"{value.strftime('%B')} {value.day}, {value.year}"
    if isinstance(value, date):
        return f"{value.strftime('%B')} {value.day}, {value.year}"
    if isinstance(value, str):
        match = re.match(r"^\s*(\d{4})-(\d{2})-(\d{2})", value)
        if match:
            parsed = date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
            return f"{parsed.strftime('%B')} {parsed.day}, {parsed.year}"
    return "Preview"


def _resolve_liquid_for_preview(body_md: str, front_matter: dict) -> str:
    author = str(front_matter.get("author") or "")
    author_title = str(front_matter.get("author-title") or "")
    subhed = str(front_matter.get("subhed") or "")
    date_text = _format_date_for_preview(front_matter.get("date"))

    featured_image_obj = front_matter.get("featured-image") or {}
    featured_image = featured_image_obj if isinstance(featured_image_obj, dict) else {}
    image_path = str(featured_image.get("path") or "")
    image_cutline = str(featured_image.get("cutline") or "")
    image_credit = str(featured_image.get("credit") or "")
    image_alt = str(featured_image.get("alt-text") or "")

    def _select_if_else(text: str, expression: str, keep_if: bool) -> str:
        pattern = re.compile(
            rf"{{%\s*if\s+{re.escape(expression)}\s*%}}(.*?)(?:{{%\s*else\s*%}}(.*?))?{{%\s*endif\s*%}}",
            re.S,
        )

        def _replace(match: re.Match[str]) -> str:
            if keep_if:
                return match.group(1)
            return match.group(2) or ""

        return pattern.sub(_replace, text)

    rendered = body_md
    rendered = _select_if_else(rendered, "page.author and author_title", bool(author and author_title))
    rendered = _select_if_else(rendered, "featured_image.credit", bool(image_credit))
    rendered = _select_if_else(rendered, "featured_image and featured_image.path", bool(image_path))
    rendered = re.sub(r"{%\s*assign\s+.*?%}\s*", "", rendered)

    substitutions: list[tuple[str, str]] = [
        (r"{{\s*page\.subhed\s*}}", subhed),
        (r"{{\s*page\.author\s*}}", author),
        (r"{{\s*author_title\s*}}", author_title),
        (r'{{\s*page\.date\s*\|\s*date:\s*"%B %-d, %Y"\s*}}', date_text),
        (r"{{\s*featured_image\.path\s*}}", image_path),
        (r"{{\s*featured_image\.cutline\s*}}", image_cutline),
        (r"{{\s*featured_image\.credit\s*}}", image_credit),
        (r"{{\s*featured_image\[['\"]alt-text['\"]\]\s*\|\s*default:\s*['\"].*?['\"]\s*}}", image_alt),
    ]
    for pattern, replacement in substitutions:
        rendered = re.sub(pattern, replacement, rendered)

    # Hide any unsupported Liquid instead of leaking template syntax into the preview.
    rendered = re.sub(r"{%.*?%}", "", rendered, flags=re.S)
    rendered = re.sub(r"{{.*?}}", "", rendered, flags=re.S)
    rendered = re.sub(r"<figcaption>\s*</figcaption>", "", rendered, flags=re.S)
    return rendered


def _absolutize_local_urls(html: str, repo_root: Path) -> str:
    pattern = re.compile(r'(?P<prefix>\s(?:src|href)=["\'])(?P<url>[^"\']+)(?P<suffix>["\'])')

    def _replace(match: re.Match[str]) -> str:
        url = match.group("url")
        if url.startswith(("http://", "https://", "data:", "mailto:", "javascript:", "tel:", "#", "file://")):
            return match.group(0)

        path = (repo_root / url.lstrip("/")).resolve() if url.startswith("/") else (repo_root / url).resolve()
        return f"{match.group('prefix')}{path.as_uri()}{match.group('suffix')}"

    return pattern.sub(_replace, html)


def _join_url(base: str, path: str) -> str:
    return f"{base.rstrip('/')}/{path.lstrip('/')}"


def _derive_page_path(md_path: Path, front_matter: dict) -> str:
    permalink = front_matter.get("permalink")
    if isinstance(permalink, str) and permalink.strip():
        path = permalink.strip()
        return path if path.startswith("/") else f"/{path}"

    parent = md_path.parent.name
    stem = md_path.stem

    if parent == "_journal":
        return f"/journal/{stem}/"
    if parent == "_news":
        return f"/news/{stem}/"
    if parent == "_posts":
        # Typical post filename: YYYY-MM-DD-slug.md
        match = re.match(r"^(\d{4})-\d{2}-\d{2}-(.+)$", stem)
        if match:
            return f"/blog/{match.group(1)}/{match.group(2)}/"
        return f"/blog/{stem}/"
    return f"/{stem}/"


def _comments_html(md_path: Path, front_matter: dict, site_config: dict, title: str) -> str:
    if not front_matter.get("comments"):
        return ""

    site_url = str(site_config.get("url") or "").strip().rstrip("/")
    baseurl = str(site_config.get("baseurl") or "").strip().strip("/")
    shortname = str(site_config.get("disqus_shortname") or "").strip()
    page_path = _derive_page_path(md_path, front_matter)
    page_identifier = str(front_matter.get("id") or page_path)

    full_path = _join_url(f"/{baseurl}" if baseurl else "/", page_path).replace("//", "/")
    canonical_url = _join_url(site_url, full_path) if site_url else page_path

    if shortname:
        return f"""
    <section class="preview-comments" aria-label="Comments">
      <h3 class="comments-title">Discussion</h3>
      <div id="disqus_thread">
        <p class="comments-note">Loading comments…</p>
      </div>
      <p class="comments-note">Comments render on deployed pages. Local file previews show a placeholder.</p>
    </section>
    <script>
      var disqus_config = function () {{
        this.page.url = {json.dumps(canonical_url)};
        this.page.identifier = {json.dumps(page_identifier)};
        this.page.title = {json.dumps(title)};
      }};
      (function() {{
        if (window.location.protocol === "file:") {{
          var holder = document.getElementById("disqus_thread");
          if (holder) {{
            holder.innerHTML = '<p class="comments-note">Disqus is disabled in local file preview. It will load on the deployed site.</p>';
          }}
          return;
        }}
        var d = document, s = d.createElement("script");
        s.src = "https://{shortname}.disqus.com/embed.js";
        s.setAttribute("data-timestamp", +new Date());
        (d.head || d.body).appendChild(s);
      }})();
    </script>
"""

    return """
    <section class="preview-comments" aria-label="Comments">
      <h3 class="comments-title">Discussion</h3>
      <div id="disqus_thread">
        <p class="comments-note">Comments are enabled for this post, but no Disqus shortname is configured.</p>
      </div>
    </section>
"""


def build_html(md_path: Path, out_html: Path, repo_root: Path) -> tuple[str, str]:
    text = md_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\r?\n(.*?)\r?\n---\s*\r?\n(.*)$", text, re.S)
    if not match:
        raise RuntimeError(f"No front matter found in: {md_path}")

    front_matter = yaml.safe_load(match.group(1)) or {}
    config_path = repo_root / "_config.yml"
    site_config = yaml.safe_load(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}
    body_md = _resolve_liquid_for_preview(match.group(2).strip(), front_matter)
    body_html = markdown.markdown(body_md, extensions=["footnotes", "sane_lists", "smarty"])
    body_html = _absolutize_local_urls(body_html, repo_root)
    styles = front_matter.get("_styles", "")
    title = front_matter.get("title", "Preview")
    comments_html = _comments_html(md_path, front_matter, site_config, title)

    html = f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    body {{
      margin: 0;
      background: #f7f5ef;
      font-family: Georgia, "Times New Roman", serif;
      color: #1f1e1a;
    }}
    main {{
      width: min(980px, 100% - 2rem);
      margin: 2rem auto;
      padding: 2rem;
      background: #fffdf8;
      border: 1px solid #e8e2d4;
    }}
    .post-meta {{
      margin: 0 0 1rem;
      color: #6a6457;
      font: 600 .86rem/1.2 system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
    }}
    .preview-comments {{
      margin-top: 2rem;
      border-top: 1px solid #ddd;
      padding-top: 1rem;
    }}
    .comments-title {{
      margin: 0 0 0.75rem;
      font-size: 1.15rem;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
    }}
    .comments-note {{
      font-size: 0.92rem;
      color: #666;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
    }}
{styles}
  </style>
</head>
<body>
  <main class="post">
    <header class="post-header">
      <h1 class="post-title">{title}</h1>
      <p class="post-meta">Preview</p>
    </header>
    <article class="post-content">{body_html}</article>{comments_html}
  </main>
</body>
</html>
"""

    out_html.write_text(html, encoding="utf-8")
    return title, html


async def screenshot(html_path: Path, out_png: Path, width: int = 1600, height: int = 2400) -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": width, "height": height})
        await page.goto(html_path.resolve().as_uri())
        await page.wait_for_timeout(1200)
        await page.screenshot(path=str(out_png), full_page=True)
        await browser.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Regenerate HTML + browser screenshot preview for a markdown post.")
    parser.add_argument("markdown_file", help="Path to the markdown file, e.g. _journal/2025-08-13-ai-dream-domination.md")
    parser.add_argument("--out-dir", default="_preview", help="Output directory (default: _preview)")
    parser.add_argument("--name", default=None, help="Base name for output files (default: markdown filename without .md)")
    args = parser.parse_args()

    md_path = Path(args.markdown_file)
    if not md_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {md_path}")

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    base_name = args.name or md_path.stem
    out_html = out_dir / f"{base_name}.preview.html"
    out_png = out_dir / f"{base_name}.desktop.png"

    repo_root = Path(__file__).resolve().parents[1]
    build_html(md_path, out_html, repo_root)
    asyncio.run(screenshot(out_html, out_png))

    print(out_html.resolve())
    print(out_png.resolve())


if __name__ == "__main__":
    main()
