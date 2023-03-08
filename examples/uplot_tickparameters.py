# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from ulab import numpy as np
from circuitpython_uplot.uplot import Uplot, color
from circuitpython_uplot.ucartesian import ucartesian


# Setting up the display
display = board.DISPLAY

# Setting up the plot area
plot = Uplot(
    0,
    0,
    display.width,
    display.height,
    background_color=color.WHITE,
    box_color=color.BLACK,
)

# Setting up tick parameters
plot.tick_params(tickx_height=12, ticky_height=6, tickcolor=color.BLACK, tickgrid=False)
# Seeting some date to plot
x = np.linspace(-4, 4, num=50)
constant = 1.0 / np.sqrt(2 * np.pi)
y = constant * np.exp((-(x**2)) / 2.0)

# Drawing the graph
ucartesian(plot, x, y, line_color=color.BLACK)

# Plotting and showing the plot
display.show(plot)

# Adding some wait time
while True:
    time.sleep(1)
