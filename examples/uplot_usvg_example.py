# SPDX-FileCopyrightText: Copyright (c) Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
from circuitpython_uplot.uplot import Uplot, color
from circuitpython_uplot.usvg import usvg
from circuitpython_uplot.icons import FULL, Humidity, Temperature, Temperature2


# Setting up the display
display = board.DISPLAY

plot = Uplot(0, 0, display.width, display.height)
usvg(plot, FULL, 50, 50, 2, color.YELLOW)
usvg(plot, Humidity, 150, 50, 2, color.TEAL)
usvg(plot, Temperature, 250, 50, 2, color.GREEN)

usvg(plot, Temperature2, 300, 50, 0.25, color.BLUE)
display.show(plot)
