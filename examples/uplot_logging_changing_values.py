# SPDX-FileCopyrightText: Copyright (c) Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import displayio
import board
from circuitpython_uplot.uplot import Uplot, color
from circuitpython_uplot.ulogging import ulogging

# Setting up the display
display = board.DISPLAY

plot = Uplot(0, 0, display.width, display.height)
g = displayio.Group()

DISPLAY_WIDTH = 200
DISPLAY_HEIGHT = 200
FOREGROUND_COLOR = color.BLACK
BACKGROUND_COLOR = color.WHITE

background_bitmap = displayio.Bitmap(DISPLAY_WIDTH, DISPLAY_HEIGHT, 1)
# Map colors in a palette
palette = displayio.Palette(1)
palette[0] = BACKGROUND_COLOR
# Create a Tilegrid with the background and put in the displayio group
t = displayio.TileGrid(background_bitmap, pixel_shader=palette)
g.append(t)


plot_1 = Uplot(
    0,
    50,
    200,
    60,
    padding=1,
    show_box=True,
    box_color=color.BLACK,
    background_color=color.WHITE,
)

plot_1.tick_params(
    tickx_height=4, ticky_height=4, show_ticks=True, tickcolor=color.BLACK
)

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
temp_y = [26, 25, 24, 23, 28, 24, 54, 76, 34, 23]

g.append(plot_1)

display.show(g)
display.refresh()

my_log = ulogging(
    plot_1,
    x,
    temp_y,
    rangex=[0, 200],
    rangey=[0, 100],
    line_color=color.BLACK,
    ticksx=[10, 50, 80, 100],
    ticksy=[15, 30, 45, 60],
)


while True:
    for i in range(len(x)):
        my_log.draw_points(plot_1, x[0:i], temp_y[0:i])
        time.sleep(1)
