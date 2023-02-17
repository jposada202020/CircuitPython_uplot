# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from circuitpython_uplot.uplot import Uplot

# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Uplot(0, 0, display.width, display.height)

plot.draw_circle(radius=8, x=120, y=120)

display.show(plot)

while True:
    time.sleep(1)
