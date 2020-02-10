---
layout: post
title: Color Pickers - How do they work?
hidden: True
---

## Tech Specs

- Both apps were built in `Qt` using `Python` which support all desktop operating systems.
- `Qt` includes many useful classes that make dealing with colors and pixels very easy.
- Apps are packaged into single executable files via [Pyinstaller](https://pyinstaller.readthedocs.io/en/stable/).

## Skin Tone Checker

![Image of the UI](/images/color_picker_skin_tone.jpg){:.image-medium}<br>

### Finding The Perfect Skin Tone Range

Editing photos as a color-blind person is tricky so simplifying that process is always a plus. One day I watched this [this video](https://www.youtube.com/watch?v=Wvr8LCSuFjE) and was inspired to find the perfect skin tone range and create this program

In order to find that range I took the initial colors from the video, and took samples of many [peoples' faces](http://vis-www.cs.umass.edu/lfw/alpha_all_30.html). With all of that data I started looking for patterns.

I initially used the [RGB](https://es.wikipedia.org/wiki/RGB) color model as it's commonly used to define colors, however, I found that switching to the [HSL](https://en.wikipedia.org/wiki/HSL_and_HSV) model revealed a pattern much faster. It turns out that common skin tones have a fairly specific hue, and their lightness/saturation follows a simple 2D curve.

Essentially when a skin tone is light, the saturation is low; and when the tone is darker, the saturation is much higher. The final lightness/saturation relationship is shown to users as a dotted curve in the UI. The optimum hue was found be at around 20° and is also shown to users in the hue slider.

### Code Implementation

{:.img-with-text}
![The perfect skin tone range displayed with the internal proximity map](/images/color_picker_proximity.jpg)<br>
The internal limits used to determine whether a color is close to the ideal range.

The program works by checking a color's proximity to the ideal skin tone range (the dotted curve displayed to users). A 'proximity bitmap' is used in code to measure whether a given color is close to the ideal range. The internally used bitmap is represented by the white shading in the above image.

The basic algorithm implemented in code is as follows:
- Create a UI which displays colors using the HSV color model. [This existing project](https://github.com/PyQt5/CustomWidgets) helped me out there.
- Check that the color is within the suitable hue range (~20°).
- Check that the color is close to the curve using the 'proximity bitmap'.
  - The 'proximity bitmap' is made by drawing with a thick translucent brush along the dotted line, followed by a thinner white brush.
  - The bitmap is simply sampled in the background as the user picks colors. The proximity is close, close-ish, or not close if the respective bitmap sample is white, translucent, or transparent.
  - Colors to the left and right of the curve represent low and high saturations which can also be conveyed to the user.

With the given proximity information of the color now known, the program can provide hints to the user to improve the skin tone color.

---

## Color Identifier

![Image of the UI](/images/color_picker_identifier.jpg){:.image-medium}<br>

### Sourcing Color Names

It turns out there are [many ways](https://en.wikipedia.org/wiki/Lists_of_colors) to name colors. As such it's likely that different users would want to name their colors differently too. A web developer, for instance, might be interested in [CSS color names](https://www.w3schools.com/colors/colors_groups.asp). A color-blind user on the other hand might prefer simpler [shading based names](https://en.wikipedia.org/wiki/List_of_colors_by_shade).

I decided to make the app color agnostic so that the user can use any color names they want. The app defaults to a [shading based](https://en.wikipedia.org/wiki/List_of_colors_by_shade) list of colors, but allows users to use external color name lists to overwrite the default names.

The following optional color name lists are shipped with the program:
- All [CSS](https://www.w3schools.com/colors/colors_groups.asp) color names - useful for web developers.
- The [xkcd](https://xkcd.com/color/rgb/) color name list.
- Common [Crayola](https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors) color names.
- User can of course make their own lists too.

### Finding The Closest Color In Code

The program initially loads the internal or an external color name list into memory. Once a color is sampled, this internal list is simply checked against for color closeness. The closest color name is then displayed to the user. There are [a number of ways](https://en.wikipedia.org/wiki/Color_difference) to measure the difference between two colors, but this app uses the [Euclidean](https://en.wikipedia.org/wiki/Color_difference#Euclidean) formula.