# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from ulab import numpy as np
from circuitpython_uplot.uplot import Uplot
from circuitpython_uplot.umap import umap


# Setting up the display
display = board.DISPLAY

# Adding the plot area
plot = Uplot(0, 0, display.width, display.height, show_box=False)

# Setting some date to plot
x = np.array(
    [
        [1, 3, 9, 25],
        [12, 8, 4, 2],
        [18, 3, 7, 5],
        [2, 10, 9, 22],
        [8, 8, 14, 12],
        [3, 13, 17, 15],
    ],
    dtype=np.int16,
)

# Plotting and showing the plot
umap(plot, x, 0xFF0000, 0x0000FF)

# Plotting and showing the plot
display.show(plot)

# Adding some wait time
while True:
    time.sleep(1)
