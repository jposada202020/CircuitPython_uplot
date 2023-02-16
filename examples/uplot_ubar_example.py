# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from circuitpython_uplot.uplot import Uplot
from circuitpython_uplot.ubar import ubar


# Setting up the display
display = board.DISPLAY

plot = Uplot(0, 0, display.width, display.height)

# Setting up tick parameters
plot.axs_params(axstype="box")
a = ["a", "b", "c", "d"]
b = [3, 5, 1, 7]
ubar(plot, a, b, 0xFF1000, True)

# Plotting and showing the plot
display.show(plot)

# Adding some wait time
while True:
    time.sleep(1)
