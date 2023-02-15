# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`ucartesian`
================================================================================

CircuitPython pie graph

* Author(s): Jose D. Montoya


"""

from bitmaptools import draw_line
from ulab import numpy as np


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"

# pylint: disable=too-many-arguments, invalid-name, no-self-use, too-few-public-methods
class ucartesian:
    """
    Class to draw cartesian plane
    """

    def __init__(
        self,
        plot,
        x: any,
        y: any,
        rangex: any = None,
        rangey: any = None,
        line_color: int = 0xFFFFFF,
    ) -> None:
        """

        :param plot: Plot object for the scatter to be drawn
        :param x: x points coordinates
        :param y: y points coordinates

        """

        plot._plot_palette[plot._index_colorused] = line_color

        if rangex is None:
            xmin = np.min(x)
            xmax = np.max(x)
        else:
            xmin = min(rangex)
            xmax = max(rangex)

        if rangey is None:
            ymin = np.min(y)
            ymax = np.max(y)
        else:
            ymin = min(rangey)
            ymax = max(rangey)

        x = np.array(x)
        y = np.array(y)

        xnorm = np.array(
            plot.normalize(xmin, xmax, plot._newxmin, plot._newxmax, x),
            dtype=np.uint16,
        )
        ynorm = np.array(
            plot.normalize(ymin, ymax, plot._newymin, plot._newymax, y),
            dtype=np.uint16,
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
            plot._draw_ticks(x, y)

        plot._index_colorused = plot._index_colorused + 1
