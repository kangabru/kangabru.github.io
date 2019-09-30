---
layout: post
title: Quick Mocks - Challenges
hidden: 1
---

[Back to original article here]({% post_url 2017-07-06-quickmocks %}){:.big-link}

---

### Saving Pages
By far the hardest challenge with `Quick Mocks` (`QM`) was saving and re-editing mocks. it was _the_ critical feature necessary for widespread adoption. My dream was to save websites as a _single file_ which could be shared and easily re-edited. In the end it wasn't technically hard, but it took a long time to perfect.

Websites are dynamic and multi-content beasts. Often they have dozens of external images, stylesheets, Iframes, you name it.

<blockquote>
How can we save these? Is this even possible?<br>
- Me at the time
</blockquote>

Try right click and save a website. You'll see it creates a directory with dozens of files and images. And when you open it? Often the styling is broken and un-usable for mocks.

Thankfully [developers are awesome](https://github.com/gildas-lormeau/SingleFile) and I was able to achieve my dream in the end. Some challenges I faced:
- This was a completely separate extension. Originally I was able to integrate with it through Chrome APIs. This worked but required users to install a second extension.
- Eventually I completely integrated the extension into `QM`. This involved a deep dive into the original code to extract exactly what I needed. Tricky but doable.
- I had to build a UI to indicate the various stages of download. Downloads were sometimes fickle and my UI had to indicate why.
- The final challenge: re-saving. This is where the user was required to save through Chrome, and not the extension. Work and user testing was done to make the distinction between the 'compression' and 'save' processes. More of a UX issue but a challenge nonetheless.

<div class="img-with-text">
    <video controls autoplay loop width="250">
    <source src="/images/quickmock_vids/save.mp4" type="video/mp4">
    </video>
    <br>
    <span>(Click Play) Save and compression into a single file.</span>
    <br>
    <br>
</div>

---

### Designing for Designers
Intuitive UX can be hard to design. It's even harder when there's no UI! `QM` was originally made for devs but quickly found use by more visual users - like designers. All functionality was hidden behind keyboard shortcuts which made it hard for new and graphically inclined users. Looking back, this is likely what limited its adoption further.

Many steps to were taken to improve usability, for example:
1. Created an extensive documentation page to list all commands and functionality. The problem is that most people don't want to read.
1. Prettied the documentation page and added gifs for _every_ action to provide visual examples.
1. Created a [playground page](/images/quickmocks_playground.png) which users could use to experiment and practice their skills in a friendly environment. All gifs used the 'playground' in order to provide a direct and reproducible reference.

Had I continued with `QM` development I would have liked to build a UI to make selection and actioning more visual. Subsequent tools such a [Visbug](https://github.com/GoogleChromeLabs/ProjectVisBug) implement this well.

{:.img-with-text}
![Quick Mocks features page](/images/quickmocks_features.png)
`QM` feature search and explanation page.

Other challenges involved getting users to think about a website's structure. Block elements typically display vertically, but inline ones horizontally. The sibling selector action used the left/right arrows, so if elements were displayed vertically, then pressing right to select the element underneath was confusing.

A UI might have helped solve the problem, but I resorted to running small `QM` sessions to users who wanted it.

---

### Performance
The idea for `QM` was that it had to function on any webpage and be ready at any time. To achieve this, `QM` had to sit silently until a user selected or actioned something.

To achieve the `ALT + Click` select action for example, a 'click' event needs to be set on an element or parent element.

*"Do we set an event to EVERY element on the page?"*
Dynamic elements won't work + this will likely impact performance.

*"Do we set one on the body element and find the target on click?"*
Elements with existing click events will run their action first (i.e. button and links).

What did I do? Added click events as the mouse hovers into elements. This worked for all elements AND the event could be placed first in the event queue to override buttons etc.

What's the problem you ask? Over time I noticed that _all_ webpages started to slow down the more I used them. Click events were being added to thousands of elements and each click caused a significant performance impact. Not good!

How did I fix it? Clean up! Not only did I have to add click events, I needed to remove old ones when leaving elements.

`QM` had lots of impact potential as it ran on all websites. Lots of work like this was made to ensure `QM` was completely invisible until needed.

---

### The feature that never was

The number one requested feature? Undo. This was the biggest feature that I never got to work on.

`QM` can be _very_ dynamic. Users can select an element, the element's parent, _that_ element's parent, then perform actions on all three at once. Dealing with nested data types like this is uncommon. The implementation always seemed tricky and I departed the company before being able to implement it.

[The Memento algorithm](https://en.wikipedia.org/wiki/Memento_pattern) saves and restore states to implement undo. Websites can be LARGE though, do you really want to save a whole copy of the `HTML` each time you duplicate a button? If not the entire website, how would one save the state of multiple potentially nested elements?

Something akin to the [Command Pattern](https://en.wikipedia.org/wiki/Command_pattern) seemed more suitable. One solution that might have worked is as follows:
- Create an appropriate 'undo' action for each 'normal' action. E.g. To undo a 'duplicate' action you simply 'delete' the new elements.
- As a user actions elements, tag them with a unique `CSS` class to identify them later.
- Track the actions in a stack. Track what the action was and the `CSS` identifier.
- When an action is undone, find the elements using the `CSS` identifier, then perform the action's 'undo' function.
- Place undone actions in another stack to permit 'redo' actions later.

Some problems:
- *How does this work for editing text?* Editing text doesn't add/remove elements so one might have had to duplicate and hide versions of the text fields as they were edited.
- *How does this work for saved pages?* If undo is achieved using actual `HTML` elements, then all of those edits would be available when the file is opened at a later date. Is this desired behaviour? Could you find and delete the undo history before a page is saved?

All-in-all a delicious problem, it would have been great to solve!

---

[Back to original article here]({% post_url 2017-07-06-quickmocks %}){:.big-link}