A small tour for uplot.

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


.. image:: https://github.com/jposada202020/CircuitPython_uplot/blob/main/docs/readme.png


Good Luck!
