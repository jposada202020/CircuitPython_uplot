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

        self._axesparams = "box"

        self.padding = padding
        self._newxmin = padding
        self._newxmax = width - 1 * padding
        self._newymin = height - 1 * padding
        self._newymax = padding

        self._tickheight = 8
        self._tickcolor = 0xFFFFFF
        self._showticks = False
        self._tickgrid = False

        self._width = width
        self._height = height

        self._axeslinethikness = 1

        self._plotbitmap = displayio.Bitmap(width, height, 4)

        self._plot_palette = displayio.Palette(4)
        self._plot_palette[0] = 0x000000
        self._plot_palette[1] = 0xFFFFFF
        self._plot_palette[2] = self._tickcolor
        self.append(
            displayio.TileGrid(
                self._plotbitmap, pixel_shader=self._plot_palette, x=x, y=y
            )
        )

    def axs_params(self, axstype="box"):
        """
        Setting up axs visibility

        :param axs: argument with the kind of axs you selected
        :return: none

        """
        self._axesparams = axstype

    def _drawbox(self):
        if self._axesparams == "cartesian":
            draw_box = [True, True, False, False]
        elif self._axesparams == "line":
            draw_box = [False, True, False, False]
        else:
            draw_box = [True, True, True, True]

        if draw_box[0]:
            # y axes line
            draw_line(
                self._plotbitmap,
                self.padding,
                self.padding,
                self.padding,
                self._height - self.padding,
                1,
            )
        if draw_box[1]:
            draw_line(
                self._plotbitmap,
                self.padding,
                self._height - self.padding,
                self._width - self.padding,
                self._height - self.padding,
                1,
            )
        if draw_box[2]:
            draw_line(
                self._plotbitmap,
                self._width - self.padding,
                self.padding,
                self._width - self.padding,
                self._height - self.padding,
                1,
            )
        if draw_box[3]:
            draw_line(
                self._plotbitmap,
                self.padding,
                self.padding,
                self._width - self.padding,
                self.padding,
                1,
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
        self._drawbox()

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
        if self._showticks:
            self._draw_ticks(x, y)

    def _draw_ticks(self, x, y):
        """
        Draw ticks in the plot area

        :return:

        """
        ticks = np.array([10, 30, 50, 70, 90])
        subticks = np.array([20, 40, 60, 80])
        ticksxnorm = np.array(self.normalize(0, 100, np.min(x), np.max(x), ticks))
        ticksynorm = np.array(self.normalize(0, 100, np.min(y), np.max(y), ticks))

        subticksxnorm = np.array(self.normalize(0, 100, np.min(x), np.max(x), subticks))
        subticksynorm = np.array(self.normalize(0, 100, np.min(y), np.max(y), subticks))

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

        for tick in ticksxrenorm:
            draw_line(
                self._plotbitmap,
                tick,
                self._newymin,
                tick,
                self._newymin - self._tickheight,
                2,
            )
        for tick in ticksyrenorm:
            draw_line(
                self._plotbitmap,
                self._newxmin,
                tick,
                self._newxmin + self._tickheight,
                tick,
                2,
            )
        for tick in subticksxrenorm:
            draw_line(
                self._plotbitmap,
                tick,
                self._newymin,
                tick,
                self._newymin - self._tickheight // 2,
                2,
            )
        for tick in subticksyrenorm:
            draw_line(
                self._plotbitmap,
                self._newxmin,
                tick,
                self._newxmin + self._tickheight // 2,
                tick,
                2,
            )

        if self._tickgrid:
            self._draw_gridx(ticksxrenorm)
            self._draw_gridy(ticksyrenorm)

    def tick_params(self, tickheight=8, tickcolor=0xFFFFFF, tickgrid=False):
        """
        Function to set ticks parameters

        :param tickheight:
        :param tickcolor:

        :return: None

        """

        self._showticks = True
        self._tickheight = tickheight
        self._plot_palette[2] = tickcolor
        self._tickgrid = tickgrid

    def _draw_gridx(self, ticks_data):
        """
        draw plot grid

        :return: None

        """
        grid_espace = 10
        line_lenght = 10
        for tick in ticks_data:
            start = self._newymin
            while start >= self._newymax:
                draw_line(
                    self._plotbitmap,
                    tick,
                    start,
                    tick,
                    start - line_lenght,
                    2,
                )
                start = start - grid_espace - line_lenght

    def _draw_gridy(self, ticks_data):
        """
        draw plot grid

        :return: None

        """
        grid_espace = 10
        line_lenght = 10
        for tick in ticks_data:
            start = self._newxmin
            while start <= self._newxmax:
                draw_line(
                    self._plotbitmap,
                    start,
                    tick,
                    start + line_lenght,
                    tick,
                    2,
                )
                start = start + grid_espace + line_lenght
