# SPDX-FileCopyrightText: Copyright (c) 2023 Casainho, Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from random import choice
import displayio
import terminalio
import board
from adafruit_display_text import label
from circuitpython_uplot.uplot import Uplot, color
from circuitpython_uplot.ucartesian import ucartesian

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

plot_2 = Uplot(
    0,
    180,
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
plot_2.tick_params(
    tickx_height=4, ticky_height=4, show_ticks=True, tickcolor=color.BLACK
)


temperatures = [26, 25, 24, 23, 28]
humidity = [66, 67, 71, 79]
x = list(range(0, 144, 1))
temp_y = [choice(temperatures) for _ in x]
humidity_y = [choice(humidity) for _ in x]

g.append(plot_1)
g.append(plot_2)

display.show(g)
display.refresh()

for i, element in enumerate(x):
    ucartesian(
        plot_1,
        x[0:i],
        temp_y[0:i],
        rangex=[0, 143],
        rangey=[0, 40],
        fill=False,
        line_color=color.BLACK,
        logging=True,
    )
    ucartesian(
        plot_2,
        x[0:i],
        humidity_y[0:i],
        rangex=[0, 143],
        rangey=[0, 100],
        fill=False,
        line_color=color.BLACK,
        logging=True,
    )
    text_temperature.text = f"{temp_y[i]}"
    text_humidity.text = f"{int(round(humidity_y[i], 0))}%"
    time.sleep(0.1)
