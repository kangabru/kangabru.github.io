---
title: false
---

# {{ site.title }}

Welcome! This is a portfolio of my favourite projects that I have undertaken over the years.

Not sure where to start? Check out my favourite projects:

[Personal]({% post_url 2019-03-26-where-is-kangabru %}){:.big-link}
[Professional]({% post_url 2017-07-06-quickmocks %}){:.big-link}
[Thesis]({% post_url 2014-01-01-thesis %}){:.big-link}

---

{% for post in site.posts %}
{% if post.hidden != 1 %}

## [{{ post.title }} - {{ post.when }}]({{ post.url }})

{{ post.description }}

<a href="{{ post.url }}"><img class="image-medium" src="{{ post.image_url }}"/></a>

{% include tags.html tags=post.tags %}

---

{% endif %}
{% endfor %}
