# SPDX-FileCopyrightText: Copyright (c) Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
import displayio
import ulab.numpy as np
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import bitmap_label
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.cartesian import Cartesian

font_file = "fonts/LeagueSpartan-Bold-16.bdf"
font_to_use = bitmap_font.load_font(font_file)

g = displayio.Group()
text = "Sin(x)"
text_area = bitmap_label.Label(font_to_use, text=text, color=0x149F14)
text_area.x = 60
text_area.y = 15
# board.DISPLAY.show(text_area)

text2 = "Cos(x)"
text2_area = bitmap_label.Label(font_to_use, text=text2, color=0x647182)
text2_area.x = 135
text2_area.y = 135

display = board.DISPLAY
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)

plot = Plot(0, 0, display.width // 2, display.height // 2, padding=1)
Cartesian(plot, x, y, rangex=[0, 10], rangey=[-1.1, 1.1])
Cartesian(plot, x, y2, rangex=[0, 10], rangey=[-1.1, 1.1])

g.append(plot)
g.append(text_area)
g.append(text2_area)

display.show(g)
