# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
import ulab.numpy as np
from circuitpython_uplot.plot import Plot, color
from circuitpython_uplot.polar import Polar

# Setting up the display
display = board.DISPLAY
plot = Plot(10, 10, 250, 250, padding=0, show_box=False)

# Creating the data
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

# Plotting and showing the plot
Polar(plot, theta, r, rangex=[-2, 2], rangey=[-2, 2], line_color=color.ORANGE)
display.show(plot)
