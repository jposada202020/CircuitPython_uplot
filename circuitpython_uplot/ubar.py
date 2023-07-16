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
        projection=False,
    ) -> None:
        """
        :param Uplot plot: Plot object for the scatter to be drawn
        :param list x: x data
        :param list y: y data
        :param int color: boxes color. Defaults to const:``0xFFFFFF``
        :param bool fill: boxes fill attribute. Defaults to `False`
        :param int bar_space: space in pixels between the bars
        :param int xstart: start point in the x axis for the bar to start. Default to :const:`50`
        :param bool projection: creates projection of the bars given them depth.

        """
        y = [i * plot.scale for i in y]
        self._bar_space = int(bar_space / plot.scale)
        self._graphx = plot.scale * int(
            abs(plot._newxmax - plot._newxmin) / (len(x) + 4)
        )
        self._graphy = plot.scale * int(
            abs(plot._newymax - plot._newymin) / (max(y) + 2)
        )
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
                        y=int(plot._newymin - self._graphy * y[i] / plot.scale),
                        color_index=plot._index_colorused,
                    )
                )
                if projection:
                    delta = 20
                    rx = int(delta * math.cos(-0.5))
                    ry = int(delta * math.sin(-0.5))
                    points = [
                        (0, 0),
                        (self._graphx, 0),
                        (self._graphx - rx, 0 + ry),
                        (0 - rx, 0 + ry),
                    ]
                    plot._plot_palette[plot._index_colorused + 6] = color_fader(
                        plot._plot_palette[plot._index_colorused], 0.7, 1
                    )
                    plot.append(
                        Polygon(
                            pixel_shader=plot._plot_palette,
                            points=points,
                            x=xstart + (i * self._graphx),
                            y=plot._newymin - self._graphy * y[i],
                            color_index=plot._index_colorused + 6,
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
                            color_index=plot._index_colorused + 6,
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


def color_fader(source_color=None, brightness=1.0, gamma=1.0):
    """
    Function taken from https://github.com/CedarGroveStudios
    Copyright (c) 2022 JG for Cedar Grove Maker Studios
    License: MIT

    Scale a 24-bit RGB source color value in proportion to the brightness
    setting (0 to 1.0). Returns an adjusted 24-bit RGB color value or None if
    the source color is None (transparent). The adjusted color's gamma value is
    typically from 0.0 to 2.0 with a default of 1.0 for no gamma adjustment.

    :param int source_color: The color value to be adjusted. Default is None.
    :param float brightness: The brightness value for color value adjustment.
      Value range is 0.0 to 1.0. Default is 1.0 (maximum brightness).
    :param float gamma: The gamma value for color value adjustment. Value range
      is 0.0 to 2.0. Default is 1.0 (no gamma adjustment).

    :return int: The adjusted color value."""

    if source_color is None:
        return source_color

    # Extract primary colors and scale to brightness
    r = min(int(brightness * ((source_color & 0xFF0000) >> 16)), 0xFF)
    g = min(int(brightness * ((source_color & 0x00FF00) >> 8)), 0xFF)
    b = min(int(brightness * ((source_color & 0x0000FF) >> 0)), 0xFF)

    # Adjust result for gamma
    r = min(int(round((r**gamma), 0)), 0xFF)
    g = min(int(round((g**gamma), 0)), 0xFF)
    b = min(int(round((b**gamma), 0)), 0xFF)

    return (r << 16) + (g << 8) + b
