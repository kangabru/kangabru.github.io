---
layout: post
title: Quick Mocks
description: Originally a 'Hack Day' project, this UI mocking utility became loved by devs and designers alike at a prior company. I won 3 awards and a significant windfall for developing it.
when: Jun 2017 - Nov 2018
image_url: images/quickmocks.png
tags: [Jquery, Chrome Extension, Google Analytics]
---

## Key Points
- A `Jquery` based Chrome extension which brings powerful website editing capabilities to _any_ web page.
- Was well received and used by 300+ users in a 1000+ person company.
- As the sole developer I won 3 high profile awards and recognition from the CEO and R&D Director.

---

## Features

`Quick Mocks` (`QM`) lets you modify the layout and text of _any_ webpage quickly and easily to create mock-up designs. Essentially webpages become editable design templates.

Tweak the label on a card component to see if it looks better. Looking for a new banner image? Paste in external images and try them out. `QM` makes it easy to tweak the UI of an actual website without touching a single line of code.

<blockquote>
Think of the browser 'inspector' tool, but on steroids!<br>
- My sales pitch to colleagues
</blockquote>

---

<div class="img-with-text">
    <video controls autoplay loop>
    <source src="/images/quickmock_vids/replace.mp4" type="video/mp4">
    </video>
    <br>
    <span>(Click Play) Example 'replace' feature.</span>
    <br>
    <br>
</div>

---

Here are some videos of my favourite actions:

{:.tags}
[Edit Text](/images/quickmock_vids/edit-text.mp4)
[Move](/images/quickmock_vids/move.mp4)
[Copy and Drag](/images/quickmock_vids/drag-images.mp4)
[Paste Images](/images/quickmock_vids/paste-images.mp4)
[Sort](/images/quickmock_vids/sortable.mp4)
[Screenshot](/images/quickmock_vids/screenshot.mp4)

[Save as single file](/images/quickmock_vids/save.mp4){:.tag}
Compresses all external images and links into a single HTML file which can be re-edited.

[Playground](/images/quickmocks_playground.png){:.tag}
A test friendly environment where users can practice actions.

Some other cool features:
- All actions supported multi-element manipulation. Want to change 5 icons at once? No problem. Need to duplicate a particular button for every card on screen? Easy as. This multi-elemental approach was very powerful when used correctly.
- Copy and paste was available across tabs. Copied data wasn't simply text, it was a collection of independent HTML elements. You could select 5 different text fields on screen, then replace them with 5 icons from another screen. Very useful.

---

[See more explanation and the history here]({% post_url 2017-07-06-quickmocks-features %}){:.big-link}

---

## Tech Specs

`QM` is a chrome extension which runs in the background of every page you open. `JS` is injected to process actions and interact with HTML elements. `CSS` is injected for minimal styling such as to highlight selected elements, and to enable draggable functionality.

### ![Algorithm](/icons/algorithm.png) Algorithm
- Nearly all actions follow a basic 'select -> action' principle.
- `QM` logic is injected into webpage and awaits for user actions.
- `ALT + Click` is used to select one or more elements. These are styled by a `CSS` class.
- Upon action (e.g. duplicate), selected elements are found by that `CSS` class, then code is run to apply the action to each element independently.

### ![Jquery](/icons/jquery.png) Jquery
- `Jquery` is used to handle `CSS` selection and `HTML` manipulation with little code.
- Many basic HTML element actions were already provided by `Jquery` (i.e. copy, paste, delete) which made initial development very easy.
- `Jquery` natively supports multiple element actions. For instance the 'delete' action is a simple 'elements.delete()' action and works for any number of elements without loops.
- `QM` constantly modified classes and interacts with HTML elements. At the time `Jquery` was the easiest and cleanest way to do this.

### ![Chrome](/icons/chrome.png) Chrome Extension
- A browser extension is the only way to inject `QM`-like functionality into every webpage. Chrome was the dev browser of choice which made it the primary supported browser.
- Deployment was performed through Chrome Store which supported decent analytics, A/B versioning, and an employee only download portal.

---

## Challenges

[Continue the article here]({% post_url 2017-07-06-quickmocks-challenges %}){:.big-link}
