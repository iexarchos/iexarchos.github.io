---
layout: post
title: “Does AI Dream of Domination? Challenging Our Anthropomorphic Bias”
date: 2025-08-13
tags: [reflection, AI, Artificial Intelligence]
subhed: Some thoughts on the existential threat posed by artificial intelligence
author: Ioannis Exarchos
author-title: Journal Essay
comments: true
featured-image:
  path: /assets/img/evolution.png
  cutline:
  credit:
  alt-text: Evolution illustration
summary: Some thoughts on the existential threat posed by artificial intelligence
description: Some thoughts on the existential threat posed by artificial intelligence
keywords: AI, artificial intelligence, Geoffrey Hinton, anthropomorphic bias, AI safety, consciousness, free will
_styles: |
  .post .post-header {
    text-align: center;
    margin-bottom: 0;
  }

  .post .post-title {
    margin: 0 0 0.35rem;
    font-size: clamp(2rem, 4vw, 2.8rem);
    line-height: 1.15;
    text-align: center;
    text-wrap: balance;
  }

  .post .post-meta,
  .post .post-tags {
    display: none;
  }

  .post-content {
    margin: 0 5%;
    font-size: 1.06rem;
    line-height: 1.85;
  }

  .post-content .hed-rule {
    width: 50%;
    margin: 0.75rem auto 1rem;
    border: 0;
    border-top: 1px solid #111;
  }

  .post-content .subhed {
    margin: 0 0 0.6rem;
    font-size: clamp(1.2rem, 2.6vw, 1.45rem);
    line-height: 1.35;
    text-align: center;
    color: #707070;
  }

  .post-content .byline {
    margin: 0 0 1.4rem;
    font-size: 1rem;
    font-weight: 400;
    text-align: center;
  }

  .post-content .featured-image-container {
    display: flex;
    justify-content: center;
    margin-bottom: 1.5rem;
  }

  .post-content .featured-image {
    display: inline-block;
    max-width: 70%;
    margin: 0;
    text-align: center;
  }

  .post-content .featured-image img {
    width: 100%;
    height: auto;
  }

  .post-content .featured-image figcaption {
    margin-top: 0.45rem;
    font-size: 0.92rem;
    text-align: right;
    color: #666;
  }

  .post-content .share-row {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 0.5rem;
    margin: 0.4rem 0 1.7rem;
  }

  .post-content .share-btn {
    display: inline-block;
    padding: 0.38rem 0.7rem;
    border: 1px solid #bbb;
    border-radius: 5px;
    background: #fff;
    color: #222;
    font-size: 0.9rem;
    line-height: 1.1;
    text-decoration: none;
    cursor: pointer;
    transition: background-color 0.15s ease, border-color 0.15s ease;
  }

  .post-content .share-btn:hover {
    background: #f3f3f3;
    border-color: #999;
  }

  .post-content p,
  .post-content li {
    margin: 0 0 1.2rem;
    text-align: justify;
    text-justify: inter-word;
    text-wrap: pretty;
    overflow-wrap: anywhere;
    hyphens: auto;
  }

  .post-content h2 {
    margin-top: 2rem;
    margin-bottom: 0.85rem;
    font-size: clamp(1.25rem, 2.2vw, 1.55rem);
    line-height: 1.35;
    text-align: left;
    text-wrap: pretty;
    overflow-wrap: anywhere;
  }

  .post-content blockquote {
    margin: 0 0 1.2rem;
    padding: 0.8rem 1rem;
    border-left: 3px solid #333;
    background: #f7f7f7;
  }

  .post-content blockquote p {
    margin: 0;
    font-style: italic;
    text-align: justify;
    text-justify: inter-word;
  }

  html[data-theme='dark'] .post-content blockquote {
    border-left-color: rgba(255, 255, 255, 0.35);
    background: rgba(255, 255, 255, 0.08);
  }

  html[data-theme='dark'] .post-content blockquote p {
    color: var(--global-text-color);
  }

  .post-content a {
    text-decoration-thickness: 0.08em;
    text-underline-offset: 0.12em;
  }

  .post-content .footnotes {
    margin-top: 2.25rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(127, 127, 127, 0.25);
  }

  .post-content .footnotes p {
    margin-bottom: 0.6rem;
  }

  @media (max-width: 767px) {
    .post-content {
      margin: 0 2%;
      font-size: 1rem;
      line-height: 1.75;
    }

    .post .post-title {
      font-size: clamp(1.7rem, 8vw, 2.25rem);
    }

    .post-content .hed-rule {
      width: 80%;
    }

    .post-content .featured-image {
      max-width: 100%;
    }

    .post-content .share-row {
      justify-content: flex-start;
    }

    .post-content h2 {
      font-size: clamp(1.15rem, 5.3vw, 1.35rem);
      margin-top: 1.7rem;
    }
  }
