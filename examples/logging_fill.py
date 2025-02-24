# SPDX-FileCopyrightText: Copyright (c) Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import displayio
import board
from circuitpython_uplot.plot import Plot, color
from circuitpython_uplot.logging import Logging

# Setting up the display
display = board.DISPLAY

group = displayio.Group()

palette = displayio.Palette(1)
palette[0] = 0x000000

plot_1 = Plot(
    0,
    0,
    150,
    60,
    padding=1,
    show_box=True,
    box_color=color.BLACK,
    background_color=color.TEAL,
    scale=2,
)

plot_1.tick_params(
    tickx_height=4, ticky_height=4, show_ticks=True, tickcolor=color.BLACK
)

plot_2 = Plot(
    0,
    150,
    300,
    120,
    padding=1,
    show_box=True,
    box_color=color.BLACK,
    background_color=color.YELLOW,
    scale=1,
)

plot_2.tick_params(
    tickx_height=4, ticky_height=4, show_ticks=True, tickcolor=color.BLACK
)

x = [10, 20, 30, 40, 50]
temp_y = [26, 25, 24, 23, 28]

Logging(
    plot_1,
    x,
    temp_y,
    rangex=[0, 200],
    rangey=[0, 50],
    line_color=color.BLACK,
    ticksx=[10, 50, 80, 100],
    ticksy=[15, 30, 45, 60],
    fill=True,
)
Logging(
    plot_2,
    x,
    temp_y,
    rangex=[0, 200],
    rangey=[0, 50],
    line_color=color.BLACK,
    ticksx=[10, 50, 80, 100],
    ticksy=[15, 30, 45, 60],
    fill=True,
)

group.append(plot_1)
group.append(plot_2)

display.root_group = group

time.sleep(10)
