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
    140,
    60,
    200,
    200,
    show_box=True,
    box_color=color.WHITE,
)

# Setting the tick parameters
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
y = [26, 32, 34, 30, 28, 35, 46, 65, 37, 23, 40, 27, 26, 36, 44, 53, 69, 27, 26]

# Creating the random numbers
random_numbers = [32, 34, 45, 65, 24, 40, 18, 27]


display.show(my_plot)
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
    limits=[30, 60],
)

# Showing the loggraph
for i in range(45):
    if dist > len(x):
        y.pop(0)
        y.append(random.choice(random_numbers))

    my_loggraph.draw_points(my_plot, x[0:dist], y[0:dist])
    display.refresh()
    dist += 1
    time.sleep(0.5)
