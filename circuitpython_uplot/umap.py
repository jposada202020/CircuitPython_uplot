# SPDX-FileCopyrightText: 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT


"""

`umap`
================================================================================

CircuitPython color map graph

* Author(s): Jose D. Montoya


"""
try:
    from circuitpython_uplot.uplot import Uplot
except ImportError:
    pass

from ulab import numpy as np
import displayio
from vectorio import Rectangle

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/CircuitPython_uplot.git"


# pylint: disable=too-few-public-methods, invalid-name, duplicate-code, too-many-locals, too-many-arguments
# pylint: disable=unused-variable
class umap:
    """
    Main class to display different graphics
    """

    def __init__(
        self,
        plot: Uplot,
        data_points: np.ndarray,
        initial_color: int,
        final_color: int,
    ) -> None:

        """

        :param plot: Plot object for the scatter to be drawn
        :param data_points: data points to create the color map
        :param initial_color: initial color to create the color map
        :param final_color: final color to create the color map

        """

        xmin = np.min(data_points)
        xmax = np.max(data_points)

        xnorm = np.array(plot.transform(xmin, xmax, 0.0, 1.0, data_points))

        box_iny = data_points.shape[0]
        box_inx = data_points.shape[1]

        width = plot._newxmax - plot._newxmin
        height = plot._newymin - plot._newymax
        xdist = width // box_inx
        ydist = height // box_iny

        palette = displayio.Palette(box_inx * box_iny)
        start_color = initial_color
        end_color = final_color
        counter = 0
        for row in xnorm:
            for element in row:
                palette[counter] = color_fade(start_color, end_color, element)
                counter = counter + 1

        deltax = plot._newxmin
        deltay = plot._newymax
        color = 0
        for j in range(box_iny):
            for i in range(box_inx):
                plot.append(
                    Rectangle(
                        pixel_shader=palette,
                        x=deltax,
                        y=deltay,
                        width=xdist,
                        height=ydist,
                        color_index=color,
                    )
                )
                deltax = deltax + xdist
                color = color + 1

            deltax = plot._newxmin
            deltay = deltay + ydist


def color_to_tuple(value):
    """Converts a color from a 24-bit integer to a tuple.
    :param value: RGB LED desired value - can be a RGB tuple or a 24-bit integer.
    """
    if isinstance(value, tuple):
        return value
    if isinstance(value, int):
        if value >> 24:
            raise ValueError("Only bits 0->23 valid for integer input")
        r = value >> 16
        g = (value >> 8) & 0xFF
        b = value & 0xFF
        return [r, g, b]

    raise ValueError("Color must be a tuple or 24-bit integer value.")


def color_fade(start_color: int, end_color: int, fraction: float):
    """Linear extrapolation of a color between two RGB colors (tuple or 24-bit integer).
    :param start_color: starting color
    :param end_color: ending color
    :param fraction: Floating point number  ranging from 0 to 1 indicating what
    fraction of interpolation between start_color and end_color.
    """

    start_color = color_to_tuple(start_color)
    end_color = color_to_tuple(end_color)
    if fraction >= 1:
        return end_color
    if fraction <= 0:
        return start_color

    faded_color = [0, 0, 0]
    for i in range(3):
        faded_color[i] = start_color[i] - int(
            (start_color[i] - end_color[i]) * fraction
        )
    return faded_color
