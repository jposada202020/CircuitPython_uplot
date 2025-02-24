# SPDX-FileCopyrightText: Copyright (c) Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import random
import board
from circuitpython_uplot.plot import Plot, color
from circuitpython_uplot.logging import Logging

# Setting up the display
display = board.DISPLAY
display.auto_refresh = False

# Drawing the graph
my_plot = Plot(
    5,
    5,
    480,
    300,
    padding=20,
    show_box=True,
    box_color=color.WHITE,
)

# Setting the tick parameters
my_plot.tick_params(
    tickx_height=4,
    ticky_height=4,
    show_ticks=True,
    tickcolor=color.TEAL,
    tickgrid=True,
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
y = [26, 22, 24, 30, 28, 35, 26, 25, 24, 23, 20, 27, 26, 33, 24, 23, 19, 27, 26]

# Creating the random numbers
random_numbers = [19, 22, 35, 33, 24, 26, 28, 37]


display.root_group = my_plot
display.refresh()

dist = 1

# Creating the loggraph
my_loggraph = Logging(
    my_plot,
    x[0:dist],
    y[0:dist],
    rangex=[0, 210],
    rangey=[0, 110],
    line_color=color.BLUE,
    ticksx=[25, 50, 75, 100, 125, 150, 175, 200],
    ticksy=[25, 50, 75, 100],
    fill=False,
)

# Showing the loggraph
for _ in range(20):
    if dist > len(x):
        y.pop(0)
        y.append(random.choice(random_numbers))

    my_loggraph.draw_points(my_plot, x[0:dist], y[0:dist])
    display.refresh()
    dist += 1
    time.sleep(0.5)
