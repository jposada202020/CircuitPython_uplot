# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
import displayio
import ulab.numpy as np
from circuitpython_uplot.plot import Plot, color
from circuitpython_uplot.cartesian import Cartesian

# Inspired by
# https://github.com/CodeDrome/polar-plots-python

# pylint: disable=dangerous-default-value
# Setting up the display
display = board.DISPLAY
plot = Plot(0, 0, display.width // 2, display.height // 2, padding=1)
plot2 = Plot(240, 0, display.width // 2, display.height // 2, padding=1)
plot3 = Plot(0, 160, display.width // 2, display.height // 2, padding=1)
plot4 = Plot(240, 160, display.width // 2, display.height // 2, padding=1)
g = displayio.Group()
g.append(plot)
g.append(plot2)
g.append(plot3)
g.append(plot4)

# Plotting and showing the plot
display.show(g)


def rose_function(n=3, angle_range=[0, 360], radius=30):
    """
    Rose function
    :param int n: Node number. Defaults to 3
    :param list angle_range: angle range to be plot. Defaults to [0, 360]
    :param int radius: radius of the rose function. Defatuls to 30
    """
    test = np.linspace(angle_range[0], angle_range[1], angle_range[1] - angle_range[0])
    radians = np.radians(test)

    return (
        np.cos(radians) * np.sin(radians * n) * radius,
        np.sin(radians) * np.sin(radians * n) * radius,
    )


def spiral_function(a=1, b=3, angle_range=[0, 720]):
    """
    Spiral Graph
    :param int a: spiral's rotation. Defaults to 1
    :param int b: distance between the lines. Defaults to 3
    :param list angle_range: angle range to be plot. Defaults: [0, 720]
    """

    test = np.linspace(angle_range[0], angle_range[1], angle_range[1] - angle_range[0])
    radians = np.radians(test)

    distance = a + b * radians

    return np.cos(radians) * distance, np.sin(radians) * distance


def cardioid_function(angle_range=[0, 360], radius=35):
    """
    Cardiod Function
    :param list angle_range: angle range to be plot. Defaults: [0, 360]
    :param int radius: Radius of the cardiod plot

    """
    test = np.linspace(angle_range[0], angle_range[1], angle_range[1] - angle_range[0])
    radians = np.radians(test)
    distance = (1 + np.cos(radians)) * radius

    return np.cos(radians) * distance, np.sin(radians) * distance


def circle_function(angle_range=[0, 360], radius=35):
    """
    Circle function
    :param list angle_range: angle range to be plot. Defaults: [0, 360]
    :param int radius: Radius of the cardiod plot
    """
    test = np.linspace(angle_range[0], angle_range[1], angle_range[1] - angle_range[0])
    radians = np.radians(test)
    return np.cos(radians) * radius, np.sin(radians) * radius


x, y = rose_function(n=3, angle_range=[0, 360], radius=35)
Cartesian(plot, x, y, rangex=[-40, 40], rangey=[-40, 40], line_color=0xE30B5D)

x, y = spiral_function(a=1, b=3, angle_range=[0, 900])
Cartesian(plot2, x, y, rangex=[-50, 50], rangey=[-50, 50], line_color=color.YELLOW)

x, y = cardioid_function(angle_range=[0, 360], radius=35)
Cartesian(plot3, x, y, rangex=[-15, 75], rangey=[-50, 50], line_color=color.TEAL)

x, y = circle_function(angle_range=[0, 360], radius=35)
Cartesian(plot4, x, y, rangex=[-40, 40], rangey=[-40, 40], line_color=color.ORANGE)
