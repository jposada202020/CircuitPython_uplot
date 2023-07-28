# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

from random import choice
import board
import displayio
from ulab import numpy as np
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.bar import Bar
from circuitpython_uplot.scatter import Scatter
from circuitpython_uplot.pie import Pie
from circuitpython_uplot.cartesian import Cartesian


display = board.DISPLAY
plot = Plot(0, 0, display.width, display.height, show_box=False)

group = displayio.Group()

palette = displayio.Palette(1)
palette[0] = 0xFFFFFF


plot2 = Plot(0, 0, 130, 130)
x = np.linspace(-4, 4, num=25)
constant = 2.0 / np.sqrt(2 * np.pi)
y = constant * np.exp((-(x**2)) / 4.0)
Cartesian(plot2, x, y, rangex=[-5, 5], rangey=[0, 1])
plot.append(plot2)

plot3 = Plot(130, 0, 160, 160)

# Setting up tick parameters
plot3.tick_params(tickx_height=12, ticky_height=12, tickcolor=0xFF00FF, tickgrid=True)

# Seeting some data to plot
x = np.linspace(-4, 4, num=50)
constant = 1.0 / np.sqrt(2 * np.pi)
y = constant * np.exp((-(x**2)) / 2.0)

# Plotting and showing the plot
Cartesian(plot3, x, y, rangex=[-5, 5], rangey=[0, 0.5])
plot.append(plot3)

plot4 = Plot(290, 0, 150, 150)

# Setting up tick parameters
plot4.axs_params(axstype="box")
a = ["a", "b", "c", "d"]
b = [3, 5, 1, 7]
Bar(plot4, a, b, 0xFF1000, fill=True)

plot.append(plot4)

plot5 = Plot(0, 180, 120, 120)

# Setting up tick parameters
plot5.axs_params(axstype="cartesian")
a = np.linspace(3, 98)
b = [choice(a) for _ in a]
Scatter(plot5, a, b, rangex=[0, 102], rangey=[0, 102], radius=2)

plot.append(plot5)

plot6 = Plot(130, 160, 150, 150)

# Setting up tick parameters
plot6.axs_params(axstype="box")
a = [5, 2, 7, 3]

Pie(plot6, a, 0, 0)

plot.append(plot6)


plot7 = Plot(290, 160, 150, 150)

# Creating some points to graph
x = np.linspace(1, 10, num=10)

y = [6, 7, 9, 6, 9, 7, 6, 6, 8, 9]
Cartesian(plot7, x, y, rangex=[0, 11], rangey=[0, 12], line_color=0xFF0000, fill=True)

y = [4, 3, 7, 8, 3, 9, 3, 2, 1, 2]
Cartesian(plot7, x, y, rangex=[0, 11], rangey=[0, 12], line_color=0xFF00FF, fill=True)

y = [1, 4, 6, 3, 6, 6, 5, 0, 9, 2]
Cartesian(plot7, x, y, rangex=[0, 11], rangey=[0, 12], line_color=0x4444FF, fill=True)

plot.append(plot7)

# Plotting and showing the plot
display.show(plot)
