# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from random import choice
import board
from ulab import numpy as np
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.scatter import Scatter


# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Plot(0, 0, display.width, display.height)

# Setting up tick parameters
plot.tick_params(tickx_height=12, ticky_height=12, tickcolor=0xFF0008, tickgrid=True)
plot.axs_params(axstype="cartesian")
a = np.linspace(1, 100)
b = [choice(a) for _ in a]
Scatter(plot, a, b)

# Plotting and showing the plot
display.show(plot)

# Adding some wait time
while True:
    time.sleep(1)
