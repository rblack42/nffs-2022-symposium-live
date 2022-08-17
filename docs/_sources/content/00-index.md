# Predicting Indoor Model Flight Time Using Python

**Author: [Roie Black](https://rblack42.github.io/math-magik)**

Welcome to the live version of this article, to be published in the 2022 edition of the *National Free Flight Society* Symposium. If you found your way here after reading that publication, you will be able to see a more detailed version of the article here, complete with all the code used to generate the results. If you are really up for an adventure, you can run all of the code presented in the article by launching your own copy of the project on *Binder*,  a public cloud server that will fire up a new *virtual machine* for you, install *Python* and the code for this project, and let you play with it, all without installing anything on your machine.

This article is part of the [Math Magik](https://rblack42.github.io/math-magik) project. I started this project in 2020 as part of my plan to build a Python application to assist model builders in designing and flying indoor model airplanes. The initial effort, published in the 2021 issue of the NFFS Symposium {cite}`black2021` focused on using *OpenSCAD* and some supporting *Python* code to design a model and analyze the proposed design to calculate weight and balance data.

The *Python* code presented here extends that project by adding code that can help predict the flying time for an indoor model using data extracted from the *OpenSCAD* design, or entered manually for other designs. It is based on work published by Doug McLean in the 1976 edition of the NFFS Symposium {cite}`mclean1976`, and Walter Erbach' in the 1990 edition of the Symposium {cite}`erbach1990`. All equations and code shown here has been developed using *Python SymPy* so you can reproduce the exactly what is shown by running this live code yourself!

At present, this is a work in progress. I invite all interested readers to contact me for help, or to offer suggestions on how I can improve this project. My goal is to provide information and tools helpful to builders of all ages (well, maybe those who are at least into some math studies, which usually happens in high school!) I am trying to keep the math approachable by all readers, but this is tough to do since much of aeronautical engineering depends on advanced math concepts.

The original document you are reading was developed using a tool very popular in the Data Science world: *Jupyter*. This is a web based tool that you can install on your personal computer. This program lets you create *notebooks* where you document your research work, complete with nice figures, math, and code that you actually run as you work through a development. You cannot easily create a conventional program with *Jupyter*, but you can write parts of a program that can be copied to a more normal development environment for proper testing and deployment. The program developed in this article is available from my *GitHub* repository {cite}`mmtime`.

A really neat benefit of working with *Jupyter* is the existence of free services that let anyone with a web browser experience the research environment I used on my personal laptop. Basically, these free services create a "virtual" computer and then install everything you need on that virtual computer to run a *Jupyter* web server you can interact with using just your normal web browser. The latest copy of my code gets loaded into this machine from its home on *GitHub*, and you can experiment with it as you like. You are working on a copy of my code, so you cannot hurt anything. When you close your browser, the virtual machine is destroyed and all changes you made will be lost.  I am using the Binder service for this. The project is available at https://mybinder.org/v2/gh/rblack42/nffs-2022-symposium-live/HEAD. A brief overview of using this system is in the appendix.


- Roie R. Black
    - BS, MS, Aerospace Engineering, Virginia Tech
    - MS, Computer Science, Texas State
    - Major, USAF (retired)
    - Professor, Computer Science, Austin Community College (retired)
    - AMA 18079

```python

```
