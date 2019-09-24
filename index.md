---
# tabtitle: # This is the home page so don't add an additional title
---

# {{ site.title }}

Welcome dear user. Below you will find various projects I have undertaken over the years. Please enjoy!

---

{% for post in site.posts %}
{% if post.hidden != 1 %}

### [{{ post.title }} - {{ post.when }}]({{ post.url }})

{{ post.description }}

<img src="{{ post.image_url }}"/>

<p class="tags">
{% for tag in post.tags %}
    <span>{{ tag }}</span>
{% endfor %}
</p>

---

{% endif %}
{% endfor %}
