---
layout: post
title: Thesis Beam Analysis Tool - Theory
hidden: true
---

[Back to original article here]({% post_url 2014-01-01-thesis %}){:.big-link}

---

### Theory

The program uses well established 'concrete section analysis' principals to function. The basic theory is as follows:
- When a beam is under load, the top of the beam will compress, and the bottom will stretch. The resulting shortening/expansion in the beam is called a 'strain profile' and is assumed to be linear.
- Somewhere inside the beam it will neither compress nor stretch. This is called the 'neutral depth' ('dn' in the image).
- All materials have a stress/strain relationship. Given the size of the material and this relationship, we can calculate the force within a material for a given strain value.
- If we guess a neutral depth, we can create the strain profile. With the given strain profile, we can calculate all of the forces within the beam.
- A beam can only exist when all compression forces equal all tension forces - i.e. the sum of forces equals zero. Once we find a strain profile where this is true, we have 'solved' the beam.

![Concrete section analysis diagram](/images/thesis_algorithm.png){:.image-small}

### Algorithm

The algorithm to 'solve' a beam is therefore:
- Guess a neutral depth within the beam.
- Calculate all forces in the beam.
- Iterate on the solution until we find a neutral depth where all forces equal zero.

The program simply runs this process for varying loads in order to calculate results such as failure modes, ultimate strength capacity, deflection, etc.

In order to deal with real world data, the program makes use of the stated `Python` libraries to interpret inputted graphs.
- The program uses a non-linear solver to guess, iterate, and finally solve for the neutral depth. Custom stress/strain material properties are usually non-linear themselves.
- Numerical integration was used to calculate areas under graphs.
- Linear interpolation was used to find stresses/strains from custom curves when evaluating material forces.

---

[Back to original article here]({% post_url 2014-01-01-thesis %}){:.big-link}
