# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
from ulab import numpy as np
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.fillbetween import Fillbetween


# Setting up the display
display = board.DISPLAY

plot = Plot(0, 0, display.width, display.height)

x = np.linspace(0, 8, num=25)

y1 = x**2 / 2
y2 = 2 + x**2 + 3 * x

Fillbetween(plot, x, y1, y2)

display.root_group = plot
