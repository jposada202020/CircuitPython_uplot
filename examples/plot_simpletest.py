# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
from circuitpython_uplot.plot import Plot

# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Plot(0, 0, display.width, display.height)

plot.draw_circle(radius=8, x=120, y=120)

display.root_group = plot
