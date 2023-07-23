# SPDX-FileCopyrightText: Copyright (c) Jose D. Montoya
#
# SPDX-License-Identifier: MIT

# In order to run this example you need to install the following libraries:
# - adafruit_display_text
# - adafruit_bitmap_font
# - CircuitPython_TABLE (from https://github.com/jposada202020/CircuitPython_TABLE)

import time
import displayio
import board
from table import Table
from circuitpython_uplot.uplot import Uplot, color
from circuitpython_uplot.ulogging import ulogging

# Create a display object
display = board.DISPLAY

# Create a table object
# To use the font, create a fonts directory in the root of the CIRCUITPY drive,
# and add the font file from the fonts folder
my_table = Table(
    95,
    65,
    200,
    150,
    [("-------------", "-----------")],
    [
        ("Range", "Values"),
        ("Temp", "-50-125"),
        ("Humidity", "0-100%"),
    ],
    "fonts/LibreBodoniv2002-Bold-10.bdf",
    color.BLUE,
)

# Create a group to hold the objects
g = displayio.Group()

# Create a plot object
plot_1 = Uplot(
    0,
    50,
    200,
    160,
    padding=1,
    show_box=True,
    box_color=color.BLACK,
    background_color=color.WHITE,
)

plot_1.tick_params(
    tickx_height=4, ticky_height=4, show_ticks=True, tickcolor=color.BLUE
)

# Defining some data
x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
temp_y = [26, 25, 24, 23, 28, 24, 54, 76, 34, 23]

# Create a ulogging object
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

# Append the objects to the group
g.append(plot_1)
g.append(my_table)
# Show the group
display.show(g)

while True:
    for i in range(len(x)):
        my_log.draw_points(plot_1, x[0:i], temp_y[0:i])
        time.sleep(1)
