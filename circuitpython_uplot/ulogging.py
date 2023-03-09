# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`ulogging`
================================================================================

CircuitPython logging data graph

* Author(s): Jose D. Montoya


"""
try:
    from typing import Union
    from circuitpython_uplot.uplot import Uplot
except ImportError:
    pass
from bitmaptools import draw_line, fill_region
from ulab import numpy as np

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"


# pylint: disable=too-many-arguments, invalid-name, no-self-use, too-few-public-methods
# pylint: disable=too-many-locals, too-many-branches, protected-access
class ulogging:
    """
    Class to log data
    """

    def __init__(
        self,
        plot: Uplot,
        x: Union[list, np.linspace, np.ndarray],
        y: Union[list, np.linspace, np.ndarray],
        rangex: list,
        rangey: list,
        line_color: int = 0xFFFFFF,
        ticksx: np.array = np.array([0, 10, 30, 50, 70, 90]),
        ticksy: np.array = np.array([0, 10, 30, 50, 70, 90]),
    ) -> None:
        """

        :param Uplot plot: Plot object for the log to be drawn
        :param list|ulab.numpy.linspace|ulab.numpy.ndarray x: x points coordinates
        :param list|ulab.numpy.linspace|ulab.numpy.ndarray y: y points coordinates
        :param list|None rangex: x range limits. Defaults to None
        :param list|None rangey: y range limits. Defaults to None
        :param int|None line_color: line color. Defaults to None

        """
        self.points = []
        self.ticksx = np.array(ticksx)
        self.ticksy = np.array(ticksy)

        plot._plot_palette[plot._index_colorused] = line_color

        self.xmin = rangex[0]
        self.xmax = rangex[1]
        self.ymin = rangey[0]
        self.ymax = rangey[1]

        x = np.array(x)
        y = np.array(y)

        xnorm = np.array(
            plot.transform(self.xmin, self.xmax, plot._newxmin, plot._newxmax, x),
            dtype=np.int16,
        )
        ynorm = np.array(
            plot.transform(self.ymin, self.ymax, plot._newymin, plot._newymax, y),
            dtype=np.int16,
        )

        fill_region(
            plot._plotbitmap,
            plot._newxmin + plot._tickheightx + 1,
            plot._newymax + 1,
            plot._newxmax - 1,
            plot._newymin - plot._tickheighty,
            0,
        )

        if len(x) == 1:
            plot._plotbitmap[xnorm[0], ynorm[0]] = 1
        else:
            for index, _ in enumerate(xnorm):
                if index + 1 >= len(xnorm):
                    break
                draw_line(
                    plot._plotbitmap,
                    xnorm[index],
                    ynorm[index],
                    xnorm[index + 1],
                    ynorm[index + 1],
                    plot._index_colorused,
                )
        if plot._showticks:
            if plot._loggingfirst:
                self._draw_ticks(plot)
                plot._loggingfirst = False
                plot._showticks = False

    def _draw_ticks(self, plot) -> None:
        """
        Draw ticks in the plot area

        """

        ticksxnorm = np.array(
            plot.transform(
                self.xmin, self.xmax, plot._newxmin, plot._newxmax, self.ticksx
            ),
            dtype=np.int16,
        )
        ticksynorm = np.array(
            plot.transform(
                self.ymin, self.ymax, plot._newymin, plot._newymax, self.ticksy
            ),
            dtype=np.int16,
        )

        for i, tick in enumerate(ticksxnorm):
            draw_line(
                plot._plotbitmap,
                tick,
                plot._newymin,
                tick,
                plot._newymin - plot._tickheightx,
                2,
            )
            if plot._showtext:
                plot.show_text(
                    "{:.2f}".format(ticksxnorm[i]), tick, plot._newymin, (0.5, 0.0)
                )
        for i, tick in enumerate(ticksynorm):
            draw_line(
                plot._plotbitmap,
                plot._newxmin,
                tick,
                plot._newxmin + plot._tickheighty,
                tick,
                2,
            )
            if plot._showtext:
                plot.show_text(
                    "{:.2f}".format(ticksynorm[i]), plot._newxmin, tick, (1.0, 0.5)
                )
