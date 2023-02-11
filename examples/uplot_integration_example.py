# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: Unlicense

import board
from ulab import numpy as np
from uhistogram import Histogram
from uplot import Uplot


# Setting Up the histogram
data = [5, 4, 3, 2, 7, 5, 3, 3, 3, 3, 2, 9, 7, 6]
my_box = Histogram(data, x=50, y=50, width=100, height=100)
my_box.draw()

# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Uplot(0, 0, display.width, display.height)

# Seeting some date to plot
x = np.linspace(-4, 4, num=50)
constant = 1.0 / np.sqrt(2 * np.pi)
y = constant * np.exp((-(x**2)) / 2.0)

# Plotting and showing the plot
plot.draw_plot(x, y)
plot.append(my_box)

# Adding a circle
plot.draw_circle(radius=8, x=120, y=120)

# Showing in the screen
display.show(plot)

while True:
    pass
