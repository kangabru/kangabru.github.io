---
layout: post
title: Galactic Reign
description: A multi-touch <code>Android</code> game sporting a purpose built game engine, collision detection, and 3D renderer.
when: Aug 2013
image_url: /images/galactic_reign.jpg
tags: [Java, Android]
---

## Key Points
- An `Android` game written in `Java` and built as a learning experience at university.
- Features a custom game engine, 3D rendering, collision detection etc.
- Overcame many technical challenges, but realised the hardest challenge was making the game actually fun.

## Features

Whilst never realised into a fully fledged game, this summer project served as a great learning experience and is packed with cool tech (in my opinion).

---

<div class="img-with-text">
    <video controls autoplay loop width="500">
    <source src="/images/galactic_reign_ui.mp4" type="video/mp4">
    </video>
    <br>
    <span>(Video) The planet is key to the game, so the menu displays it front and centre. Notice that the land mass drifts, and the rings orbit around the planet gracefully.</span>
    <br>
    <br>
</div>

---

<div class="img-with-text">
    <video controls autoplay loop width="500">
    <source src="/images/galactic_reign_game.mp4" type="video/mp4">
    </video>
    <br>
    <span>(Video) The aim of the game is survival. Destroy the rain of asteroids that come your way with various weapons.</span>
    <br>
    <br>
</div>

---

<div class="img-with-text">
    <video controls autoplay loop width="500">
    <source src="/images/galactic_reign_menu.mp4" type="video/mp4">
    </video>
    <br>
    <span>(Video) The game features cool animations like this seamless masking interaction with the menu.</span>
    <br>
    <br>
</div>

---

{:.img-with-text}
![Image of different planets.](/images/galactic_reign_planets.jpg){:.image-medium}
The game features various planets, game modes, weapons etc. Weapons include rapid-fire bullets, lasers, and bombs.

---

## Tech Specs

### Game Engine
- Uses a clean, custom-made game engine. Multi-threading is used to separate CPU intensive tasks such as state updates, rendering, and collision detection.
- External libraries were not used in order to learn about and implement the engine myself.
- Collision detection is implemented via [spatial partitioning](https://en.wikipedia.org/wiki/Space_partitioning), hit boxes, and [bezier curves](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) for more intricate objects.

### Asteroids
- Rendered on-the-fly using bezier curves instead of sprites.
- Bezier curves allow each asteroid shape to be unique, have custom colours, and to maintain globally lit shadows as they rotate.
- Bezier curves allow for accurate collision detection after bullets have entered their hit boxes.
- Animated via simple particle physics to move through the world and interact with other objects.

### 3D Saturn Rings
- Purpose built pseudo-3D logic was made to render the Saturn rings.
- The logic uses the standard 2D drawing library but with masks and transforms that render the rings in 3D space.
- 3D libraries were not used as to minimise bloat, and because the rings are only a minor part of the graphics.

## Lessons Learnt

This was a great project to learn about `Android` and game development. I was able to execute my vision technically and overcome various challenges on the way.

The hardest challenge, however, was making the game actually fun. I had so much fun making the game, I never stopped to make it enjoyable for others. Definitely a learning moment, and perhaps I will finish the game in future.