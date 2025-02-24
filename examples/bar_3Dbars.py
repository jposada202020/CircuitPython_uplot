# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.bar import Bar


# Setting up the display
display = board.DISPLAY

plot = Plot(0, 0, display.width, display.height)

# Setting up tick parameters
plot.axs_params(axstype="box")
a = ["a", "b", "c", "d", "e"]
b = [3, 5, 1, 9, 7]

# Creating a 3D bar
Bar(
    plot,
    a,
    b,
    color=0xFF1000,
    fill=True,
    bar_space=30,
    xstart=70,
    projection=True,
)

# Plotting and showing the plot
display.root_group = plot
