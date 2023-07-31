# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
import displayio
from ulab import numpy as np
from table import Table
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.scatter import Scatter
from circuitpython_uplot.cartesian import Cartesian

# In order to run this example you need to install the following libraries:
# - adafruit_display_text
# - adafruit_bitmap_font
# - CircuitPython_TABLE (from https://github.com/jposada202020/CircuitPython_TABLE)

g = displayio.Group()

table_width = 125

# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Plot(0, 0, display.width - table_width, display.height, padding=1)
plot.tick_params(tickx_height=12, ticky_height=12, tickcolor=0x939597, tickgrid=True)
plot_table = Plot(
    display.width - table_width - 1, 0, table_width - 1, display.height, padding=1
)

display.show(g)
g.append(plot)
g.append(plot_table)


general_rangex = [0, 17]
general_rangey = [0, 70]

# Creating the values
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
y = np.array([3, 14, 23, 25, 23, 15, 9, 5, 9, 13, 17, 24, 32, 36, 46])

# Creating the table
# To use the font, create a fonts directory in the root of the CIRCUITPY drive,
# and add the font file from the fonts folder
# fmt: off
my_table = Table(
    10,
    10,
    140,
    315,
    [("-----------", "-----------",)],
    [("Value X", "Value Y",), ("1", "3",), ("2", "14",),("3", "23",),("4", "25",),
     ("5", "23",),("6", "15",),("7", "9",),("8", "5",),("9", "9",),("10", "13",),
     ("11", "17",),("12", "24",),("13", "32",),("14", "36",),
     ("15", "46",)],
    "fonts/LibreBodoniv2002-Bold-10.bdf",
    text_color = 0xFFFFFF,
)
# fmt: on
plot_table.append(my_table)

# Polyfit Curve third degree
z = np.polyfit(x, y, 3)
new_x = np.linspace(0, 16, 50)
fit = z[0] * new_x**3 + z[1] * new_x**2 + z[2] * new_x + z[3]
Cartesian(plot, new_x, fit, rangex=general_rangex, rangey=general_rangey)

# Polyfit Curve Second degree
z = np.polyfit(x, y, 2)
new_x = np.linspace(0, 16, 50)
fit = z[0] * new_x**2 + z[1] * new_x + z[2]
Cartesian(plot, new_x, fit, rangex=general_rangex, rangey=general_rangey)

# Polyfit Curve First degree
z = np.polyfit(x, y, 1)
new_x = np.linspace(0, 16, 50)
fit = z[0] * new_x + z[1]
Cartesian(plot, new_x, fit, rangex=general_rangex, rangey=general_rangey)

# Adding the Scatter Plot
Scatter(
    plot,
    x,
    y,
    rangex=general_rangex,
    rangey=general_rangey,
    pointer="triangle",
    pointer_color=0x00FFFF,
)

# Adding the labels for the Polylines
# change the x and y values to move the text according to your needs
plot.show_text(
    "Polyfit 1",
    x=300,
    y=10,
    anchorpoint=(0.5, 0.0),
    text_color=0x149F14,
    free_text=True,
)
plot.show_text(
    "Polyfit 2",
    x=72,
    y=270,
    anchorpoint=(0.0, 0.0),
    text_color=0x647182,
    free_text=True,
)
plot.show_text(
    "Polyfit 3",
    x=175,
    y=200,
    anchorpoint=(0.5, 0.0),
    text_color=0x7428EF,
    free_text=True,
)
