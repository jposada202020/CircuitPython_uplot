# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
from ulab import numpy as np
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.cartesian import Cartesian

# Setting up the display
display = board.DISPLAY
plot = Plot(0, 0, display.width, display.height)

# Creating some points to graph
x = np.linspace(-4, 4, num=25)
constant = 1.0 / np.sqrt(2 * np.pi)
y = constant * np.exp((-(x**2)) / 2.0)

# Drawing the graph
Cartesian(
    plot, x, y, rangex=[-5, 5], rangey=[0, 1], line_color=0xFF0000, line_style="- -"
)

# Creating some points to graph
x = np.linspace(-3, 3, num=50)
constant = 2.0 / np.sqrt(2 * np.pi)
y = constant * np.exp((-(x**2)) / 2.0)
Cartesian(
    plot, x, y, rangex=[-5, 5], rangey=[0, 1], line_color=0x00FF00, line_style="."
)


x = np.linspace(-4, 4, num=50)
constant = 2.5 / np.sqrt(2 * np.pi)
y = constant * np.exp((-(x**2)) / 6.5)
Cartesian(
    plot, x, y, rangex=[-5, 5], rangey=[0, 1], line_color=0x123456, line_style="-.-"
)

# Plotting and showing the plot
display.show(plot)
