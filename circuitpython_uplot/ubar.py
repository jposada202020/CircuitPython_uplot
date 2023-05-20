# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`ubar`
================================================================================

CircuitPython scatter graph

* Author(s): Jose D. Montoya


"""

try:
    from circuitpython_uplot.uplot import Uplot
except ImportError:
    pass
import math
from bitmaptools import draw_line
from vectorio import Rectangle, Polygon

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"

# pylint: disable=too-many-arguments, invalid-name, protected-access
# pylint: disable=too-few-public-methods, no-self-use, too-many-locals
class ubar:
    """
    Main class to display different graphics
    """

    def __init__(
        self,
        plot: Uplot,
        x: list,
        y: list,
        color: int = 0xFFFFFF,
        fill: bool = False,
        bar_space=16,
        xstart=50,
    ) -> None:
        """
        :param Uplot plot: Plot object for the scatter to be drawn
        :param list x: x data
        :param list y: y data
        :param int color: boxes color. Defaults to const:``0xFFFFFF``
        :param bool fill: boxes fill attribute. Defaults to `False`
        :param int bar_space: space in pixels between the bars
        :param int xstart: start point in the x axis for the bar to start. Default to :const:`50`

        """
        self._bar_space = bar_space
        self._graphx = abs(plot._newxmax - plot._newxmin) // (len(x) + 4)
        self._graphy = abs(plot._newymax - plot._newymin) // (max(y) + 2)
        self._new_min = int(plot.transform(0, max(y), max(y), 0, 0))
        self._new_max = int(plot.transform(0, max(y), max(y), 0, max(y)))

        plot._plot_palette[plot._index_colorused] = color

        if fill:
            for i, _ in enumerate(x):
                plot.append(
                    Rectangle(
                        pixel_shader=plot._plot_palette,
                        width=self._graphx,
                        height=self._graphy * y[i],
                        x=xstart + (i * self._graphx),
                        y=plot._newymin - self._graphy * y[i],
                        color_index=plot._index_colorused,
                    )
                )

                delta = 20
                rx = int(delta * math.cos(-0.5))
                ry = int(delta * math.sin(-0.5))
                points = [
                    (0, 0),
                    (self._graphx, 0),
                    (self._graphx - rx, 0 + ry),
                    (0 - rx, 0 + ry),
                ]

                plot.append(
                    Polygon(
                        pixel_shader=plot._plot_palette,
                        points=points,
                        x=xstart + (i * self._graphx),
                        y=plot._newymin - self._graphy * y[i],
                        color_index=plot._index_colorused - 1,
                    )
                )
                points = [
                    (0, 0),
                    (0 - rx, 0 + ry),
                    (0 - rx, self._graphy * y[i]),
                    (0, self._graphy * y[i]),
                ]
                plot.append(
                    Polygon(
                        pixel_shader=plot._plot_palette,
                        points=points,
                        x=xstart + (i * self._graphx),
                        y=plot._newymin - self._graphy * y[i],
                        color_index=plot._index_colorused + 1,
                    )
                )

                plot.show_text(
                    str(y[i]),
                    xstart + (i * self._graphx) + self._graphx // 2,
                    plot._newymin,
                )
                xstart = xstart + self._bar_space
                plot._index_colorused = plot._index_colorused + 1
        else:
            for i, _ in enumerate(x):
                self._draw_rectangle(
                    plot,
                    xstart + (i * self._graphx),
                    plot._newymin,
                    self._graphx,
                    self._graphy * y[i],
                    plot._index_colorused,
                )
                delta = 20
                rx = int(delta * math.cos(-0.5))
                ry = int(delta * math.sin(-0.5))
                x0 = xstart + (i * self._graphx)
                y0 = plot._newymin - self._graphy * y[i]
                x1 = xstart + (i * self._graphx) + self._graphx
                y1 = plot._newymin - self._graphy * y[i]

                draw_line(
                    plot._plotbitmap, x0, y0, x0 - rx, y0 + ry, plot._index_colorused
                )
                draw_line(
                    plot._plotbitmap, x1, y1, x1 - rx, y1 + ry, plot._index_colorused
                )
                draw_line(
                    plot._plotbitmap,
                    x0 - rx,
                    y0 + ry,
                    x1 - rx,
                    y1 + ry,
                    plot._index_colorused,
                )
                draw_line(
                    plot._plotbitmap,
                    x0 - rx,
                    y0 + ry,
                    x0 - rx,
                    plot._newymin,
                    plot._index_colorused,
                )

                xstart = xstart + bar_space
                plot._index_colorused = plot._index_colorused + 1
                plot.show_text(
                    str(y[i]),
                    xstart + (i * self._graphx) - bar_space + self._graphx // 2,
                    plot._newymin,
                )

    def _draw_rectangle(
        self, plot: Uplot, x: int, y: int, width: int, height: int, color: int
    ) -> None:
        """
        Helper function to draw bins rectangles
        """
        draw_line(plot._plotbitmap, x, y, x + width, y, color)
        draw_line(plot._plotbitmap, x, y, x, y - height, color)
        draw_line(plot._plotbitmap, x + width, y, x + width, y - height, color)
        draw_line(plot._plotbitmap, x + width, y - height, x, y - height, color)
