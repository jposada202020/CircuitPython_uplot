# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from circuitpython_uplot.uplot import Uplot, color
from circuitpython_uplot.ubar import ubar

# Setting up the display
display = board.DISPLAY

# Configuring display dimensions
DISPLAY_WIDTH = 480
DISPLAY_HEIGHT = 320

# Defining the plot
plot = Uplot(
    0,
    0,
    DISPLAY_WIDTH,
    DISPLAY_HEIGHT,
    background_color=color.BLACK,
    padding=10,
    box_color=color.WHITE,
)

display.show(plot)

# Dummy data to plot
some_values = [55, 20, 25, 30, 35, 10]
a = ["a", "b", "c", "d", "e", "f"]

# Showing the plot
display.show(plot)

# Creating the bar
my_ubar = ubar(
    plot,
    a,
    some_values,
    0xFF1000,
    True,
    projection=False,
    max_value=50,
)
time.sleep(2)
# Changing all the bars to Yellow
my_ubar.update_colors(
    [color.YELLOW, color.YELLOW, color.YELLOW, color.YELLOW, color.YELLOW, color.YELLOW]
)

time.sleep(2)

# Changing the 3 bar to Purple
my_ubar.update_bar_color(2, color.PURPLE)
