# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from ulab import numpy as np
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.cartesian import Cartesian
from circuitpython_uplot.shade import shade

# This example is based in the following Library
# https://github.com/CedarGroveStudios/CircuitPython_TemperatureTools
# And this Wikipedia Article
# https://en.wikipedia.org/wiki/Heat_index


# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Plot(0, 0, display.width, display.height, padding=5)


def heat_index(temp, humidity):
    """
    Inspired by
    https://github.com/CedarGroveStudios/CircuitPython_TemperatureTools

    """

    heat_index_value = (
        -8.78469475556
        + 1.61139411 * temp
        + 2.33854883889 * humidity
        - 0.14611605 * temp * humidity
        - 0.012308094 * temp**2
        - 0.0164248277778 * humidity**2
        + 0.002211732 * temp**2 * humidity
        + 0.00072546 * temp * humidity**2
        - 0.000003582 * temp**2 * humidity**2
    )
    return heat_index_value


x = np.linspace(25, 50, num=2)

# Drawing the Shades
shade(
    plot,
    x,
    [25, 25],
    [26.3, 26.3],
    rangex=[25, 50],
    rangey=[25, 60],
    fill_color=0x59FF33,
)
shade(
    plot,
    x,
    [26.3, 26.3],
    [30.5, 30.5],
    rangex=[25, 50],
    rangey=[25, 60],
    fill_color=0xFFFDD0,
)
shade(
    plot,
    x,
    [30.5, 30.5],
    [40.5, 40.5],
    rangex=[25, 50],
    rangey=[25, 60],
    fill_color=0xFFEB99,
)
shade(
    plot,
    x,
    [40.5, 40.5],
    [53.5, 53.5],
    rangex=[25, 50],
    rangey=[25, 60],
    fill_color=0xFFDB58,
)
shade(
    plot,
    x,
    [53.5, 53.5],
    [60, 60],
    rangex=[25, 50],
    rangey=[25, 60],
    fill_color=0xFF9D5C,
)

# Creating some points to graph
x = np.linspace(25, 50, num=25)

# Drawing the graphs
for i in range(40, 110, 10):
    Cartesian(plot, x, heat_index(x, i), rangex=[25, 50], rangey=[25, 60])

display.show(plot)
