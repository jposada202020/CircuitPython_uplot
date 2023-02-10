# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: Unlicense

import board
import displayio
import time
import vectorio
from uplot import Uplot

display = board.DISPLAY
plot = Uplot(0, 0, display.width, display.height)
print(plot.width)
print(plot.height)


group = displayio.Group()

palette = displayio.Palette(1)
palette[0] = 0xFFFFFF

circle = vectorio.Circle(pixel_shader=palette, radius=5, x=10, y=10)
plot.append(circle)


display.show(plot)
while True:
    time.sleep(1)
