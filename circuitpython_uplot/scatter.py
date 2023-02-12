# SPDX-FileCopyrightText: 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT


"""

`scatter`
================================================================================

CircuitPython scatter graph

* Author(s): Jose D. Montoya


"""
from ulab import numpy as np
import displayio
from vectorio import Circle

# pylint: disable=too-few-public-methods, invalid-name
class scatter:
    """
    Main class to display different graphics
    """

    def __init__(self, plot, x, y, radius=3):
        """

        :param plot: Plot Object for the scatter to be drawn
        :param x: x points coordinates
        :param y: y points coordinates
        :param radius: circle radius

        """
        plot._drawbox()

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

        palette = displayio.Palette(1)
        palette[0] = 0xFFFFFF
        for i, _ in enumerate(x):
            plot.append(
                Circle(pixel_shader=palette, radius=radius, x=xnorm[i], y=ynorm[i])
            )

        if plot._showticks:
            plot._draw_ticks(x, y)
