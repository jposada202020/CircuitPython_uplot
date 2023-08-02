# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
from ulab import numpy as np
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.cartesian import Cartesian


# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Plot(0, 0, display.width - 125, display.height, padding=25)

display.show(plot)

# Creating the values
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
y = np.array([3, 14, 23, 25, 23, 15, 9, 5, 9, 13, 17, 24, 32, 36, 46])

# Polyfit Curve third degree
z = np.polyfit(x, y, 3)
new_x = np.linspace(0, 15, 50)
fit = z[0] * new_x**3 + z[1] * new_x**2 + z[2] * new_x + z[3]
Cartesian(
    plot,
    new_x,
    fit,
    rangex=[0, 15],
    rangey=[0, 70],
    fill=True,
)
