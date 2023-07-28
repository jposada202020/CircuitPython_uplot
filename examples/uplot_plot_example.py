# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from ulab import numpy as np
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.cartesian import Cartesian

# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Plot(0, 0, display.width, display.height)

# Creating some points to graph
x = np.linspace(-4, 4, num=25)
constant = 1.0 / np.sqrt(2 * np.pi)
y = constant * np.exp((-(x**2)) / 2.0)

# Drawing the graph
Cartesian(plot, x, y)

display.show(plot)
while True:
    time.sleep(1)
