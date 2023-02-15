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

try:
    from typing import Union
    from typing_extensions import Literal
except ImportError:
    pass

import displayio
from bitmaptools import draw_line
from vectorio import Circle
from ulab import numpy as np


__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"


# pylint: disable=too-many-arguments, too-many-instance-attributes, too-many-locals


class Uplot(displayio.Group):
    """
    Canvas Class to add different elements to the screen.
    The origin point set by ``x`` and ``y`` properties

    :param int x: origin x coordinate
    :param int y: origin y coordinate
    :param int width: plot box width in pixels
    :param int height: plot box height in pixels
    :param int padding: padding for the plot box in all directions

    """

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 100,
        height: int = 100,
        padding: int = 15,
        show_box: bool = True,
    ) -> None:
        if width not in range(50, 481):
            print("Be sure to verify your values. Defaulting to width=100")
            width = 100
        if height not in range(50, 321):
            print("Be sure to verify your values. Defaulting to height=100")
            height = 100
        if x + width > 481:
            print(
                "Modify this settings. Some of the graphics will not shown int the screen"
            )
            print("Defaulting to x=0")
            x = 0
        if y + height > 321:
            print(
                "Modify this settings. Some of the graphics will not shown int the screen"
            )
            print("Defaulting to y=0")
            y = 0

        super().__init__(x=x, y=y, scale=1)

        self._axesparams = "box"

        self.padding = padding
        self._newxmin = padding
        self._newxmax = width - padding

        self._newymin = height - padding
        self._newymax = padding

        self._tickheight = 8
        self._tickcolor = 0xFFFFFF
        self._showticks = False
        self._tickgrid = False

        self._barcolor = 0xFFFFFF

        self._piecolor = 0xFFFFFF

        self._width = width
        self._height = height

        self._plotbitmap = displayio.Bitmap(width, height, 10)

        if show_box:
            self._drawbox()

        self._plot_palette = displayio.Palette(10)
        self._plot_palette[0] = 0x000000
        self._plot_palette[1] = 0xFFFFFF
        self._plot_palette[2] = self._tickcolor
        self._plot_palette[3] = self._barcolor
        self._plot_palette[4] = 0xFFFF00
        self._plot_palette[5] = 0xFF0000
        self._plot_palette[6] = 0x7428EF
        self._plot_palette[7] = 0x005E99
        self._plot_palette[8] = 0x00A76D
        self._plot_palette[9] = 0x2C4971
        self.append(
            displayio.TileGrid(
                self._plotbitmap, pixel_shader=self._plot_palette, x=0, y=0
            )
        )

    def axs_params(self, axstype: Literal["box", "cartesian", "line"] = "box") -> None:
        """
        Setting up axs visibility

        :param axstype: argument with the kind of axs you selected
        :return: None

        """
        self._axesparams = axstype

    def _drawbox(self):
        """
        Draw the plot box

        :return: None

        """

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

    def draw_circle(self, radius: int = 5, x: int = 100, y: int = 100) -> None:
        """
        Draw a circle in the plot area

        :param int radius: circle radius
        :param int x: circles center x coordinate position in pixels, Defaults to 100.
        :param int y: circles center y coordinate position in pixels. Defaults to 100.

        :return: None

        """
        palette = displayio.Palette(1)
        palette[0] = 0xFFFFFF
        self.append(Circle(pixel_shader=palette, radius=radius, x=x, y=y))

    @staticmethod
    def normalize(
        oldrangemin: Union[float, int],
        oldrangemax: Union[float, int],
        newrangemin: Union[float, int],
        newrangemax: Union[float, int],
        value: Union[float, int],
    ) -> Union[float, int]:
        """
        This function converts the original value into a new defined value in the new range

        :param int|float oldrangemin: minimum of the original range
        :param int|float oldrangemax: maximum of the original range
        :param int|float newrangemin: minimum of the new range
        :param int|float newrangemax: maximum of the new range
        :param int|float value: value to be converted
        :return int|float: converted value

        """

        return (
            ((value - oldrangemin) * (newrangemax - newrangemin))
            / (oldrangemax - oldrangemin)
        ) + newrangemin

    def _draw_ticks(self, x: int, y: int) -> None:
        """
        Draw ticks in the plot area

        :param int x: x coord
        :param int y: y coord
        :return:None

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

    def tick_params(
        self, tickheight: int = 8, tickcolor: int = 0xFFFFFF, tickgrid: bool = False
    ) -> None:
        """
        Function to set ticks parameters

        :param int tickheight: tick height in pixels
        :param int tickcolor: tick color in hex
        :param bool tickgrid: defines if the grid is to be shown
        :return: None

        """

        self._showticks = True
        self._tickheight = tickheight
        self._plot_palette[2] = tickcolor
        self._tickgrid = tickgrid

    def _draw_gridx(self, ticks_data: list[int]) -> None:
        """
        Draws the plot grid
        :param list[int] ticks_data: ticks data information
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

    def _draw_gridy(self, ticks_data: list[int]) -> None:
        """
        Draws plot grid in the y axs
        :param list[int] ticks_data: ticks data information
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

    def update_plot(self) -> None:
        """
        Function to update graph

        :return: None

        """

        self._drawbox()