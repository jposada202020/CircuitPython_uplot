# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

from random import choice
import board
from ulab import numpy as np
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.scatter import Scatter


# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Plot(0, 0, display.width, display.height, padding=1)
plot.tick_params(tickx_height=12, ticky_height=12, tickcolor=0x939597, tickgrid=True)

display.show(plot)

a = np.linspace(1, 200, 150)
z = [4, 5, 6, 7, 8]
radi = [choice(z) for _ in a]
b = [choice(a) for _ in a]
Scatter(
    plot, a, b, rangex=[0, 210], rangey=[0, 210], radius=radi, pointer_color=0xF456F3
)
