---
layout: post
title: Where is Kangabru?
ref: kangabru
description: Like, where is he man? Well this site lets you find out! Originally built for friends and family, this web app lets you explore my adventures with a map and pretty photos.
when: Mar 2019
image_url: /images/wikb_home.jpg
tags: [React, Firebase, Typescript, JS, Redux, HTML, Less, Webpack]
link: https://whereiskangabru.com/
---

## Key Points
- A single page web app built in `React` and hosted on `Firebase`.
- Incorporates modern technologies and is highly scalable without further effort.
- Looks pretty cool I reckon 👌

---

## Features

`Where is Kangabru?` is all about showcasing beautiful places that I have visited in a fun and interactive way. Friends and family can see where I am, and also explore my favourite places around the globe.

<blockquote>
I love it, I can keep an eye on him while he's off on his amazing adventures.<br>
- Mom
</blockquote>

It sports:

{:.img-with-text}
![Map Screen](/images/wikb_map.jpg)<br>
An interactive map with my current and previous locations.

---

{:.img-with-text}
![Albums Screen](/images/wikb_albums.jpg)<br>
A vast and growing collection of my travel photos and albums.

---

{:.img-with-text}
![CMD and Game Screen](/images/wikb_cms_game.jpg)<br>
[A fully playable game!](https://whereiskangabru.com/#/play) and CMS to manage photos and content.

---

## Tech Specs

This is a single page application built from the ground up by me. The app utilises various technologies that I wanted to try out at the time.

### ![Firebase](/icons/firebase.png) Firebase
- Uses `Firebase` for hosting, auth, photo storage, and cloud functions.
- Cloud functions are used to create image thumbnails, and to compress DB entries into a single read on page load.
- `Firebase` was chosen for fantastic dev usability, low cost, and full [GCP](https://cloud.google.com/) integration.

### ![React](/icons/react.png) React
- All code is run client side which simplifies deployment. I simply host the static files which negates the need to manage a traditional server/DB setup.
- `React` apps are component based which allows for complex, yet maintainable single page applications.
- The diverse `React` and `NPM` ecosystem allow me to develop more, faster.

### ![Redux](/icons/redux.png) Redux
- `Redux` is used to manage a centralised application state.
- Server call responses update the `Redux` state, which `React` then uses to render the UI.
- The one way data flow reduces bugs, and allows for easy UI testing based on state data.

### ![Performance](/icons/cog.png) Performance
- The initial page load is kilobytes which loads instantly and signals the page is loading.
- Home page data is loaded in a single DB read, as is the data for each individual album.
- Server calls, larger client side processes, and UI rendering are all async.
- Thumbnails are used extensively to improve loading speed and animation performance.
- `Firebase` handles content delivery which uses Google's global CDN and servers.

### ![JS Packages](/icons/javascript.png) JS Packages
- `Tailwinds`: A fantastic library which generates atomic `CSS` utility classes. It helps prevent breakages, simplifies responsive design, and reduces the size of stylesheets through the app.
- `Leaflet`: Renders and handles all maps used in the app.
- `Redux Thunk`: Enables async `Redux` actions.
- `React Router`: Enables url navigation with the single page app.
- `Webpack`: Builds the app. Includes transpiling `Typescript`, compiling `Less`, building `Tailwinds`, running dev/prod builds, tree shaking etc.
- `Jest`: Used for `JS`, UI, and [snapshot](https://jestjs.io/docs/en/snapshot-testing.html) testing.

---

## Mistakes and Challenges

[Continue the article here]({% post_url 2019-03-26-where-is-kangabru-challenges %}){:.big-link}