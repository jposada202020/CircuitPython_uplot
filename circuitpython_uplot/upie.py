# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`upie`
================================================================================

CircuitPython pie graph

* Author(s): Jose D. Montoya


"""

import math
import bitmaptools

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"

# pylint: disable=too-many-arguments, invalid-name, no-self-use
class upie:
    """
    Class to draw pie
    """

    def __init__(self, plot, data: list, x: int = 130, y: int = 130, radius: int = 50):
        """

        :param plot: Plot object for the upie to be drawn
        :param list data: data to make the pie
        :param x: pie center x coordinate
        :param y: pie center y coordinate
        :param int radius: pie radius

        """

        plot._drawbox()

        step = 2
        total = sum(data)
        per = [int(i / total * 360) for i in data]

        start = 0
        end = 0
        index_color = 4

        for pie in per:
            end = end + pie
            for i in range(start, end, step):
                self.draw_lines(plot._plotbitmap, x, y, radius, i, index_color)
            start = start + pie
            index_color = index_color + 1

    def draw_lines(self, bitmap, x, y, radius, angle, color):
        """

        :param bitmap: bitmap to be drawn in
        :param x: center x coordinate
        :param y: center y coordinate
        :param radius: pie radius in pixels
        :param angle: line angle
        :param color: color index
        :return: None

        """
        return bitmaptools.draw_line(
            bitmap,
            x,
            y,
            x + int(radius * math.cos(angle * math.pi / 180)),
            y + int(radius * math.sin(angle * math.pi / 180)),
            color,
        )
