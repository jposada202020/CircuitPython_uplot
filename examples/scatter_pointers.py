# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT


from random import choice
import displayio
import board
from ulab import numpy as np
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.scatter import Scatter, Pointer


# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Plot(0, 0, display.width // 2, display.height // 2, padding=1)
plot.tick_params(tickx_height=12, ticky_height=12, tickcolor=0xFF0008, tickgrid=True)
plot2 = Plot(240, 0, display.width // 2, display.height // 2, padding=1)
plot2.tick_params(tickx_height=6, ticky_height=6, tickcolor=0x939597, tickgrid=True)
plot3 = Plot(0, 160, display.width // 2, display.height // 2, padding=1)
plot3.tick_params(tickx_height=6, ticky_height=6, tickcolor=0x939597, tickgrid=False)
plot4 = Plot(240, 160, display.width // 2, display.height // 2, padding=1)
g = displayio.Group()
g.append(plot)
g.append(plot2)
g.append(plot3)
g.append(plot4)
display.show(g)
# Setting up tick parameters


a = np.linspace(1, 100)
b = [choice(a) for _ in a]
Scatter(plot, a, b)
Scatter(plot2, a, b, pointer=Pointer.TRIANGLE, pointer_color=0x00FF00)
Scatter(plot3, a, b, pointer=Pointer.SQUARE, pointer_color=0xFFFFFF)
Scatter(plot4, a, b, pointer=Pointer.DIAMOND, pointer_color=0xFF32FF)
