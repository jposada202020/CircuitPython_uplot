# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`polar`
================================================================================

CircuitPython Polar graph

* Author(s): Jose D. Montoya


"""
try:
    from typing import Optional, Union
    from circuitpython_uplot.plot import Plot
except ImportError:
    pass
from bitmaptools import draw_line, draw_circle
from ulab import numpy as np

__version__ = "0.11.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"


# pylint: disable=dangerous-default-value
class Polar:
    """
    Class to draw polar plots
    """

    def __init__(
        self,
        plot: Plot,
        radius: Union[list, np.linspace, np.ndarray],
        theta: Union[list, np.linspace, np.ndarray],
        rangex: Optional[list] = None,
        rangey: Optional[list] = None,
        line_color: Optional[int] = None,
        polar_plot_line_color: int = 0x647182,
        nudge: bool = True,
        radius_ticks: list = [1.0, 2.0],
    ) -> None:
        """

        :param Plot plot: Plot object for the scatter to be drawn
        :param list|ulab.numpy.linspace|ulab.numpy.ndarray radius: radius points
        :param list|ulab.numpy.linspace|ulab.numpy.ndarray theta: theta points
        :param list|None rangex: x range limits. Defaults to None
        :param list|None rangey: y range limits. Defaults to None
        :param int|None line_color: line color. Defaults to None
        :param bool fill: Show the filling. Defaults to `False`
        :param bool nudge: moves the graph a little for better displaying. Defaults to `True`

        """

        angles_list = [45, 90, 135, 180, 225, 270, 315, 360]
        angles = np.ndarray(angles_list, dtype=np.int16)

        self.angle_radians = np.radians(angles)
        self._color_index = plot._index_colorused + 1

        if line_color is not None:
            plot._plot_palette[plot._index_colorused] = line_color

        plot._plot_palette[self._color_index] = polar_plot_line_color

        if nudge:
            nudge_factor = 1
        else:
            nudge_factor = 0

        if rangex is None:
            xmin = np.min(radius) - nudge_factor * (
                abs(np.max(radius) - np.min(radius)) / 10
            )
            xmax = np.max(radius) + nudge_factor * (
                abs(np.max(radius) - np.min(radius)) / 10
            )
        else:
            xmin = min(rangex)
            xmax = max(rangex)

        if rangey is None:
            ymin = np.min(theta) - nudge_factor * (
                abs(np.max(theta) - np.min(theta)) / 10
            )
            ymax = np.max(theta) + nudge_factor * (
                abs(np.max(theta) - np.min(theta)) / 10
            )
        else:
            ymin = min(rangey)
            ymax = max(rangey)

        xnorm = np.array(
            plot.transform(
                xmin,
                xmax,
                plot._newxmin,
                plot._newxmax,
                np.cos(np.array(radius)) * np.array(theta),
            ),
            dtype=np.int16,
        )
        ynorm = np.array(
            plot.transform(
                ymin,
                ymax,
                plot._newymin,
                plot._newymax,
                np.sin(np.array(radius)) * np.array(theta),
            ),
            dtype=np.int16,
        )

        rnorm = np.array(
            plot.transform(
                0, xmax, plot._newxmin, plot._newxmax, np.array(radius_ticks)
            ),
            dtype=np.int16,
        )

        self.originx = int(plot.transform(xmin, xmax, plot._newxmin, plot._newxmax, 0))
        self.originy = int(plot.transform(ymin, ymax, plot._newymin, plot._newymax, 0))

        for index, _ in enumerate(xnorm):
            if index + 1 >= len(xnorm):
                break
            if theta[index] >= ymax:
                continue
            draw_line(
                plot._plotbitmap,
                xnorm[index],
                ynorm[index],
                xnorm[index + 1],
                ynorm[index + 1],
                plot._index_colorused,
            )
        for radius_norm in rnorm:
            draw_circle(
                plot._plotbitmap,
                self.originx,
                self.originy,
                radius_norm // 2,
                self._color_index,
            )

        for element in self.angle_radians:
            x = self.originx + int(np.cos(element) * rnorm[-1] // 2)
            y = self.originy + int(np.sin(element) * rnorm[-1] // 2)

            draw_line(
                plot._plotbitmap, self.originx, self.originy, x, y, self._color_index
            )
