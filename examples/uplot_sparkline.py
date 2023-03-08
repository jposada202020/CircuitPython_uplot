# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from ulab import numpy as np
from adafruit_display_shapes.sparkline import Sparkline
from circuitpython_uplot.uplot import Uplot, color


# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Uplot(0, 0, display.width, display.height)

# 500 linearly spaced numbers
x = np.linspace(-10 * np.pi, 10 * np.pi, 500)

# the function, which is y = sin(x) here
y = np.sin(x)

# Creating the sparkline
sparkline = Sparkline(
    width=200,
    height=200,
    max_items=80,
    y_min=np.min(y),
    y_max=np.max(y),
    x=100,
    y=40,
    color=color.TEAL,
)

# Adding shapes to the plot
plot.append(sparkline)

# Plotting and showing the plot
display.show(plot)

for element in y:
    display.auto_refresh = False
    sparkline.add_value(element)
    display.auto_refresh = True

    time.sleep(0.1)
