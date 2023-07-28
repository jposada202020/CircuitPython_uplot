# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import displayio
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.bar import Bar

# Setting up the display
display = board.DISPLAY

# Creating a group to add the two plots
group = displayio.Group()

# Creating the plot objects
plot_scale1 = Plot(0, 0, 100, 100, 1, scale=1)
plot_scale2 = Plot(125, 0, 100, 100, 1, scale=2)

# Creating the data
a = ["a", "b", "c", "d"]
b = [3, 5, 1, 7]

# Creating the bar plot
Bar(plot_scale1, a, b, 0xFF1000, True, bar_space=8, xstart=10)
Bar(plot_scale2, a, b, 0xFF1000, True, bar_space=4, xstart=5)

# Plotting and showing the plot
group.append(plot_scale1)
group.append(plot_scale2)

display.show(group)

# Adding some wait time
while True:
    time.sleep(1)
