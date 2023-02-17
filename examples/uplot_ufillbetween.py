# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from ulab import numpy as np
from circuitpython_uplot.uplot import Uplot
from circuitpython_uplot.ufillbetween import ufillbetween


# Setting up the display
display = board.DISPLAY

plot = Uplot(0, 0, display.width, display.height)

x = np.linspace(0, 8, num=25)

y1 = x**2 / 2
y2 = 2 + x**2 + 3 * x

ufillbetween(plot, x, y1, y2)

display.show(plot)

# Adding some wait time
while True:
    time.sleep(1)
