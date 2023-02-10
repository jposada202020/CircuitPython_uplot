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

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"


# pylint: disable=too-many-arguments


class Uplot(displayio.Group):
    def __init__(self, x=0, y=0, width=None, height=None):
        super().__init__(x=x, y=y, scale=1)
        self._width = width - 1
        self._height = height-1
        self._axes_palette = displayio.Palette(2)
        self._axes_palette[0] = 0x000000
        self._axes_palette[1] = 0xFFFFFF
        self._plotbitmap = displayio.Bitmap(self._width, height-1, 2)
        self._axesbitmap = displayio.Bitmap(self._width-30, 20, 2)
        self.append(displayio.TileGrid(self._plotbitmap, pixel_shader=self._axes_palette, x=0, y=0))
        self._drawbox()
        self.axes()

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
        draw_line(self._plotbitmap, 0, 0, self._width-1, 0, 1)
        draw_line(self._plotbitmap, 0, 0, 0, self._height-1, 1)
        draw_line(self._plotbitmap, self._width-1, 0, self._width-1, self._height-1, 1)
        draw_line(self._plotbitmap, 0, self._height-1, self._width-1, self._height-1, 1)

    def axes(self, line_color=1):
        draw_line(self._axesbitmap, 10, 15, 20, 15, 1)
        self.append(displayio.TileGrid(self._axesbitmap, pixel_shader=self._axes_palette, x=10, y=10))

