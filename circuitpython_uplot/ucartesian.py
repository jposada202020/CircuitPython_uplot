# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`ucartesian`
================================================================================

CircuitPython cartesian graph

* Author(s): Jose D. Montoya


"""

from bitmaptools import draw_line
from ulab import numpy as np
from vectorio import Polygon


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"

# pylint: disable=too-many-arguments, invalid-name, no-self-use, too-few-public-methods
# pylint: disable=too-many-locals
class ucartesian:
    """
    Class to draw cartesian plane
    """

    def __init__(
        self,
        plot,
        x: any,
        y: any,
        rangex: list = None,
        rangey: list = None,
        line_color: int = 0xFFFFFF,
        fill: bool = False,
        nudge: bool = True,
    ) -> None:
        """

        :param plot: Plot object for the scatter to be drawn
        :param x: x points coordinates
        :param y: y points coordinates

        """
        points = []
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
            dtype=np.uint16,
        )
        ynorm = np.array(
            plot.transform(ymin, ymax, plot._newymin, plot._newymax, y),
            dtype=np.uint16,
        )

        if fill:
            points.append((xnorm[0], plot._newymin))
            for index, item in enumerate(xnorm):
                points.append((item, ynorm[index]))
            points.append((xnorm[-1], plot._newymin))
            points.append((xnorm[0], plot._newymin))
            plot.append(
                Polygon(
                    pixel_shader=plot._plot_palette,
                    points=points,
                    x=0,
                    y=0,
                    color_index=plot._index_colorused,
                )
            )
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
            plot._draw_ticks(x, y)

        plot._index_colorused = plot._index_colorused + 1
