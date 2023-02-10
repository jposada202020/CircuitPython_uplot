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
    """
    Main class to display different graphics
    """

    def __init__(self, x=0, y=0, width=None, height=None):
        super().__init__(x=x, y=y, scale=1)
        fontsize = 35
        self._yorigin = height - fontsize

        self._width = width - 1
        self._height = height - 1

        self._plotbitmap = displayio.Bitmap(self._width, height - 1, 2)

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

        self._axesxbitmap = displayio.Bitmap(self._axesxbitmap_width, self._axesxbitmap_height, 2)
        self._axesybitmap = displayio.Bitmap(self._axesybitmap_width, self._axesybitmap_height, 4)
        #self._axesybitmap.fill(2)
        self.append(
            displayio.TileGrid(
                self._plotbitmap, pixel_shader=self._axes_palette, x=0, y=0
            )
        )
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
        draw_line(self._plotbitmap, 0, 0, self._width - 1, 0, 1)
        draw_line(self._plotbitmap, 0, 0, 0, self._height - 1, 1)
        draw_line(
            self._plotbitmap, self._width - 1, 0, self._width - 1, self._height - 1, 1
        )
        draw_line(
            self._plotbitmap, 0, self._height - 1, self._width - 1, self._height - 1, 1
        )

    def axes(self, line_color=1):
        """
        Fucntion to display the plot axes
        :param line_color: index of the color palette
        :return: None
        """
        draw_line(self._axesxbitmap, 0, self._axesxbitmap_height//2, self._axesxbitmap_width, self._axesxbitmap_height//2, line_color)
        draw_line(self._axesybitmap, self._axesybitmap_width-1, 0, self._axesybitmap_width-1, self._axesybitmap_height, line_color)

        self.append(
            displayio.TileGrid(
                self._axesxbitmap, pixel_shader=self._axes_palette, x=15, y=self._yorigin
            )
        )
        self.append(
            displayio.TileGrid(
                self._axesybitmap, pixel_shader=self._axesy_palette, x=15- self._axesybitmap_width, y=self._height-self._axesybitmap_height  - self._axesxbitmap_height
            )
        )
