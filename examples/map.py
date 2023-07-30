# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from random import choice
import board
from ulab import numpy as np
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.map import Map


# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Plot(0, 0, display.width, display.height, show_box=False)

# Setting some date to plot
x = np.linspace(-4, 4, num=100)
y = 2.0 / np.sqrt(2 * np.pi) * np.exp((-(x**2)) / 4.0)
b = [choice(y) for _ in y]
y1 = np.array(b).reshape((10, 10))

# Plotting and showing the plot
Map(plot, y1, 0xFF0044, 0x4400FF)
# Plotting and showing the plot
display.show(plot)

# Adding some wait time
while True:
    time.sleep(1)
