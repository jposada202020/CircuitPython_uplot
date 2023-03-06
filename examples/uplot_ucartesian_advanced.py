# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from ulab import numpy as np
from circuitpython_uplot.uplot import Uplot
from circuitpython_uplot.ucartesian import ucartesian

# Setting up the display
display = board.DISPLAY
plot = Uplot(0, 0, display.width, display.height)

# Creating some points to graph
x = np.linspace(-4, 4, num=25)
constant = 1.0 / np.sqrt(2 * np.pi)
y = constant * np.exp((-(x**2)) / 2.0)

# Drawing the graph
ucartesian(plot, x, y, rangex=[-5, 5], rangey=[0, 1], line_color=0xFF0000)

# Creating some points to graph
x = np.linspace(-3, 3, num=50)
constant = 2.0 / np.sqrt(2 * np.pi)
y = constant * np.exp((-(x**2)) / 2.0)
ucartesian(plot, x, y, rangex=[-5, 5], rangey=[0, 1], line_color=0x00FF00)

# Plotting and showing the plot
display.show(plot)

# Adding some wait time
while True:
    time.sleep(1)
