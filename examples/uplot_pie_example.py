# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.pie import upie


# Setting up the display
display = board.DISPLAY

plot = Plot(0, 0, display.width, display.height)

# Setting up tick parameters
plot.axs_params(axstype="box")
a = [5, 2, 7, 3]

upie(plot, a)

# Plotting and showing the plot
display.show(plot)

# Adding some wait time
while True:
    time.sleep(1)
