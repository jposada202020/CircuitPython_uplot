# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`usvg`
================================================================================

CircuitPython svg icon utility for CircuitPython_uplot

* Author(s): Jose D. Montoya


"""
try:
    from circuitpython_uplot.uplot import Uplot
except ImportError:
    pass
from bitmaptools import draw_line


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"


# pylint: disable=too-many-arguments, invalid-name, no-self-use, too-few-public-methods
# pylint: disable=too-many-locals, too-many-branches, protected-access, unnecessary-list-index-lookup
class usvg:
    """
    class to render svg images in the plot area
    """

    def __init__(
        self,
        plot: Uplot,
        icon: dict,
        x: int,
        y: int,
        factor: float,
        color: int = 0xFFFFFF,
    ) -> None:
        """

        :param Uplot plot: Plot object for the log to be drawn
        :param dictionary icon: icon dictionary
        :param int x: x position for the svg image
        :param int y: y position for the svg image
        :param float factor: scale factor for the svg
        :param color: color of the svg file. Defaults to ``White``, ``0xFFFFFF``


        """
        plot._plot_palette[plot._index_colorused] = color

        for key in icon.keys():
            path = icon[key]

            for index, _ in enumerate(path):
                if index + 1 >= len(path):
                    break
                draw_line(
                    plot._plotbitmap,
                    x + int(path[index][0] * factor),
                    y + int(path[index][1] * factor),
                    x + int(path[index + 1][0] * factor),
                    y + int(path[index + 1][1] * factor),
                    plot._index_colorused,
                )

        plot._index_colorused = plot._index_colorused + 1
