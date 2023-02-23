# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`upie`
================================================================================

CircuitPython pie graph

* Author(s): Jose D. Montoya


"""
try:
    from circuitpython_uplot.uplot import Uplot
except ImportError:
    pass


import math
from vectorio import Polygon

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"

# pylint: disable=too-many-arguments, invalid-name, no-self-use
class upie:
    """
    Class to draw pie
    """

    def __init__(
        self, plot: Uplot, data: list, x: int = 0, y: int = 0, radius: int = 40
    ) -> None:
        """

        :param Uplot plot: Plot object for the upie to be drawn
        :param list data: data to make the pie
        :param x: pie center x coordinate
        :param y: pie center y coordinate
        :param int radius: pie radius

        """

        step = 1
        total = sum(data)
        per = [int(i / total * 360) for i in data]

        start = 0
        end = 0
        index_color = 4
        self.pointlist = [(x, y)]
        for pie in per:
            end = end + pie
            for i in range(start, end + 1, step):
                self.get_points(x, y, radius, i)
            self.pointlist.append((x, y))
            plot.append(
                Polygon(
                    pixel_shader=plot._plot_palette,
                    points=self.pointlist,
                    x=plot._width // 2,
                    y=plot._height // 2,
                    color_index=index_color,
                )
            )
            start = start + pie
            index_color = index_color + 1
            self.pointlist = [(x, y)]

    def get_points(self, x: int, y: int, radius: int, angle: float) -> None:
        """

        :param bitmap: bitmap to be drawn in
        :param x: center x coordinate
        :param y: center y coordinate
        :param radius: pie radius in pixels
        :param angle: line angle
        :param color: color index
        :return: None

        """
        self.pointlist.append(
            (
                x + int(radius * math.cos(angle * math.pi / 180)),
                y + int(radius * math.sin(angle * math.pi / 180)),
            )
        )
