---
layout: post
title: Spanish Flash Card Web App
description: A bespoke flash card web app built with <code>Django</code> used to teach myself Spanish vocabulary quickly using data to analyse my progress.
when: Jan 2018
image_url: /images/spanish.png
tags: [Python, Django, Heroku, PostgreSQL, Jquery, Ajax]
---

## Key Points
- A `Django` web app deployed on `Heroku` using a `Postgres` database.
- Applies 'spaced repetition' theory and data tracking to present words at the perfect time.
- Aided in my journey to becoming proficient in Spanish at a C1 level.

---

## Features

At first glance this app looks like a simple flash card app like any other. Underneath, however, its powered by a sophisticated data analytical powerhouse used to track your progress and optimise your learning. Well that's a bit exaggerated, but it _is_ cool.

{:.img-with-text}
![Image of the UI](/images/spanish_ui.gif){:.image-small}<br>
No fancy `JS` frameworks here, just good old `HTML` and `Ajax` calls.

Fill the app with the phrases you want learn and the app cleverly feeds you new phrases once you've begun to master old ones. This [spaced repetition](https://en.wikipedia.org/wiki/Spaced_repetition) technique has found to be effective in learning vocabulary.

Some key features:
- View phrases in a random language or choose one specifically.
- It sports a voice synthesiser (with real accents!) for listening practice.
- Isolate phrases based how easy/medium/hard they are according to your past performance.
- Use keyboard shortcuts to quickly mark words and other actions.
- Group phrases in sets and activate specific sets and/or phrases you wish to practice.
- Import 100s of phrases in one go.

---

{:.img-with-text}
![Images of the content edit UI.](/images/spanish_words.jpg){:.image-medium}<br>
Includes a multi-parameter filter, pagination, and lovely CRUD operations.

---

{:.img-with-text}
![Images of stats.](/images/spanish_graph.jpg){:.image-medium}<br>
Check out your overall performance or dive into specific stats for each phrase.

---

## Tech Specs

This web app was built in `Django` and deployed on `Heroku` with a `Postgres` database. This was built for web in order to practise web development, but also to be able to access the data and progress from any device, anywhere in the world.

### ![The D is silent](/icons/django.png) Django
- A `Python` based server framework used to serve HTML, handle DB calls, and front APIs used by the front end.
- Is DB agnostic so tests are setup with `SQLite` and production with `Postgres`.
- Ships with niceties like user auth, safeguards against SQL injection, powerful admin screens, and much more.
- The 'd' is silent.

### ![Heroku](/icons/heroku.png) Heroku
- A [PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service) used to host the `Django` server and `Postgres` DB.
- Makes deployment is super easy. Simply push to a `GIT` repo and `Heroku` handles the rest.
- The app was built for me and is hosted privately. Their free and dev tiered products are perfect for this use case.

### ![JS](/icons/javascript.png) Front End
- `HTML` is built dynamically through `Django` and its templates. No frontend libraries are used for rendering.
- `Jquery` is used for interactivity and handling server API calls through `Ajax` using `JSON`.
- Phrases are returned in batches and the API is called in advanced in order to eliminate lag under heavy use.
