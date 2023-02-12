# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: Unlicense

import time
from random import choice
import board
from ulab import numpy as np
from circuitpython_uplot.uplot import Uplot
from circuitpython_uplot.scatter import scatter


# Setting up the display
display = board.DISPLAY

plot = Uplot(0, 0, display.width, display.height)

# Setting up tick parameters
plot.tick_params(tickheight=12, tickcolor=0xFF0008, tickgrid=True)
plot.axs_params(axstype="cartesian")
a = np.linspace(1, 100)
b = [choice(a) for _ in a]
scatter(plot, a, b)

# Seeting some date to plot

# Plotting and showing the plot
display.show(plot)

# Adding some wait time
while True:
    time.sleep(1)
