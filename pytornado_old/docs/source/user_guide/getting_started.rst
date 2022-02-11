.. _getting_started:

Getting started
===============

This page briefly explains how to get started with a very simple example using |name|'s command line interface. Notice that a more detailed user guide can be found here: :ref:`detailed_user_guide`

First, open a terminal and try to simply run the command ``pytornado`` (without any arguments). A short help page should show up. One of the available arguments is ``--make-example`` which we will use in this tutorial to create a minimal working example. Now, in your terminal run:

.. code::

    pytornado --make-example

This command creates a folder named `pytornado` in your current directory. Change into this folder (``cd pytornado``) and then run

.. code::

    pytornado -v --run settings/template.json

The flag ``-v`` tells |name| to go into *verbose* mode. You should see some text output on your terminal screen. We use ``--run`` to execute a VLM analysis. The argument is the path to |name|'s main settings file. If everything worked correctly, you should see a plot of a simple rectangular wing.

.. figure:: pytornado/example_plot.png
   :width: 500
   :alt: Template
   :align: center

   Pressure plot for a simple rectangular wing with deflected control surfaces

While creating this minimalistic example, several directories and files were created. Feel free to explore the different files. However, don't be worried if you don't understand everything yet. We will give more detailed instructions on the following pages.

Troubleshooting
---------------

Linux
~~~~~

* If you run ``pytornado`` and get a ``pytornado: command not found`` error, try to add ``~/.local/bin`` to your ``PATH`` variable:

.. code:: bash

    echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
    source ~/.bashrc

.. seealso::

    Learn more about the |name|'s command line interface:

    * :ref:`command_line_interface`

    Learn more about |name|'s input files:

    * :ref:`input_files`
