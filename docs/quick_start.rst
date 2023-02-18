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


===============
Cartesian
===============
With the cartesian class it's possible to add (x,y) plots. You can add different (x,y) plots to the
same plot area. After you create your plot area you will need to define the xy plane
for the plot. Secondly, you will need to give some ``x`` and ``y`` data.
This data will be converted to a ulab.numpy.ndarray. For more information please refer
to the ulab library

.. py:function:: ucartesian(plot, x, y, rangex, rangey, line_color, fill, nudge,)

   :param ~uplot.Uplot plot: uplot.Uplot object
   :param `~ulab.numpy.linspace` x: x data
   :param ~ulab.numpy.linspace y: y data
   :param rangex: x data range
   :type rangex: list or None
   :param rangey: y data range
   :type rangey: list or None
   :param int line_color: color line
   :param int nudge:  graph displacement from the origin


.. code-block:: python

    from ulab import numpy as np
    from circuitpython_uplot.uplot import Uplot
    from circuitpython_uplot.ucartesian import ucartesian
    display = board.DISPLAY
    plot = Uplot(0, 0, display.width, display.height)

    x = np.linspace(-4, 4, num=25)
    constant = 1.0 / np.sqrt(2 * np.pi)
    y = constant * np.exp((-(x**2)) / 2.0)

After the initial setup we add our xy plane and show our plot

.. code-block:: python

    ucartesian(plot, x, y)
    display.show(plot)





There are some parameters that you coan customize:

    * rangex and rangey: you could specify the ranges of your graph. Allowing you to move your graph according to your needs. This parameters only accept lists
    * line color: you could specify the color in HEX
    * fill: if you selected this as `True` the area under your graph will be filled
    * nudge: this parameter allows yuo to move a little bit the graph. This is useful when the data start/end in the limits of your range

With the following code, we are setting up the x axis to [-5, 5]
the y axis to [0, 1], line color to Green (0x00FF00) and no filling


.. code-block:: python

    x = np.linspace(-3, 3, num=50)
    constant = 2.0 / np.sqrt(2 * np.pi)
    y = constant * np.exp((-(x**2)) / 2.0)
    ucartesian(plot, x, y, rangex=[-5, 5], rangey=[0, 1], line_color=0x00FF00)


if you want to add more than un line to your plot, you could do something like this:

.. code-block:: python

    plot = Uplot(0, 0, display.width, display.height)
    x = np.linspace(-4, 4, num=25)
    y1 = x**2 / 2
    y2 = 2 + x**2 + 3 * x
    ucartesian(plot, x, y1)
    ucartesian(plot, x, y1)
    display.show(plot)
