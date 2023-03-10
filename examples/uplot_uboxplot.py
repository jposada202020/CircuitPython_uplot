# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
Simple test to display boxplot using uplot
"""

import board
from uboxplot import Boxplot
from circuitpython_uplot.uplot import Uplot


display = board.DISPLAY

plot = Uplot(0, 0, display.width, display.height)

plot.tick_params(tickx_height=10, ticky_height=10, tickcolor=0x440008, tickgrid=True)

a = [1, 1, 4, 5, 6, 7, 7, 7, 8, 9, 10, 15, 16, 17, 24, 56, 76, 87, 87]
my_box = Boxplot(a, x=50, y=50, height=100, line_color=0xFF00FF)
my_box.draw()

b = [1, 1, 4, 5, 6, 7, 7, 7, 8, 9, 10, 15, 16, 17, 24]
my_box2 = Boxplot(b, x=90, y=90, height=100, line_color=0x0000FF)
my_box2.draw()

c = [
    1,
    1,
    4,
    5,
    6,
    7,
    7,
    7,
    8,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    9,
    10,
    15,
    15,
    15,
    15,
    16,
    16,
    17,
    23,
    28,
    39,
    41,
    41,
    41,
    43,
]
my_box3 = Boxplot(c, x=150, y=50, height=100, line_color=0x1CFF11)
my_box3.draw()

plot.append(my_box)
plot.append(my_box2)
plot.append(my_box3)
display.show(plot)

while True:
    pass
