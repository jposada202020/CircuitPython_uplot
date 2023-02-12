# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`ubar`
================================================================================

CircuitPython uscatter graph

* Author(s): Jose D. Montoya


"""
from bitmaptools import draw_line

# pylint: disable=too-many-arguments, invalid-name, protected-access
# pylint: disable=too-few-public-methods, no-self-use
class ubar:
    """
    Main class to display different graphics
    """

    def __init__(self, plot, x: any, y: any, color=0xFFFFFF) -> None:

        plot._drawbox()

        self._graphx = abs(plot._newxmax - plot._newxmin) // (len(x) + 2)
        self._graphy = abs(plot._newymax - plot._newymin) // (max(y) + 2)
        self._new_min = int(plot.normalize(0, max(y), max(y), 0, 0))
        self._new_max = int(plot.normalize(0, max(y), max(y), 0, max(y)))
        xstart = self._graphx
        bar_space = 10
        plot._plot_palette[3] = color

        for i, _ in enumerate(x):
            self._draw_rectangle(
                plot,
                xstart + (i * self._graphx),
                plot._newymin,
                self._graphx,
                self._graphy * y[i],
                3,
            )
            xstart = xstart + bar_space

    def _draw_rectangle(self, plot, x, y, width, height, color):
        """
        Helper function to draw bins rectangles
        """
        draw_line(plot._plotbitmap, x, y, x + width, y, color)
        draw_line(plot._plotbitmap, x, y, x, y - height, color)
        draw_line(plot._plotbitmap, x + width, y, x + width, y - height, color)
        draw_line(plot._plotbitmap, x + width, y - height, x, y - height, color)
