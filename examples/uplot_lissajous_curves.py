# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import math
import board
import displayio
from circuitpython_uplot.uplot import Uplot, color
from circuitpython_uplot.ucartesian import ucartesian

# Inspired by Paul McWhorter Raspberry Pi Pico W LESSON 27: Creating Lissajous Patterns
# on an OLED Display
# And
# https://storm-coder-dojo.github.io/activities/python/curves.html


def create_curve(a=1, b=2, mul_factor=10, delta=3.14 / 2):
    """
    Creates a curve based on the formula
    adapted from https://github.com/JPBotelho/Lissajous-Curve
    Liscense: MIT
    """
    delta = 3.14 / 2
    xvalues = []
    yvalues = []
    for i in range(0, 315):
        t = i * 0.02
        x = mul_factor * math.cos(t * a + delta)
        y = mul_factor * math.sin(t * b)
        xvalues.append(x)
        yvalues.append(y)
        if abs(x - xvalues[0]) + abs(y - yvalues[0]) < 0.01 and i > 1:
            print("iterated " + str(i) + " points")
            break
    return xvalues, yvalues


# Setting up the display
display = board.DISPLAY
plot = Uplot(0, 0, display.width // 2, display.height // 2, padding=1)
plot2 = Uplot(240, 0, display.width // 2, display.height // 2, padding=1)
plot3 = Uplot(0, 160, display.width // 2, display.height // 2, padding=1)
plot4 = Uplot(240, 160, display.width // 2, display.height // 2, padding=1)
g = displayio.Group()
g.append(plot)
g.append(plot2)
g.append(plot3)
g.append(plot4)

# Plotting and showing the plot
display.show(g)


# Some Variables
factor = 10
separation = 2

# Creating the Plots
x_number_list, y_number_list = create_curve(1, 2, 10)
ucartesian(
    plot,
    x_number_list,
    y_number_list,
    rangex=[-factor - separation, factor + separation],
    rangey=[-factor - separation, factor + separation],
    line_color=color.GRAY,
)

x_number_list, y_number_list = create_curve(3, 2, 10)
ucartesian(
    plot2,
    x_number_list,
    y_number_list,
    rangex=[-factor - separation, factor + separation],
    rangey=[-factor - separation, factor + separation],
    line_color=color.YELLOW,
)

x_number_list, y_number_list = create_curve(3, 4, 10)
ucartesian(
    plot3,
    x_number_list,
    y_number_list,
    rangex=[-factor - separation, factor + separation],
    rangey=[-factor - separation, factor + separation],
    line_color=color.TEAL,
)

x_number_list, y_number_list = create_curve(5, 4, 10)
ucartesian(
    plot4,
    x_number_list,
    y_number_list,
    rangex=[-factor - separation, factor + separation],
    rangey=[-factor - separation, factor + separation],
    line_color=color.ORANGE,
)
