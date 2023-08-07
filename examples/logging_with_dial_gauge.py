# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import random
import board
import displayio
from dial_gauge import DIAL_GAUGE
from circuitpython_uplot.plot import Plot, color
from circuitpython_uplot.logging import Logging


# In order to run this example you need to install the following library:
# - CircuitPython_DIAL_GAUGE (from https://github.com/jposada202020/CircuitPython_DIAL_GAUGE)

rangey_values = [0, 110]

display = board.DISPLAY
display.auto_refresh = False
my_plot = Plot(0, 0, display.width // 2, display.height // 2)
plot2 = Plot(display.width // 2, 0, display.width // 2, display.height // 2)

my_dial = DIAL_GAUGE(60, 50, 60, 40, range_values=rangey_values, color=color.BLUE)

plot2.append(my_dial)

g = displayio.Group()
g.append(my_plot)
g.append(plot2)
display.show(g)


my_plot.tick_params(
    tickx_height=4,
    ticky_height=4,
    show_ticks=True,
    tickcolor=color.TEAL,
    showtext=True,
)

# Creating the x and y data
x = [
    10,
    20,
    30,
    40,
    50,
    60,
    70,
    80,
    90,
    100,
    110,
    120,
    130,
    140,
    150,
    160,
    170,
    180,
    190,
]
y = []

# Creating the random numbers
random_numbers = [32, 34, 45, 65, 24, 40, 18, 27]


# display.show(my_plot)
display.refresh()

dist = 0

# Creating the loggraph
my_loggraph = Logging(
    my_plot,
    x[0:dist],
    y[0:dist],
    rangex=[0, 210],
    rangey=rangey_values,
    line_color=color.BLUE,
    ticksx=[25, 50, 75, 100, 125, 150, 175, 200],
    ticksy=[25, 50, 75, 100],
    limits=[30, 60],
)

# Showing the loggraph
for i in range(150):
    if dist > len(x):
        y.pop(0)

    update_value = random.choice(random_numbers)
    y.append(update_value)

    my_loggraph.draw_points(my_plot, x[0:dist], y[0:dist])

    if dist > len(x):
        my_dial.update(update_value)
    else:
        my_dial.update(y[i])
    display.refresh()
    dist += 1
    time.sleep(0.5)
