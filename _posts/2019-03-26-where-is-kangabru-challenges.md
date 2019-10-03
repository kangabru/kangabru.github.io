---
layout: post
title: Where is Kangabru? Mistakes and Challenges
hidden: 1
---

[Back to original article here]({% post_url 2019-03-26-where-is-kangabru %}){:.big-link}

---

### Expanding Images ([Try it out here](https://whereiskangabru.com/#/album/2019_costa_rica_central_coast))
Embarking on a personal project is always exciting, and for this project I was eager to show off my chops and create a slick, modern webpage. Naturally 'animations' came to mind. I discovered a [fantastic image gallery concept](https://tympanus.net/Development/ImageGridEffects/index3.html) and decided to use it.

<blockquote>
The code is right there, it shouldn't be too hard right?<br>
- Excitable me
</blockquote>

#### The process
Converting the animation example started off well:
- I reimagined the original `JQuery` code into a standalone `React` component.
- The algorithm took the clicked image, calculated a `CSS` transform to make it big, then animated it via `CSS`. It was buttery smooth, and I was pleased.

What I failed to account for was future enhancements. Naturally I wanted some image gallery nav controls shortly after. Some problems:
- The enlarged image was the original image element but blown up.
- If I swapped the image via the gallery, how would I animate to the correct image on close?
- How would I reinstate the original image on close?

Whoops, I did the conversion wrong! The original concept used a floating 'image preview' element and animated that to specific images. Had I intended to have those features beforehand, I would have questioned my original algorithm. I was blindsided by the excitement of building something.

With some more work I got the animation working, but it took longer than expected.

#### Lessons Learnt:
- Breaking new ground takes time to implement, to test, and it still might be buggy.
- Spec out your design! I was eager to build and jumped in head first. Some simple design planning would have saved me some time.
- Keep it simple stupid! Do you need these animations right now?

---

### Image Navigation ([Try it out here](https://whereiskangabru.com/#/album/2017_colombia_north_colombia/012.jpg))

Once the animation was complete, I wanted image navigation controls. Initially the actions were: next, previous, and close. Simple right? I created the UI, wrote the code, hooked it all up to the animation component. Easy enough.

Then I wanted a seamless transition when the thumbnail switched to the full image. Next I wanted swipe between photos on mobile. Of course I need to let users zoom into the image too. Later I wanted an image gallery slider so users could navigate the album easier.

My ideal image viewer became more and more complicated. There are so many lightweight, feature rich components out there that I should have used one of them. Again I could have saved a lot of time, but this is how you learn.

#### Lessons Learnt:
- I should have designed the component properly before writing code.
- I should have explored existing options. Something as common as an image viewer would of course have oodles of options. The decision to use one would have been easy.
- My current image viewer still has problems and could be improved. Instead of adding complexity I might opt for an existing library in future.

---

### Masonry Grid ([Try it out here](https://whereiskangabru.com/#/albums))

I wanted a classic masonry grid to showcase my albums and images. The popular library [Masonry](https://masonry.desandro.com/) was of course my first choice.

The problem started when trying to retrofit the library into my `React` app. Duck tape solutions exist to combine the two libraries, but I've never been able to get it working quite perfectly. The following issues in my Masonry implementation still exist:
- Sometimes images load in a single vertical line despite my attempts to stop it.
- Sometimes the whole grid reorders itself on image load, again despite my attempts to stop it.

Whilst the library initially looked promising, it's been frustrating trying to fix the interoperability issues. In future, I might implement a more [react specific solution](https://codesandbox.io/embed/26mjowzpr).

#### Lessons Learnt:
- I should have explored more solutions specific to my use case before committing to a particular library. I.e. `React` specific libraries instead of the most popular one.
- Knowing that Masonry uses `JQuery`, I should have questioned its interoperability with `React` and researched some problems that might have arisen.

---

[Back to original article here]({% post_url 2019-03-26-where-is-kangabru %}){:.big-link}