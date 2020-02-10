---
layout: post
title: Color Pickers
description: Take the guess work out of colors with these color picking apps. Are you a photographer? Then achieve the perfect skin tones in your photos. Color-blind? Then identify colors by their name quickly and easily.
when: Jan 2020
tags: [Python, Qt]
image_url: /images/color_pickers.jpg
---

## Key Points
- Two color picking apps which help users work with colors easily on the desktop.
- The [Skin Tone Checker](#skin-tone-checker) app helps photographers to achieve the perfect skin tones in their photos.
- The [Color Identifier](#color-identifier) app helps color-blind users identify colors by name such as 'pink' or 'purple'.
- App were built using `Qt` and `Python`, and support all desktop operating systems.

---

{% include github_link_header.html id="skin-tone-checker" title="Skin Tone Checker" link="https://github.com/kangabru/skin-tone-checker" %}

![Image of the UI](/images/color_picker_skin_tone.jpg){:.image-medium}<br>

Achieve those perfect skin tones in your photos using this skin tone based color picker.

## Features
- Pick colors on screen and visually compare them to the perfect skin tone color range.
- Watch a specific area while you make color adjustments in external apps.
- Identify problems and see hints to improve the skin tone - e.g. when the saturation is too high.
- Fix the window above others to view the color changes whilst editing in external apps like Photoshop or Lightroom.
- Useful for photographers and videographers, especially those who are color-blind.

[Read about how the app was made]({% post_url 2020-02-01-color-pickers-tech-specs %}){:.big-link}

---

{% include github_link_header.html id="color-identifier" title="Color Identifier" link="https://github.com/kangabru/color-identifier" %}

![Image of the UI](/images/color_picker_identifier.jpg){:.image-medium}<br>

Identify colors by name like 'pink' or 'purple' using this color picker identifier.

## Features
- Pick colors anywhere on screen and the closest matching color name will be displayed.
- Includes a slow-mo mode for pixel accurate picking.
- Use the default color names or create your own. The app also ships with additional name lists such as [CSS](https://www.w3schools.com/colors/colors_groups.asp), [xkcd](https://xkcd.com/color/rgb/), and even [Crayola](https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors) color names.
- Useful for color-blind users who struggle to differentiate between subtle color differences.

[Read about how the app was made]({% post_url 2020-02-01-color-pickers-tech-specs %}){:.big-link}
