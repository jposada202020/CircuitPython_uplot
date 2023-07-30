# SPDX-FileCopyrightText: Copyright (c) Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
from circuitpython_uplot.plot import Plot, color
from circuitpython_uplot.svg import SVG
from circuitpython_uplot.icons import FULL, Humidity, Temperature, Temperature2


# Setting up the display
display = board.DISPLAY

plot = Plot(0, 0, display.width, display.height)
SVG(plot, FULL, 50, 50, 2, color.YELLOW)
SVG(plot, Humidity, 150, 50, 2, color.TEAL)
SVG(plot, Temperature, 250, 50, 2, color.GREEN)

SVG(plot, Temperature2, 300, 50, 0.25, color.BLUE)
display.show(plot)
