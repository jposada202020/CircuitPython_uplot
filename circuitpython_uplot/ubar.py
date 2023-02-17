# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`ubar`
================================================================================

CircuitPython scatter graph

* Author(s): Jose D. Montoya


"""
from bitmaptools import draw_line
from vectorio import Rectangle

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"

# pylint: disable=too-many-arguments, invalid-name, protected-access
# pylint: disable=too-few-public-methods, no-self-use
class ubar:
    """
    Main class to display different graphics
    """

    def __init__(self, plot, x: any, y: any, color=0xFFFFFF, fill=False) -> None:

        self._graphx = abs(plot._newxmax - plot._newxmin) // (len(x) + 2)
        self._graphy = abs(plot._newymax - plot._newymin) // (max(y) + 2)
        self._new_min = int(plot.transform(0, max(y), max(y), 0, 0))
        self._new_max = int(plot.transform(0, max(y), max(y), 0, max(y)))

        bar_space = max(2, plot._width // 30)
        xstart = self._graphx + bar_space

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
                xstart = xstart + bar_space
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
                xstart = xstart + bar_space
                plot._index_colorused = plot._index_colorused + 1

    def _draw_rectangle(self, plot, x, y, width, height, color):
        """
        Helper function to draw bins rectangles
        """
        draw_line(plot._plotbitmap, x, y, x + width, y, color)
        draw_line(plot._plotbitmap, x, y, x, y - height, color)
        draw_line(plot._plotbitmap, x + width, y, x + width, y - height, color)
        draw_line(plot._plotbitmap, x + width, y - height, x, y - height, color)
