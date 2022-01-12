# Predicting Indoor Model Flight Time Using Python

Welcome to the live version of this article, scheduled to be published in the
2022 edition of the NFFS Symposium. If you found your way here after reading
that publication, you will be able to see a more detailed version of the
article here, complete with all the code used to generate the results. If you
are really up for an adventure, you can run the code used to generate the
article by launching your own copy on *Binder*,  a public cloud server that
will fire up a new *virtual machine* for you, install *Python* and the code for
this project, and let you play with it, all without installing anything on your
machine. See the *About this Document* page for more information.

This article is part of the [Math Magik](https://rblack42.github.io/math-magik)
project. I started this project in 2020 as part of my plan to build a Python
application to assist model builders in designing and flying indoor model
airplanes. The initial effort, published in the 2021 issue of the NFFS
Symposium {cite}`rblack21` focused on using *OpenSCAD* and some supporting
*Python* code to design a model and analyze the proposed design to calculate
weight and balance data.

The *Python* code presented here extends that project by adding code that can
help predict the flying time for an indoor model using data extracted from the
*OpenSCAD* design, or entered manually for other designs. It is based on works
published by Doug McLean in the 1976 edition of the NFFS Symposium
{cite}`mclean`, and Walter Erbach' in the 1990 edition of the Symposium
{cite}`erbach90`. All equations and code shown here has been developed using
*Python SymPy* so you can reproduce the exactly what is shown by running this
live code yourself!

At present, this is a work in progress. I invite all interested readers to
contact me for help, or to offer suggestions on how I can improve this project.
My goal is to provide information and tools helpful to builders of all ages
(well, maybe those who are at least into some math studies, which usually
happens in high school!) I am trying to keep the math approachable by all
readers, but this is tough to do since much of aeronautical engineering depends
on advanced math concepts. All math presented has been verified using a neat
Python tool called *SymPy*. With a little setup work, you should be able to
recreate all of the examples presented here on your own personal computer.

- Roie R. Black
    - BS, MS, Aerospace Engineering, Virginia Tech
    - MS, Computer Science, Texas State
    - Major, USAF (retired)
    - Professor, Computer Science, Austin Community College (retired)
    - AMA 18079
