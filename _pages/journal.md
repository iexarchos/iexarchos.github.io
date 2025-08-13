---
layout: page
permalink: /journal/
title: journal
description: Random thoughts and notes
nav: true
---
<ul class="post-list">
{% assign entries = site.journal | sort: 'date' | reverse %}
{% for entry in entries %}
  <li>
    <h3><a class="post-title" href="{{ entry.url | relative_url }}">{{ entry.title }}</a></h3>
    <p class="post-meta">{{ entry.date | date: '%B %-d, %Y' }}
      {% if entry.tags %}&nbsp; &middot; &nbsp;
        {% for tag in entry.tags %}
          <i class="fas fa-hashtag fa-sm"></i> {{ tag }} &nbsp;
        {% endfor %}
      {% endif %}
    </p>
    {% if entry.summary %}<p>{{ entry.summary }}</p>{% else %}<p>{{ entry.excerpt | strip_html | truncate: 140 }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
