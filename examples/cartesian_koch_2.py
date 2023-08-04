# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
# pylint: disable=unused-argument, use-dict-literal
# Example adapted to use in CircuitPython and Microplot from
# Heltonbiker
# https://stackoverflow.com/questions/7409938/fractal-koch-curve

import math
import board
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.cartesian import Cartesian

angles = [math.radians(60 * x) for x in range(6)]
sines = [math.sin(x) for x in angles]
cosin = [math.cos(x) for x in angles]


def L(angle, coords, jump):
    return (angle + 1) % 6


def R(angle, coords, jump):
    return (angle + 4) % 6


def F(angle, coords, jump):
    coords.append(
        (coords[-1][0] + jump * cosin[angle], coords[-1][1] + jump * sines[angle])
    )
    return angle


decode = dict(L=L, R=R, F=F)


def koch(steps, length=200, startPos=(0, 0)):
    pathcodes = "F"
    for _ in range(steps):
        pathcodes = pathcodes.replace("F", "FLFRFLF")

    jump = float(length) / (3**steps)
    coords = [startPos]
    angle = 0

    for move in pathcodes:
        angle = decode[move](angle, coords, jump)

    return coords


TOTALWIDTH = 300
display = board.DISPLAY
plot = Plot(0, 0, display.width, display.height, padding=0)
points = koch(5, TOTALWIDTH, (-TOTALWIDTH / 2, 0))
x_coordinates, y_coordinates = zip(*points)

# Adding the Cartesian plot
Cartesian(plot, x_coordinates, y_coordinates)
display.show(plot)
