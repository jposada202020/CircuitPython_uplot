# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
import ulab.numpy as np
import displayio
from circuitpython_uplot.plot import Plot, color
from circuitpython_uplot.polar import Polar


# Setting up the display
display = board.DISPLAY
g = displayio.Group()

# Drawing an Ellipse
theta = np.arange(0, 2 * np.pi, 0.01)
a = 2
b = 1
r = (a * b) / np.sqrt((a * np.sin(theta)) ** 2 + (b * np.cos(theta)) ** 2)

plot = Plot(0, 0, 160, 160, padding=0, show_box=False)
Polar(plot, theta, r, rangex=[-2, 2], rangey=[-2, 2], line_color=color.ORANGE)
g.append(plot)

# Drawing an Spiral
r2 = 2 * np.pi * theta + 4.5
plot2 = Plot(0, 160, 160, 160, padding=0, show_box=False)
Polar(plot2, r2, theta, rangex=[-2, 2], rangey=[-2, 2], line_color=color.ORANGE)
g.append(plot2)

# Drawing a Star
rhos = 2 + np.cos(5 * theta)
plot3 = Plot(160, 0, 160, 160, padding=0, show_box=False)
Polar(
    plot3,
    theta,
    rhos,
    rangex=[-4, 4],
    rangey=[-4, 4],
    line_color=color.ORANGE,
    radius_ticks=[2.0, 4.0],
)
g.append(plot3)

# Drawing a more dense Spiral
rhos = (np.pi / 2) * np.cos(3 * theta)
plot5 = Plot(320, 0, 160, 160, padding=0, show_box=False)
Polar(
    plot5,
    rhos,
    theta,
    rangex=[-4, 4],
    rangey=[-4, 4],
    line_color=color.ORANGE,
    radius_ticks=[2.0, 4.0],
)
g.append(plot5)

# Drawing a funky Shape
rhos = (np.pi / 2) * theta**2
plot4 = Plot(160, 160, 160, 160, padding=0, show_box=False)
Polar(
    plot4,
    rhos,
    theta,
    rangex=[-4, 4],
    rangey=[-4, 4],
    line_color=color.ORANGE,
    radius_ticks=[2.0, 4.0],
)
g.append(plot4)

# Show the Display
display.show(g)
