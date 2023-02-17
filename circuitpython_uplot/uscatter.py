# SPDX-FileCopyrightText: 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT


"""

`uscatter`
================================================================================

CircuitPython scatter graph

* Author(s): Jose D. Montoya


"""
from ulab import numpy as np
import displayio
from vectorio import Circle

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"

# pylint: disable=too-few-public-methods, invalid-name, duplicate-code, too-many-locals, too-many-arguments
class uscatter:
    """
    Main class to display different graphics
    """

    def __init__(
        self,
        plot,
        x: any,
        y: any,
        rangex: any = None,
        rangey: any = None,
        radius: int = 3,
        circle_color=0xFF905D,
    ) -> None:
        """

        :param plot: Plot object for the scatter to be drawn
        :param x: x points coordinates
        :param y: y points coordinates
        :param int radius: circle radius

        """

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

        palette = displayio.Palette(1)
        palette[0] = circle_color
        for i, _ in enumerate(x):
            plot.append(
                Circle(pixel_shader=palette, radius=radius, x=xnorm[i], y=ynorm[i])
            )

        if plot._showticks:
            plot._draw_ticks(x, y)
