# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from ulab import numpy as np
from circuitpython_uplot.uplot import Uplot

# Setting up the display
display = board.DISPLAY

# Setting up the plot area
plot = Uplot(0, 0, display.width, display.height)

# Setting up tick parameters
plot.tick_params(tickheight=12, tickcolor=0xFF00FF, tickgrid=True)

# Seeting some date to plot
x = np.linspace(-4, 4, num=50)
constant = 1.0 / np.sqrt(2 * np.pi)
y = constant * np.exp((-(x**2)) / 2.0)

# Plotting and showing the plot
plot.draw_plot(x, y)
display.show(plot)

# Adding some wait time
while True:
    time.sleep(1)
