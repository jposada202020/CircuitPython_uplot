# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`shade`
================================================================================

CircuitPython shade utility for uPlot.

* Author(s): Jose D. Montoya


"""
try:
    from typing import Optional, Union
    from circuitpython_uplot.plot import Plot
except ImportError:
    pass
from ulab import numpy as np
from bitmaptools import fill_region


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"


class shade:
    """
    Class to draw shade between two lines
    """

    def __init__(
        self,
        plot: Plot,
        x: Union[list, np.linspace, np.ndarray],
        y1: list,
        y2: list,
        rangex: Optional[list] = None,
        rangey: Optional[list] = None,
        fill_color: int = 0xF6FF41,
        nudge: bool = True,
    ) -> None:
        """
        :param Plot plot: Plot object for the scatter to be drawn
        :param list|ulab.numpy.linspace|ulab.numpy.ndarray x: x points coordinates
        :param list y1: y1 points coordinates
        :param list y2: y2 points coordinates
        :param list|None rangex: x range limits
        :param list|None rangey: y range limits
        :param int fill_color: filling color. Defaults to 0xF6FF41
        :param bool nudge: moves the graph a little for better displaying

        """

        if nudge:
            nudge_factor = 1
        else:
            nudge_factor = 0

        plot._plot_palette[plot._index_colorused] = fill_color

        if rangex is None:
            xmin = np.min(x) - nudge_factor * (abs(np.max(x) - np.min(x)) / 10)
            xmax = np.max(x) + nudge_factor * (abs(np.max(x) - np.min(x)) / 10)
        else:
            xmin = min(rangex)
            xmax = max(rangex)

        if rangey is None:
            ymin = min(np.min(y1), np.min(y2)) - nudge_factor * (
                abs(np.max(y1) - np.min(y1)) / 10
            )
            ymax = max(np.max(y1), np.max(y2)) + nudge_factor * (
                abs(np.max(y1) - np.min(y1)) / 10
            )
        else:
            ymin = min(rangey)
            ymax = max(rangey)

        x = np.array(x)
        y1 = np.array(y1)
        y2 = np.array(y2)

        xnorm = np.array(
            plot.transform(xmin, xmax, plot._newxmin, plot._newxmax, x),
            dtype=np.int16,
        )
        y1norm = np.array(
            plot.transform(ymin, ymax, plot._newymin, plot._newymax, y1),
            dtype=np.int16,
        )
        y2norm = np.array(
            plot.transform(ymin, ymax, plot._newymin, plot._newymax, y2),
            dtype=np.int16,
        )

        fill_region(
            plot._plotbitmap,
            min(xnorm),
            min(y1norm),
            max(xnorm),
            max(y2norm),
            plot._index_colorused,
        )

        plot._index_colorused += 1
