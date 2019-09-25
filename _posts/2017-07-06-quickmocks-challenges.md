---
layout: post
title: Quick Mocks - Challenges
hidden: 1
---

[Back to original article here]({% post_url 2017-07-06-quickmocks %}){:.big-link}

---

### Saving Pages
By far the hardest challenge with `QM` was saving and re-editing mocks. it was _the_ critical feature necessary for widespread adoption. My dream was to save websites as a _single file_ which could be shared and easily re-edited. In the end it was technically hard, but it took a long time to perfect.

Websites are dynamic and multi-content beats. Often they have dozens of external images, stylesheets, Iframes, you name it.

<blockquote>
How can we save these? Is this even possible?
</blockquote>

Try right click and save a website. You'll see it creates a directory with dozens of files and images. Now when you open it? Often the styling is broken and un-usable for mocks.

Thankfully [developers are awesome](https://github.com/gildas-lormeau/SingleFile) and I was able to achieve my dream in the end. Some challenges I faced:
- This was a completely separate extension. Originally I was able to integrate with the extension through Chrome APIs. This worked but was a bit painful for users.
- Eventually I completely integrating the extension into `QM`. This involved a deep dive into the original code and extracting exactly what I needed. Tricky but doable.
- I had to build a UI to indicate the various stages of download. Downloads were sometimes fickle and my UI had to indicate why.
- The final challenge: re-saving. This is where the user was required to save through Chrome, and not the extension. Work and user testing was done to make the distinction between the 'compression' and 'save' processes. More of a UX issue but a challenge nonetheless.

---

### Performance
The idea of `QM` is was to always available and work on any webpage at any time. To achieve this `QM` awaits silently until a user does something `QM` related.

To achieve the `ALT + Click` action for example, a 'click' event needs to be set on an element or parent element.

**Do we set one on EVERY element on the page?**
Dynamic elements won't work and will probably impact performance

**Do we set one on the body element and find the target on click?**
Elements with existing click events will run their action first (i.e. button and links)

What did I do? Add click events as the mouse hovers in and out of elements. This worked for all elements AND the event could be placed first in the event queue to allow functionality on buttons etc.

What's the problem you ask? over time I noticed that _all_ on my webpage started to slow down the more I used them. The clicks were being added to thousands of elements and each click caused a significant performance impact. More complex site especially.

How did I fix it? Clean up! Not only did I have to add click events, I need to remove old ones when leaving elements. Because of its impact potential, lots of care was made to ensure `QM`  was invisible until needed.

### Designing for Designers
Intuitive UX can be hard to design. It's even harder when there's no UI! `QM` was originally made for devs but quickly found use by non-technical users. All functionality was hidden behind keyboard shortcuts which made it hard for new users and more graphically inclined users. Looking back this is likely what limited its adoption further.

Many steps to were taken to improve usability, for example:
1. Created an extensive documentation page to list all commands and functionality. The problem is that most people don't want to read.
1. Prettied the documentation page and added gifs for _every_ action to provide visual examples.
1. Created a 'playground' page which users could use to experiment and practice their skills in a friendly environment. All gifs used the 'playground' in order to provide a direct and reproducible reference.

Had I continued with `QM` development, I would have liked to build an optional UI to make selection and actioning easier. Subsequent tools such a [Visbug](https://github.com/GoogleChromeLabs/ProjectVisBug) implement this well.

---

### The feature that never was

The number one requested feature? Undo.

This was the biggest feature I never got to work on. The implementation always seemed tricky and I sadly left before being able to implement it. Some challenges:

**Websites are dynamic!** You could save the page with `QM` to kills all JS, but user often  editing live pages. On scroll too far and all of those card edits get wiped!

**How do we store the state?** Common undo algorithms [save and restore states](https://en.wikipedia.org/wiki/Memento_pattern) to implement undo. With a website though

---

[Back to original article here]({% post_url 2017-07-06-quickmocks %}){:.big-link}