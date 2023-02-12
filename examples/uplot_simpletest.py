# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: Unlicense

import time
import board
import displayio
from circuitpython_uplot.uplot import Uplot

display = board.DISPLAY
plot = Uplot(0, 0, display.width, display.height)

group = displayio.Group()

palette = displayio.Palette(1)
palette[0] = 0xFFFFFF

plot.draw_circle(radius=8, x=120, y=120)

display.show(plot)
while True:
    time.sleep(1)
