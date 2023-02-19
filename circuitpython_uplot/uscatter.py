# SPDX-FileCopyrightText: 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT


"""

`uscatter`
================================================================================

CircuitPython scatter graph

* Author(s): Jose D. Montoya


"""
try:
    from typing import Optional, Union
    from circuitpython_uplot.uplot import Uplot
except ImportError:
    pass


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
        plot: Uplot,
        x: Union[list, np.linspace, np.ndarray],
        y: Union[list, np.linspace, np.ndarray],
        rangex: Optional[Union[list, None]] = None,
        rangey: Optional[Union[list, None]] = None,
        radius: Optional[Union[list, int]] = 3,
        circle_color: int = 0xFF905D,
        nudge: bool = True,
    ) -> None:
        """

        :param plot: Plot object for the scatter to be drawn
        :param x: x points coordinates
        :param y: y points coordinates
        :param list|None rangex: x range limits
        :param list|None rangey: y range limits
        :param int|list radius: circle radius
        :param bool nudge: moves the graph a little for better displaying

        """
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

        palette = displayio.Palette(1)
        palette[0] = circle_color

        if isinstance(radius, list):
            for i, _ in enumerate(x):
                plot.append(
                    Circle(
                        pixel_shader=palette, radius=radius[i], x=xnorm[i], y=ynorm[i]
                    )
                )
        else:

            for i, _ in enumerate(x):
                plot.append(
                    Circle(pixel_shader=palette, radius=radius, x=xnorm[i], y=ynorm[i])
                )

        if plot._showticks:
            plot._draw_ticks(x, y)
