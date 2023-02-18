A small tour for uplot.


Plot Usage
=============
We start importing some fundamental libraries for uplot to operate

.. code-block:: python

    import board
    import displayio
    from circuitpython_uplot.uplot import Uplot

For reference, screen in CircuitPython are defined from left to right and up to bottom. This means
that our (x=0, y=0) will be in the left upper corner of the screen.
For boards or feather with a integrated screen the following statement will initiate the scree

.. code-block:: python

    display = board.DISPLAY

For other displays please consult the right support library

We add the plot area. in this case we are selecting the whole screen as our plot area

.. code-block:: python

    plot = Uplot(0, 0, display.width, display.height)

The Uplot will be used to display our graphics. The position and the size of the plot area
could vary. This allows us to have more than 1 plot at the same time in the screen.
Every one of them with different characteristics or graphs.

We tell the microcontroller to display our plot:

.. code-block:: python

    display.show(plot)

And that is it you know have a plot area to add amazing graphs!


.. image:: ../docs/readme.png

Good Luck!

Graphics
===========

At the moment the following objects can be added to the plot area:

* Elements in the library
    * Cartesian Plane
    * Ufillbetween graph
    * Stackplot
    * Bar graph
    * Pie Chart
* Display_shapes library objects
* Histograms from the uhistogram library
* Boxplots from the uboxplot library
* Individual Vectorio Objects

In a more advanced method it is possible to add directly to the plot area using the plot bitmap object

The following code shows an example adding a shape from the Adafruit_Display_shapes
library

.. code-block:: python

    import board
    from adafruit_display_shapes.polygon import Polygon
    from adafruit_display_shapes.roundrect import RoundRect
    from circuitpython_uplot.uplot import Uplot

    display = board.DISPLAY
    plot = Uplot(0, 0, display.width, display.height)
    roundrect = RoundRect(30, 30, 61, 81, 10, fill=0x0, outline=0xFF00FF, stroke=6)
    plot.append(roundrect)
    display.show(plot)



Ticks and Grid
===============
Plot axes are shown by default. To change this behaviour you would need
to use the correct keyword in the axsparams function:

Options available are:
    * box : draws a box
    * cartesian: draws the left and bottom axes
    * line: draws the bottom axis

The following snippet shows how to create a cartesian plot

.. code-block:: python

    plot = Uplot(0, 0, display.width, display.height)
    plot.axs_params(axstype="cartesian")

Tick spacing and numbers are selected by default. However it's possible to customize
the following parameters:

    * tickheight
    * tickcolor

.. code-block:: python

    plot.tick_params(tickheight=12, tickcolor=0xFF0008)


Gridlines are normally off. If you want visible gridlines then use:

.. code-block:: python

    plot.tick_params(tickgrid=True)
