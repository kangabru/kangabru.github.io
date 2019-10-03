---
layout: post
title: Student Timetable
description: A fully fledged <code>Android</code> timetable app used to track my class schedules at university. It came fully featured with a tutorial page, snazzy animations, and a custom built UI.
when: Jul 2012
image_url: /images/student_timetable.jpg
tags: [Java, Android, SQLite]
---

## Key Points
- An `Android` app written in `Java` using an `SQLite` database.
- Sports everything you'd expect from an app - a custom styled UI with animations, a tutorial page, and basic CRUD operations including copy and paste.
- Built for personal use (3+ years of use) and to learn about `Android` development while studying at university.

## Features

This was an app designed to digitise my hand-made timetables back at university. I considered similar apps at the time to be overly complicated or lacking features that I wanted. I also wanted to practice app development - my new interest at the time.

{:.img-with-text}
![Image of manual timetable.](/images/student_timetable_manual.jpg){:.image-small}
An example of my actual timetable I made each semester. I wanted this in app form.

Some features include:
- A UI of my own design with purpose-built components.
- Multi-week timetable support with automatic week switching.
- Animations everywhere!
- Smooth 'sticky swipe' navigation when swiping between days or weeks.
- A colour picker to style different subjects.
- Dynamic screen size support.

---

<div class="img-with-text">
    <video controls autoplay loop width="500">
    <source src="/images/student_timetable_ui.mp4" type="video/mp4">
    </video>
    <br>
    <span>(Video) Look at that menu spin!</span>
    <br>
    <br>
</div>

---

## Tech Specs

Everything was built using `Java`, `Android`, and `SQLite`. Many of the components were custom built in order to realise my vision. Here are a few:
- The 'week selector' and 'week edit' screens are custom drawn according to how many periods and days the user sets up.
- 'Sticky swipe' sliders which animate smoothly to fixed positions after a user has stopped swiping. No libraries seemed to fit my needs at the time.
- Popups which feature a transparent background, coloured edges, and that ridiculous spin animation.
- The custom angled menu navigator at the bottom of the screen which is also transparent.