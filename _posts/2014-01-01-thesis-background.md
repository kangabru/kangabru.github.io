---
layout: post
title: Thesis Beam Analysis Tool - Background
hidden: true
---

[Back to original article here]({% post_url 2014-01-01-thesis %}){:.big-link}

---

### Background

This is a tool built as part of my undergraduate thesis at the [University of Queensland](https://www.uq.edu.au/). The thesis focused on the analysis and strengthening of concrete beams - specifically beams from ageing bridges in rural Queensland, Australia.

The goal was to use [fibre reinforced polymer (FRP)](https://en.wikipedia.org/wiki/Fibre-reinforced_plastic) laminates to improve beam strength of the bridges to save them from being destroyed. Think of gluing carbon fibre sheets to the underside of the concrete beams of bridges.

If aging beams could be successfully strengthened with FRP, we could add decades to their life expectancy and save tax payers $$$ in repairs.

Would they work though? That was my job to find out.

---

### Thesis

The original thesis had 2 parts - an experimental side, and an analysis side. The experimental side consisted of testing 2 beams. One beam without strengthening, and one strengthened with FRP laminates. The goal was to see if FRP laminates would significantly increase the beam strength.

The goal of the analysis side was to develop a model through which we could predict the strength increase of FRP. The idea was to use [finite element modelling (FEM)](https://en.wikipedia.org/wiki/Finite_element_method) to do this.

The design program came to light because we needed to verify our FEM results before conducting the experiments. Furthermore, _FEM takes ages!_ Our initial models took up to 2 days to finish. Not the best turnaround time when you're debugging the model.

<blockquote>
Hey, wouldn't it be good if it didn't take 2 days to do this?<br>
Yes.
</blockquote>

Spreadsheets only do so much and we had some cool ideas that we wanted to implement. So we started work on the program. It used established concrete section analysis methods and is something you often did manually. The program obviously made it _much_ easier. Our initial results were promising so our professor encouraged us to continue.

The main 'cool' feature we wanted to implement was adding the ability to input custom stress/strain data. We had taken samples of the concrete and steel from our beams which we wanted to utilise. Our relatively simple model (compared to FEM) was suddenly just as accurate, yet ran in seconds. Our professor then incorporated the program as an official part to our thesis.

{:.img-with-text}
![Image of Program vs Beams Plot](/images/thesis_plot.png){:.image-small}
Our program vs the real world performance of the beams.

From the graph you can see two things:
- FRP _significantly_ improved the strength capacity of the beam - by almost 50%!
- The program is accurate. When it isn't quite accurate, it is usually conservative (Beam #1).

As noted in our thesis, the fewer assumptions you make, the more accurate the results will be. Our model did not account for more subtle effects like bond slip, prestress loss, non-linear strain profile in the cross section.

Overall the results of the thesis were a success. We developed 2 analytical models - FEM and the this design program - and demonstrated that FRP can significantly improve strength in ageing concrete beams. [Further experiments](https://www.uq.edu.au/news/article/2018/05/uq-bridge-world-beater) have [also been successful](https://www.sciencedirect.com/science/article/pii/S0141029616311488).

---

[Back to original article here]({% post_url 2014-01-01-thesis %}){:.big-link}
