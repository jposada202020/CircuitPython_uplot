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

# pylint: disable=too-many-arguments, invalid-name, no-self-use
class ucartesian:
    """
    Class to draw cartesian plane
    """

    def __init__(self, plot, x: any, y: any) -> None:
        """

        :param plot: Plot object for the scatter to be drawn
        :param x: x points coordinates
        :param y: y points coordinates

        """

        x = np.array(x)
        y = np.array(y)

        xnorm = np.array(
            plot.normalize(np.min(x), np.max(x), plot._newxmin, plot._newxmax, x),
            dtype=np.uint16,
        )
        ynorm = np.array(
            plot.normalize(np.min(y), np.max(y), plot._newymin, plot._newymax, y),
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
                1,
            )
        if plot._showticks:
            plot._draw_ticks(x, y)