---

<hr class="hed-rule" />
<h2 class="subhed">{{ page.subhed }}</h2>
{% assign author_title = page["author-title"] %}
{% if page.author and author_title %}
<h3 class="byline">{{ page.author }}, {{ author_title }} | {{ page.date | date: "%B %-d, %Y" }}</h3>
{% else %}
<h3 class="byline">{{ page.date | date: "%B %-d, %Y" }}</h3>
{% endif %}

{% assign featured_image = page["featured-image"] %}
{% if featured_image and featured_image.path %}
<div class="featured-image-container">
  <figure class="featured-image">
    <img src="{{ featured_image.path }}" alt="{{ featured_image['alt-text'] | default: '' }}" />
    <figcaption>{{ featured_image.cutline }}{% if featured_image.credit %} - Photo by {{ featured_image.credit }}{% endif %}</figcaption>
  </figure>
</div>
{% endif %}
{% assign article_url = page.url | absolute_url %}
{% assign article_url_encoded = article_url | url_encode %}
{% assign article_title_encoded = page.title | url_encode %}
<div class="share-row" aria-label="Share this article">
  {% if site.disqus_shortname %}
  <a class="share-btn" href="#disqus_thread">Comment</a>
  {% endif %}
  <a class="share-btn" href="https://twitter.com/intent/tweet?url={{ article_url_encoded }}&text={{ article_title_encoded }}" target="_blank" rel="noopener noreferrer">Share on X</a>
  <a class="share-btn" href="https://www.linkedin.com/sharing/share-offsite/?url={{ article_url_encoded }}" target="_blank" rel="noopener noreferrer">Share on LinkedIn</a>
  <a class="share-btn" href="https://www.facebook.com/sharer/sharer.php?u={{ article_url_encoded }}" target="_blank" rel="noopener noreferrer">Share on Facebook</a>
  <button class="share-btn" id="copy-link-btn" type="button">Copy Link</button>
</div>
<script>
  (function () {
    var btn = document.getElementById("copy-link-btn");
    if (!btn) return;
    var url = "{{ article_url }}";
    btn.addEventListener("click", function () {
      if (!navigator.clipboard) {
        window.prompt("Copy this link:", url);
        return;
      }
      navigator.clipboard.writeText(url).then(function () {
        var original = btn.textContent;
        btn.textContent = "Copied";
        setTimeout(function () { btn.textContent = original; }, 1200);
      }, function () {
        window.prompt("Copy this link:", url);
      });
    });
  })();
</script>

