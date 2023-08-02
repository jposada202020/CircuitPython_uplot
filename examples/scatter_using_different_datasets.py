# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

from random import choice
import board
from ulab import numpy as np
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.scatter import Scatter, Pointer


# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Plot(0, 0, display.width, display.height, padding=25)
plot.tick_params(
    tickx_height=12,
    ticky_height=12,
    tickcolor=0x939597,
    tickgrid=True,
    showtext=True,
    decimal_points=0,
)

display.show(plot)

a = np.linspace(4, 200, 50)
z = [4, 5, 6, 7, 8]
radi = [choice(z) for _ in a]
b = [choice(a) for _ in a]
Scatter(
    plot, a, b, rangex=[0, 210], rangey=[0, 210], radius=radi, pointer_color=0xF456F3
)
a = np.linspace(50, 170, 50)
radi = [choice(z) for _ in a]
b = [choice(a) for _ in a]
Scatter(
    plot, a, b, rangex=[0, 210], rangey=[0, 210], radius=radi, pointer_color=0x00FF00
)
a = np.linspace(50, 100, 25)
z = [
    4,
    5,
    6,
]
radi = [choice(z) for _ in a]
b = [int(choice(a) / 1.2) for _ in a]
Scatter(
    plot,
    a,
    b,
    rangex=[0, 210],
    rangey=[0, 210],
    pointer=Pointer.TRIANGLE,
    pointer_color=0x00FFFF,
)
