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
        ticksx: Union[np.array, list] = np.array([0, 10, 30, 50, 70, 90]),
        ticksy: Union[np.array, list] = np.array([0, 10, 30, 50, 70, 90]),
        tick_pos: bool = False,
        fill: bool = False,
    ) -> None:
        """

        :param Uplot plot: Plot object for the log to be drawn
        :param list|ulab.numpy.linspace|ulab.numpy.ndarray x: x points coordinates
        :param list|ulab.numpy.linspace|ulab.numpy.ndarray y: y points coordinates
        :param list|None rangex: x range limits. Defaults to None
        :param list|None rangey: y range limits. Defaults to None
        :param int|None line_color: line color. Defaults to None
        :param np.array|list ticksx: X axis ticks values
        :param np.array|list ticksy: Y axis ticks values
        :param bool tick_pos: indicates ticks position. True for below the axes.
         Defaults to ``False``
        :param bool fill: enable the filling of the plot. Defaults to ``False``

        """
        self.points = []
        self.ticksx = np.array(ticksx)
        self.ticksy = np.array(ticksy)
        if tick_pos:
            self._tickposx = plot._tickheightx
            self._tickposy = plot._tickheighty
        else:
            self._tickposx = 0
            self._tickposy = 0

        plot._plot_palette[plot._index_colorused] = line_color

        self.xmin = rangex[0]
        self.xmax = rangex[1]
        self.ymin = rangey[0]
        self.ymax = rangey[1]

        self.draw_points(plot, x, y, fill)

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
                plot._newymin + self._tickposx,
                tick,
                plot._newymin - plot._tickheightx + self._tickposx,
                2,
            )
            if plot._showtext:
                plot.show_text(
                    "{:.2f}".format(ticksxnorm[i]), tick, plot._newymin, (0.5, 0.0)
                )
        for i, tick in enumerate(ticksynorm):
            draw_line(
                plot._plotbitmap,
                plot._newxmin - self._tickposy,
                tick,
                plot._newxmin + plot._tickheighty - self._tickposy,
                tick,
                2,
            )
            if plot._showtext:
                plot.show_text(
                    "{:.2f}".format(ticksynorm[i]), plot._newxmin, tick, (1.0, 0.5)
                )

    @staticmethod
    def clear_plot(plot) -> None:
        """
        Clears the plot area
        """

        fill_region(
            plot._plotbitmap,
            plot._newxmin + plot._tickheightx + 1,
            plot._newymax + 1,
            plot._newxmax - 1,
            plot._newymin - plot._tickheighty,
            0,
        )

    def draw_points(self, plot: Uplot, x: list, y: list, fill: bool = False) -> None:
        """
        Draws points in the plot
        :param Uplot plot: plot object provided
        :param list x: list of x values
        :param list y: list of y values
        :param bool fill: parameter to fill the plot graphic. Defaults to False
        :return: None
        """
        self.clear_plot(plot)

        self.draw_new_lines(plot, x, y, fill)

    def draw_new_lines(self, plot: Uplot, x: list, y: list, fill: bool = False) -> None:
        """
        Draw the plot lines
        :param Uplot plot: plot object provided
        :param list x: list of x values
        :param list y: list of y values
        :param bool fill: parameter to fill the plot graphic. Defaults to False
        :return: None
        """
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
            if fill:
                for index, _ in enumerate(xnorm):
                    draw_line(
                        plot._plotbitmap,
                        xnorm[index],
                        ynorm[index],
                        xnorm[index],
                        plot._newymin,
                        plot._index_colorused,
                    )
