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
    box_color=color.BLACK,
)

# Dummy data to plot
some_values = [55, 20, 25, 30, 35, 10]
a = ["a", "b", "c", "d", "e", "f"]

add = 1
# Showing the plot
display.show(plot)

# Creating the bar
my_ubar = ubar(
    plot,
    a,
    some_values,
    0xFF1000,
    True,
    color_palette=[
        0xFF1000,
        0x00FF00,
        0x0000FF,
        0xFFFF00,
        0x00FFFF,
        0x123456,
    ],
    max_value=100,
)

for i in range(20):
    values_changed = [j + add for j in some_values]
    my_ubar.update_values(values_changed)
    add += 1
    time.sleep(0.1)

for i in range(20):
    values_changed = [j + add for j in some_values]
    my_ubar.update_values(values_changed)
    add -= 1
    time.sleep(0.1)
