# SPDX-FileCopyrightText: 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT


"""

`scatter`
================================================================================

CircuitPython scatter graph

* Author(s): Jose D. Montoya


"""
try:
    from typing import Optional, Union
    from circuitpython_uplot.plot import Plot
except ImportError:
    pass


from ulab import numpy as np
import displayio
from vectorio import Circle, Polygon

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"


_TRIANGLE = [(0, 0), (8, 0), (4, -7)]
_SQUARE = [(0, 0), (6, 0), (6, -6), (0, -6)]
_DIAMOND = [(0, 0), (3, -4), (6, 0), (3, 4)]


class Scatter:
    """
    Main class to display different graphics
    """

    def __init__(
        self,
        plot: Plot,
        x: Union[list, np.linspace, np.ndarray],
        y: Union[list, np.linspace, np.ndarray],
        rangex: Optional[list] = None,
        rangey: Optional[list] = None,
        radius: Optional[Union[list, int]] = 3,
        pointer_color: int = 0xFF905D,
        pointer: Optional[str] = None,
        nudge: bool = True,
    ) -> None:
        """

        :param plot: Plot object for the scatter to be drawn
        :param x: x points coordinates
        :param y: y points coordinates
        :param list|None rangex: x range limits
        :param list|None rangey: y range limits
        :param int|list radius: circle radius
        :param int pointer_color: pointer color. Default is 0xFF905D
        :param str|None pointer: pointer shape.
        :param bool nudge: moves the graph a little for better displaying

        """
        if nudge:
            nudge_factor = 1
        else:
            nudge_factor = 0

        if pointer is None:
            self._pointer = "circle"
        else:
            self._pointer = pointer

        self._radius = radius
        self._pointer_color = pointer_color

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

        self._xnorm = np.array(
            plot.transform(xmin, xmax, plot._newxmin, plot._newxmax, x),
            dtype=np.int16,
        )
        self._ynorm = np.array(
            plot.transform(ymin, ymax, plot._newymin, plot._newymax, y),
            dtype=np.int16,
        )

        self._draw_pointer(plot)

        if plot._showticks:
            plot._draw_ticks(x, y)

    def _draw_pointer(self, plot: Plot) -> None:
        """

        :param plot: Plot object for the scatter to be drawn

        """
        palette = displayio.Palette(1)
        palette[0] = self._pointer_color
        if isinstance(self._radius, list):
            for i, _ in enumerate(self._xnorm):
                plot.append(
                    Circle(
                        pixel_shader=palette,
                        radius=self._radius[i],
                        x=self._xnorm[i],
                        y=self._ynorm[i],
                    )
                )
        else:
            for i, _ in enumerate(self._xnorm):
                if self._pointer == "circle":
                    plot.append(
                        Circle(
                            pixel_shader=palette,
                            radius=self._radius,
                            x=self._xnorm[i],
                            y=self._ynorm[i],
                        )
                    )
                elif self._pointer == "triangle":
                    plot.append(
                        Polygon(
                            points=_TRIANGLE,
                            pixel_shader=palette,
                            x=self._xnorm[i],
                            y=self._ynorm[i],
                        )
                    )
                elif self._pointer == "square":
                    plot.append(
                        Polygon(
                            points=_SQUARE,
                            pixel_shader=palette,
                            x=self._xnorm[i],
                            y=self._ynorm[i],
                        )
                    )
                elif self._pointer == "diamond":
                    plot.append(
                        Polygon(
                            points=_DIAMOND,
                            pixel_shader=palette,
                            x=self._xnorm[i],
                            y=self._ynorm[i],
                        )
                    )
