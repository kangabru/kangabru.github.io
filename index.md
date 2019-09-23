---
# tabtitle: # This is the home page so don't add an additional title
---

# Kangabru Portfolio

G'day bru! What you see below is a masterclass in programming intellect and innovation. Never before has such an esteemed collection of programming apps been up for display before your very eyes.... that is until, today.

Welcome my venerated guest. Please enjoy.

---

<!-- ### [Where is Kangabru?](/project/where_is_kangabru)

Like, where is he man? [Well visit here to find out](). This personal site was built for friends and family to keep track of my travels around the world. It also has some pretty photos.

[Project 1 Title](/project1)
<img src="images/test.png?raw=true"/>
<div class="tags">
    <span>Tag #1</span>
    <span>Tag #2</span>
    <span>Tag #3</span>
</div>

--- -->


{% for post in site.posts %}

### [{{ post.title }}]({{ post.url }})

{{ post.description }}

<img src="{{ post.image_url }}"/>

<div class="tags">

{% for tag in post.tags %}
    <span>{{ tag }}</span>
{% endfor %}

</div>

---

{% endfor %}
