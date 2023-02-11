# SPDX-FileCopyrightText: 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

"""

`uplot`
================================================================================

CircuitPython Plot Class

* Author(s): Jose D. Montoya

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

import displayio
from bitmaptools import draw_line
from vectorio import Circle
from ulab import numpy as np


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"


# pylint: disable=too-many-arguments, too-many-instance-attributes, too-many-locals


class Uplot(displayio.Group):
    """
    Main class to display different graphics
    """

    def __init__(self, x=0, y=0, width=None, height=None, padding=15):
        super().__init__(x=x, y=y, scale=1)
        np.set_printoptions(threshold=200)

        self.padding = padding
        self._newxmin = padding
        self._newxmax = width - 1 * padding
        self._newymin = height - 1 * padding
        self._newymax = padding

        self._tickheight = 8

        self._width = width
        self._height = height

        self._axeslinethikness = 1

        self._plotbitmap = displayio.Bitmap(width, height, 2)

        self._axes_palette = displayio.Palette(2)
        self._axes_palette[0] = 0x000000
        self._axes_palette[1] = 0xFFFFFF
        self._axescolorindex = 2

        self._axesy_palette = displayio.Palette(4)
        self._axesy_palette.make_transparent(0)
        self._axesy_palette[1] = 0xFFFFFF
        self._axesy_palette[2] = 0x00FF00
        self._axesy_palette[3] = 0x0000FF

        self._axesxbitmap_height = 20
        self._axesxbitmap_width = self._width - 30

        self._axesybitmap_height = self._height - 30
        self._axesybitmap_width = 20

        self._axesxbitmap = displayio.Bitmap(
            self._axesxbitmap_width, self._axesxbitmap_height, 2
        )
        self._axesybitmap = displayio.Bitmap(
            self._axesybitmap_width, self._axesybitmap_height, 4
        )
        self.append(
            displayio.TileGrid(
                self._plotbitmap, pixel_shader=self._axes_palette, x=x, y=y
            )
        )
        self._drawbox()

    @property
    def tickheight(self):
        """
        The plot width, in pixels. (getter only)
        :return: int

        """
        return self._tickheight

    @tickheight.setter
    def tickheight(self, tick_height):
        """
        The plot width, in pixels.

        """

        self._tickheight = tick_height

    @property
    def width(self):
        """The plot width, in pixels. (getter only)
        :return: int
        """
        return self._width

    @property
    def height(self):
        """The plot height, in pixels. (getter only)
        :return: int
        """
        return self._height

    def _drawbox(self):
        draw_line(
            self._plotbitmap,
            self.padding,
            self.padding,
            self._width - self.padding,
            self.padding,
            1,
        )
        draw_line(
            self._plotbitmap,
            self.padding,
            self.padding,
            self.padding,
            self._height - self.padding,
            1,
        )
        draw_line(
            self._plotbitmap,
            self._width - self.padding,
            self.padding,
            self._width - self.padding,
            self._height - self.padding,
            1,
        )
        draw_line(
            self._plotbitmap,
            self.padding,
            self._height - self.padding,
            self._width - self.padding,
            self._height - self.padding,
            1,
        )

    def axes(self, line_color=1):
        """

        Function to display the plot axes

        :param line_color: index of the color palette
        :return: None

        """
        draw_line(
            self._axesxbitmap,
            0,
            self._axesxbitmap_height // 2,
            self._axesxbitmap_width,
            self._axesxbitmap_height // 2,
            line_color,
        )
        draw_line(
            self._axesybitmap,
            self._axesybitmap_width - 1,
            0,
            self._axesybitmap_width - 1,
            self._axesybitmap_height,
            line_color,
        )

        self.append(
            displayio.TileGrid(
                self._axesxbitmap,
                pixel_shader=self._axes_palette,
                x=15,
                y=self._yorigin,
            )
        )
        self.append(
            displayio.TileGrid(
                self._axesybitmap,
                pixel_shader=self._axesy_palette,
                x=15 - self._axesybitmap_width,
                y=self._height
                - self._axesybitmap_height
                - self._axesxbitmap_height
                - self._axeslinethikness
                - 2,
            )
        )

    def draw_circle(self, radius=5, x=100, y=100):
        """
        Draw a circle in the plot area
        :param radius: circle radius
        :param x: circles center x coordinate position in pixels, Defaults to 100.
        :param y: circles center y coordinate position in pixels. Defaults to 100.
        :return: None
        """
        palette = displayio.Palette(1)
        palette[0] = 0xFFFFFF
        self.append(Circle(pixel_shader=palette, radius=radius, x=x, y=y))

    @staticmethod
    def normalize(oldrangemin, oldrangemax, newrangemin, newrangemax, value):
        """
        This function converts the original value into a new defined value in the new range
        :param oldrangemin: minimum of the original range
        :param oldrangemax: maximum of the original range
        :param newrangemin: minimum of the new range
        :param newrangemax: maximum of the new range
        :param value: value to be converted
        :return: converted value
        """
        return (
            ((value - oldrangemin) * (newrangemax - newrangemin))
            / (oldrangemax - oldrangemin)
        ) + newrangemin

    def draw_plot(self, x, y):
        """
        Function to draw the plot

        :param x: data for x points
        :param y: data for y points
        :return: None

        """
        ticks = np.array([10, 30, 50, 70, 90])
        subticks = np.array([20, 40, 60, 80, 100])
        ticksxnorm = np.array(self.normalize(10, 100, np.min(x), np.max(x), ticks))
        ticksynorm = np.array(self.normalize(10, 100, np.min(y), np.max(y), ticks))

        subticksxnorm = np.array(
            self.normalize(10, 100, np.min(x), np.max(x), subticks)
        )
        subticksynorm = np.array(
            self.normalize(10, 100, np.min(y), np.max(y), subticks)
        )
        x = np.array(x)
        y = np.array(y)
        xnorm = np.array(
            self.normalize(np.min(x), np.max(x), self._newxmin, self._newxmax, x),
            dtype=np.uint16,
        )
        ynorm = np.array(
            self.normalize(np.min(y), np.max(y), self._newymin, self._newymax, y),
            dtype=np.uint16,
        )
        ticksxrenorm = np.array(
            self.normalize(
                np.min(x), np.max(x), self._newxmin, self._newxmax, ticksxnorm
            ),
            dtype=np.uint16,
        )
        ticksyrenorm = np.array(
            self.normalize(
                np.min(y), np.max(y), self._newymin, self._newymax, ticksynorm
            ),
            dtype=np.uint16,
        )
        subticksxrenorm = np.array(
            self.normalize(
                np.min(x), np.max(x), self._newxmin, self._newxmax, subticksxnorm
            ),
            dtype=np.uint16,
        )
        subticksyrenorm = np.array(
            self.normalize(
                np.min(y), np.max(y), self._newymin, self._newymax, subticksynorm
            ),
            dtype=np.uint16,
        )

        # np.set_printoptions(threshold=200)
        for index, _ in enumerate(xnorm):
            if index + 1 >= len(xnorm):
                break
            draw_line(
                self._plotbitmap,
                xnorm[index],
                ynorm[index],
                xnorm[index + 1],
                ynorm[index + 1],
                1,
            )
        for tick in ticksxrenorm:
            draw_line(
                self._plotbitmap,
                tick,
                self._newymin,
                tick,
                self._newymin - self.tickheight,
                1,
            )
        for tick in ticksyrenorm:
            draw_line(
                self._plotbitmap,
                self._newxmin,
                tick,
                self._newxmin + self.tickheight,
                tick,
                1,
            )
        for tick in subticksxrenorm:
            draw_line(
                self._plotbitmap,
                tick,
                self._newymin,
                tick,
                self._newymin - self.tickheight // 2,
                1,
            )
        for tick in subticksyrenorm:
            draw_line(
                self._plotbitmap,
                self._newxmin,
                tick,
                self._newxmin + self.tickheight // 2,
                tick,
                1,
            )
