---
title: false
---

# {{ site.title }}

Welcome! This is a portfolio of my favourite projects that I have undertaken over the years.

Not sure where to start? Check out my favourite:

[Professional Project]({% post_url 2017-07-06-quickmocks %}){:.big-link}
[Personal Project]({% post_url 2019-03-26-where-is-kangabru %}){:.big-link}

---

{% for post in site.posts %}
{% if post.hidden != 1 %}

### [{{ post.title }} - {{ post.when }}]({{ post.url }})

{{ post.description }}

<img class="image-medium" src="{{ post.image_url }}"/>

{% include tags.html tags=post.tags %}

---

{% endif %}
{% endfor %}
