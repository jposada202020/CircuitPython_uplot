# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`ucartesian`
================================================================================

CircuitPython cartesian graph

* Author(s): Jose D. Montoya


"""
try:
    from typing import Optional, Union
    from circuitpython_uplot.uplot import Uplot
except ImportError:
    pass
from bitmaptools import draw_line, fill_region
from ulab import numpy as np
from vectorio import Polygon

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"


# pylint: disable=too-many-arguments, invalid-name, no-self-use, too-few-public-methods
# pylint: disable=too-many-locals, too-many-branches
class ucartesian:
    """
    Class to draw cartesian plane
    """

    def __init__(
        self,
        plot: Uplot,
        x: Union[list, np.linspace, np.ndarray],
        y: Union[list, np.linspace, np.ndarray],
        rangex: Optional[Union[list, None]] = None,
        rangey: Optional[Union[list, None]] = None,
        line_color: Optional[Union[int, None]] = None,
        fill: bool = False,
        nudge: bool = True,
        logging: bool = False,
    ) -> None:
        """

        :param Uplot plot: Plot object for the scatter to be drawn
        :param list|ulab.numpy.linspace|ulab.numpy.ndarray x: x points coordinates
        :param list|ulab.numpy.linspace|ulab.numpy.ndarray y: y points coordinates
        :param list|None rangex: x range limits. Defaults to None
        :param list|None rangey: y range limits. Defaults to None
        :param int|None line_color: line color. Defaults to None
        :param bool fill: Show the filling. Defaults to `False`
        :param bool nudge: moves the graph a little for better displaying. Defaults to `True`
        :param bool logging: used to change the logic of the cartesian to work as a logger

        """
        self.points = []

        if line_color is not None:
            plot._plot_palette[plot._index_colorused] = line_color

        if nudge:
            nudge_factor = 1
        else:
            nudge_factor = 0

        if rangex is None:
            xmin = np.min(x) - nudge_factor * (abs(np.max(x) - np.min(x)) / 10)
            xmax = np.max(x) + nudge_factor * (abs(np.max(x) - np.min(x)) / 10)
        else:
            xmin = min(rangex)
            xmax = max(rangex)

        if rangey is None:
            ymin = np.min(y) - nudge_factor * (abs(np.max(y) - np.min(y)) / 10)
            ymax = np.max(y) + nudge_factor * (abs(np.max(y) - np.min(y)) / 10)
        else:
            ymin = min(rangey)
            ymax = max(rangey)

        x = np.array(x)
        y = np.array(y)

        xnorm = np.array(
            plot.transform(xmin, xmax, plot._newxmin, plot._newxmax, x),
            dtype=np.int16,
        )
        ynorm = np.array(
            plot.transform(ymin, ymax, plot._newymin, plot._newymax, y),
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
                draw_line(
                    plot._plotbitmap,
                    xnorm[index],
                    ynorm[index],
                    xnorm[index + 1],
                    ynorm[index + 1],
                    plot._index_colorused,
                )
        if plot._showticks:
            if plot._cartesianfirst:
                if logging:
                    x = np.linspace(xmin, xmax, 100)
                    y = np.linspace(ymin, ymax, 100)
                plot._draw_ticks(x, y)
                plot._cartesianfirst = False
                plot._showticks = False

        if logging:
            plot._index_colorused = plot._index_colorused
        else:
            plot._index_colorused = plot._index_colorused + 1
