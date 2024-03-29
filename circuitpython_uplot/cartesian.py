# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`cartesian`
================================================================================

CircuitPython cartesian graph

* Author(s): Jose D. Montoya


"""
try:
    from typing import Optional, Union
    from circuitpython_uplot.plot import Plot
except ImportError:
    pass
from bitmaptools import draw_line, fill_region
from ulab import numpy as np
from vectorio import Polygon

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"


class Cartesian:
    """
    Class to draw cartesian plane
    """

    def __init__(
        self,
        plot: Plot,
        x: Union[list, np.linspace, np.ndarray],
        y: Union[list, np.linspace, np.ndarray],
        rangex: Optional[list] = None,
        rangey: Optional[list] = None,
        line_color: Optional[int] = None,
        line_style: Optional[str] = None,
        ticksx: Union[np.array, list] = None,
        ticksy: Union[np.array, list] = None,
        fill: bool = False,
        nudge: bool = True,
        logging: bool = False,
    ) -> None:
        """

        :param Plot plot: Plot object for the scatter to be drawn
        :param list|ulab.numpy.linspace|ulab.numpy.ndarray x: x points coordinates
        :param list|ulab.numpy.linspace|ulab.numpy.ndarray y: y points coordinates
        :param list|None rangex: x range limits. Defaults to None
        :param list|None rangey: y range limits. Defaults to None
        :param int|None line_color: line color. Defaults to None
        :param str|None line_style: line style. Defaults to None
        :param np.array|list ticksx: X axis ticks values
        :param np.array|list ticksy: Y axis ticks values
        :param bool fill: Show the filling. Defaults to `False`
        :param bool nudge: moves the graph a little for better displaying. Defaults to `True`
        :param bool logging: used to change the logic of the cartesian to work as a logger

        """
        self.points = []
        self.ticksx = ticksx
        self.ticksy = ticksy

        if line_color is not None:
            plot._plot_palette[plot._index_colorused] = line_color

        if line_style is None:
            self._line_type = "-"
        else:
            self._line_type = line_style

        if self._line_type not in ["-", ".", "- -", "-.-"]:
            raise ValueError("line_style must be a valid option")

        if line_style is None:
            self._line_type = "-"

        if nudge:
            nudge_factor = 1
        else:
            nudge_factor = 0

        if rangex is None:
            self.xmin = np.min(x) - nudge_factor * (abs(np.max(x) - np.min(x)) / 10)
            self.xmax = np.max(x) + nudge_factor * (abs(np.max(x) - np.min(x)) / 10)

        else:
            self.xmin = min(rangex)
            self.xmax = max(rangex)

        if rangey is None:
            self.ymin = np.min(y) - nudge_factor * (abs(np.max(y) - np.min(y)) / 10)
            self.ymax = np.max(y) + nudge_factor * (abs(np.max(y) - np.min(y)) / 10)
        else:
            self.ymin = min(rangey)
            self.ymax = max(rangey)

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

        if fill:
            self.points.append((xnorm[0], plot._newymin))
            for index, item in enumerate(xnorm):
                self.points.append((item, ynorm[index]))
            self.points.append((xnorm[-1], plot._newymin))
            self.points.append((xnorm[0], plot._newymin))
            plot.append(
                Polygon(
                    pixel_shader=plot._plot_palette,
                    points=self.points,
                    x=0,
                    y=0,
                    color_index=plot._index_colorused,
                )
            )
        else:
            if logging:
                fill_region(
                    plot._plotbitmap,
                    plot._newxmin + plot._tickheightx + 1,
                    plot._newymax + 1,
                    plot._newxmax - 1,
                    plot._newymin - plot._tickheighty,
                    0,
                )

            for index, _ in enumerate(xnorm):
                if index + 1 >= len(xnorm):
                    break
                if y[index] >= self.ymax:
                    continue

                self._draw_plotline(plot, index, xnorm, ynorm)

        if plot._showticks:
            if plot._cartesianfirst:
                if logging:
                    x = np.linspace(self.xmin, self.xmax, 100)
                    y = np.linspace(self.ymin, self.ymax, 100)
                plot._draw_ticks(x, y, self.ticksx, self.ticksy)
                plot._cartesianfirst = False
                plot._showticks = False

        if logging:
            plot._index_colorused = plot._index_colorused
        else:
            plot._index_colorused = plot._index_colorused + 1

    def _draw_plotline(self, plot, index, xnorm, ynorm):
        if self._line_type == "-":
            self._plot_line(plot, index, xnorm, ynorm)
        elif self._line_type == "-.-":
            if index % 3 == 0:
                self._plot_line(plot, index, xnorm, ynorm)
            else:
                plot._plotbitmap[xnorm[index], ynorm[index]] = plot._index_colorused
        elif self._line_type == ".":
            plot._plotbitmap[xnorm[index], ynorm[index]] = plot._index_colorused
        elif self._line_type == "- -":
            if index % 2 == 0:
                self._plot_line(plot, index, xnorm, ynorm)

    @staticmethod
    def _plot_line(plot, index, xnorm, ynorm):
        draw_line(
            plot._plotbitmap,
            xnorm[index],
            ynorm[index],
            xnorm[index + 1],
            ynorm[index + 1],
            plot._index_colorused,
        )


class LineStyle:
    """
    Line style class
    """

    SOLID = "-"
    DASHED = "- -"
    DASH_DOT = "-.-"
    DOTTED = "."