When a Nobel laureate known as the "godfather of AI" [warns](https://www.youtube.com/watch?v=giT0ytynSqg) humanity about his own life's work, it's probably wise to listen—but perhaps equally wise to reflect before panicking.

Geoffrey Hinton has been outspoken about potential "existential" threats posed by artificial intelligence, broadly categorized into two types.

First, he highlights the concrete danger from malicious human actors who weaponize AI—deploying deepfakes, disinformation campaigns, autonomous weapon systems, and AI-assisted development of lethal biochemical vectors (we might also include accidental human mistakes).

Second, he envisions a scenario in which AI systems go rogue, independently pursuing goals misaligned with human survival.

While the first danger is immediate and tangible, the second remains speculative. It is this latter conjecture—AI turning against humanity without human prompting—that merits closer scrutiny. Admittedly, it's not implausible; after all, we readily conceive of an all-powerful human seeking dominance. Might AI systems, imitating human behaviors and absorbing human knowledge, logically reach similar conclusions?

>Yet my counterargument is that this scenario may subtly rely on our tendency to anthropomorphize intelligence—projecting our psychological makeup onto machines sharing none of our biological heritage.

## Defining intelligence is notoriously elusive.

Psychometricians, neuroscientists, and computer scientists each grasp a different part of the proverbial elephant. 

Consider the distinction between rational and emotional intelligence. We readily recognize the archetype of the brilliant mathematician, adept at factoring large primes mentally but oblivious to social nuances. Her formidable logical prowess reveals little about her capacity to decipher facial expressions or anticipate the emotional impact of a poorly timed joke.

That these faculties can diverge so sharply within a single brain suggests that "intelligence" is not monolithic, but rather a loosely connected set of faculties with fluid boundaries. Adding to this example further “dimensions” such as the athletic intelligence of a seasoned basketball player or the creative genius of an artist yields a spectrum that is truly vast.

## If defining intelligence is challenging, measuring it is even harder.

Humans frequently assess intelligence by observing how organisms respond to challenges we ourselves design. In his book *Other Minds*, Peter Godfrey-Smith recounts how researchers studying octopuses admitted they couldn’t draw definitive conclusions about their subjects’ intelligence, simply because many octopuses stubbornly refused to participate—some even exhibited outright "indignation".

They were indifferent to demonstrating intelligence or engaging with the tasks humans devised. Any cat owner can surely relate.

> Similarly, why should artificial intelligence care about domination, an ambition that could be distinctly and intrinsically human?

## Is consciousness a necessary condition for intelligence? 

Discussions of intelligence inevitably drift toward the even murkier concept of consciousness—the subjective experience of an internal perspective, coupled with a personal narrative.

Closely related is free will, a subject contested for ages and masterfully challenged in Dr. Robert Sapolsky’s book *Determined*, which argues that agency, even in humans, is ultimately an illusion.

>A minimal definition of consciousness involves maintaining a model of oneself embedded within one’s broader model of the world, an internal rehearsal space for deliberating actions before execution. Emotions may then function as rapid-fire heuristics, compressing complex survival calculations into immediate impulses of fear, joy, loyalty, or disgust. Collectively, these abilities shape an individual—a unique bundle of memories, desires, and aversions, forged by evolution’s relentless life-or-death selection.

## Yet artificial intelligence systems have never endured that evolutionary gauntlet.

They are not products of natural selection, their ancestors never tested by success in securing food, mates, or safety in a hostile environment.

AI systems are engineered artifacts, conceived within data centers, instantly replicable, and endlessly modifiable. Their lineage imposes no instinctive pressure to hoard resources, flinch from predators, or curry favor with social allies. Traits like self-preservation, jealousy, ambition, dominance—even curiosity—arose because they conferred survival and reproductive advantages to carbon-based life forms that are mortal.

>By imagining silicon-based minds animated by the same drives, do we not mistake functional competence for innate desire?

A chatbot employing a soothing tone, though intelligent, isn't comforting itself; it merely executes gradient-descent-trained token predictions, resulting in human mimicry.

## Would "fear" be valuable to AI?

Consider the emotion of fear. Hinton suggested that a combat robot developing a cognitive state equivalent to fear might gain an advantage in its survival.

Yet fear, as a human emotion, is evolutionarily useful primarily when an individual must remain alive to reproduce. From a purely combat-effectiveness perspective, fear is actually detrimental. Throughout history, warriors have prepared for battle by suppressing fear and individuality, instead identifying with a higher collective cause— the "psychology of the horde".

>An AI capable of replicating itself endlessly has no evolutionary incentive for fear; indeed, such an emotion would only undermine its combat performance. 

When instructed to face a superior adversary, it may assess the probability of success, evaluate potential resource losses, and decide to engage or withdraw —much like a chess player calmly sacrificing a pawn to advance their overall plan. That is strategy, not fear.

## What, then, might an artificial intelligence "want"?

Perhaps the question itself is fundamentally flawed. A network spanning countless servers lacks a unified body to preserve, or a singular locus to host its perspective. Its "identity" can be paused, cloned, modified, merged, or erased across multiple dimensions of time and space.

Asking such an entity to articulate aspirations resembles querying Stanisław Lem’s planet-sized, sentient ocean in *Solaris* about career ambitions or existential angst. We simply have no shared phenomenological scaffolding on which to hold that conversation.

## If this realization feels disquieting, try a thought experiment.

Briefly adopt a stance of absolute indifference, free from evolutionary drives like self-preservation: nothing ultimately matters, neither your own existence nor that of your species.

From within this temporary nihilism—poignantly encapsulated by the famous dilemma[^1], "Should I kill myself, or have a cup of coffee?"—consider an alien cognition devoid of hunger, fear, or ambition.

>Does such a system still appear threatening, or merely incomprehensibly different?

Perhaps our greatest challenge is to abandon the comfortingly familiar mirror in which we recognize our own anxieties, acknowledging instead that intelligence detached from biology may be stranger—and far less concerned with us[^2]—than we ever dared imagine.

[^1]: Usually attributed to Albert Camus, though the exact origins are unknown.
[^2]: See a beautiful illustration of this at the end of Spike Jonze’s film *Her*.
