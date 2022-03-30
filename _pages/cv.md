---
layout: page
permalink: /cv/
title: cv
description: Within this page you can view or download my CV. It will periodically be updated. For any inquiries or questions do not hesitate to contact me.
nav: true
---
{% assign rootpath = '/' | relative_url %}
In case the inline PDF does not appear, you may download the PDF file [here]({{ site.cv.pdf | prepend: pathprefix | relative_url }}).
{% pdf site.cv.pdf | page.title | rootpath %}
