# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from adafruit_display_shapes.polygon import Polygon
from adafruit_display_shapes.roundrect import RoundRect
from circuitpython_uplot.uplot import Uplot

# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Uplot(0, 0, display.width, display.height)

# Setting up tick parameters
plot.tick_params(tickx_height=12, ticky_height=12, tickcolor=0xFF0008, tickgrid=True)
plot.axs_params(axstype="box")

# Creating some shapes to show
polygon = Polygon(
    [
        (255, 40),
        (262, 62),
        (285, 62),
        (265, 76),
        (275, 100),
        (255, 84),
        (235, 100),
        (245, 76),
        (225, 62),
        (248, 62),
    ],
    outline=0x0000FF,
)

roundrect = RoundRect(30, 30, 61, 81, 10, fill=0x0, outline=0xFF00FF, stroke=6)

# Adding shapes to the plot
plot.append(polygon)
plot.append(roundrect)

# Plotting and showing the plot
display.show(plot)

# Adding some wait time
while True:
    time.sleep(1)
