---
layout: page
title: research
description: 
permalink: /research/
nav: true
---

My research has largely focused on stochastic control, reinforcement learning, optimization, ML applications in neuroscience, and some differential game theory. You can view my doctoral dissertation [here](https://smartech.gatech.edu/handle/1853/59263). Below you will find a selection of my past and current research.

***

<div class="post">

  <ul class="post-list">
    {%- assign research = site.research | reverse -%} 
    {% for item in research %}

    {% assign read_time = item.content | number_of_words | divided_by: 180 | plus: 1 %}
    {% assign year = item.date | date: "%Y" %}

    <li>
      <h3>
        {% if item.redirect == blank %}
          <a class="post-title" href="{{ item.url | prepend: site.baseurl }}">{{ item.title }}</a>
        {% else %}
        <a class="post-title" href="{% if item.redirect contains '://' %}{{ item.redirect }}{% else %}{{ item.redirect | relative_url }}{% endif %}">{{ item.title }}</a>
        {% endif %}
      </h3>
      <p>{{ item.description }}</p>
      <p class="post-meta">{{read_time}} min read &nbsp; &middot; &nbsp;
        {{ item.date | date: '%B %-d, %Y' }}
      </p>
      <p class="post-tags">
        <i class="fas fa-calendar fa-sm"></i> {{ year }}
      </p>
    </li>

    {% endfor %}
  </ul>
</div>
