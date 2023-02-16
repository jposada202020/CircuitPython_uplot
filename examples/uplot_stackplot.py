# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
Example to show how to draw stackplots
"""

import time
import board
from ulab import numpy as np
from circuitpython_uplot.uplot import Uplot
from circuitpython_uplot.ucartesian import ucartesian

# Setting up the display
display = board.DISPLAY
plot = Uplot(0, 0, display.width, display.height)

# Creating some points to graph
x = np.linspace(1, 10, num=10)

y = [6, 7, 9, 6, 9, 7, 6, 6, 8, 9]
ucartesian(plot, x, y, rangex=[0, 11], rangey=[0, 12], line_color=0xFF0000, fill=True)

y = [4, 3, 7, 8, 3, 9, 3, 2, 1, 2]
ucartesian(plot, x, y, rangex=[0, 11], rangey=[0, 12], line_color=0xFF00FF, fill=True)

y = [1, 4, 6, 3, 6, 6, 5, 0, 9, 2]
ucartesian(plot, x, y, rangex=[0, 11], rangey=[0, 12], line_color=0x4444FF, fill=True)


display.show(plot)

while True:
    time.sleep(1)
