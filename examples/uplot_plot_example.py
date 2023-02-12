# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: Unlicense

import time
import board
from ulab import numpy as np
from circuitpython_uplot.uplot import Uplot

display = board.DISPLAY
plot = Uplot(0, 0, display.width, display.height)


x = np.linspace(-4, 4, num=25)

constant = 1.0 / np.sqrt(2 * np.pi)
y = constant * np.exp((-(x**2)) / 2.0)


plot.draw_plot(x, y)

display.show(plot)
while True:
    time.sleep(1)
