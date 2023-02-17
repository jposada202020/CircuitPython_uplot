# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`ufillbetween`
================================================================================

CircuitPython fillbetween graph

* Author(s): Jose D. Montoya


"""

from ulab import numpy as np
from vectorio import Polygon


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"

# pylint: disable=too-many-arguments, invalid-name, no-self-use, too-few-public-methods
# pylint: disable=too-many-locals
class ufillbetween:
    """
    Class to draw a fillbetween graph
    """

    def __init__(
        self,
        plot,
        x: any,
        y1: any,
        y2: any,
        rangex: any = None,
        rangey: any = None,
        fill_color: int = 0xF6FF41,
    ) -> None:
        """
        :param plot: Plot object for the scatter to be drawn
        :param x: x points coordinates
        :param y1: y1 points coordinates
        :param y2: y2 points coordinates
        :param rangex: range of the X axis
        :param rangey: range of the Y axis
        :param fill_color int: filling color. Defaults to 0xF6FF41

        """
        points = []
        plot._plot_palette[plot._index_colorused] = fill_color

        if rangex is None:
            xmin = np.min(x)
            xmax = np.max(x)
        else:
            xmin = min(rangex)
            xmax = max(rangex)

        if rangey is None:
            ymin = min(np.min(y1), np.min(y2))
            ymax = max(np.max(y1), np.max(y2))
        else:
            ymin = min(rangey)
            ymax = max(rangey)

        x = np.array(x)
        y1 = np.array(y1)
        y2 = np.array(y2)

        xnorm = np.array(
            plot.normalize(xmin, xmax, plot._newxmin, plot._newxmax, x),
            dtype=np.uint16,
        )
        y1norm = np.array(
            plot.normalize(ymin, ymax, plot._newymin, plot._newymax, y1),
            dtype=np.uint16,
        )
        y2norm = np.array(
            plot.normalize(ymin, ymax, plot._newymin, plot._newymax, y2),
            dtype=np.uint16,
        )
        flip2y = np.flip(y2norm)

        for index, item in enumerate(xnorm):
            points.append((item, y1norm[index]))
        for index, item in enumerate(np.flip(xnorm)):
            points.append((item, flip2y[index]))

        points.append((xnorm[0], y2norm[0]))
        plot.append(
            Polygon(
                pixel_shader=plot._plot_palette,
                points=points,
                x=0,
                y=0,
                color_index=plot._index_colorused,
            )
        )
