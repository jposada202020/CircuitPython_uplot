# SPDX-FileCopyrightText: Copyright (c) Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import displayio
import terminalio
import board
from adafruit_display_text import label
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

text_temperature = label.Label(terminalio.FONT, color=FOREGROUND_COLOR, scale=3)
text_temperature.anchor_point = 0.0, 0.0
text_temperature.anchored_position = 25, 0
g.append(text_temperature)

text_humidity = label.Label(terminalio.FONT, color=FOREGROUND_COLOR, scale=3)
text_humidity.anchor_point = 0.0, 0.0
text_humidity.anchored_position = 130, 0
g.append(text_humidity)

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

x = [10, 20, 30, 40, 50]
temp_y = [26, 25, 24, 23, 28]

g.append(plot_1)

display.show(g)
display.refresh()

dist = 3

ulogging(
    plot_1,
    x[0:dist],
    temp_y[0:dist],
    rangex=[0, 200],
    rangey=[0, 100],
    line_color=color.BLACK,
    ticksx=[10, 50, 80, 100],
    ticksy=[15, 30, 45, 60],
)

text_temperature.text = "{}C".format(temp_y[dist])
