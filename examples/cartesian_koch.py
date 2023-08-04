# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

# Example adapted to use in CircuitPython and Microplot from
# https://github.com/TheAlgorithms/Python/blob/master/fractals/koch_snowflake.py
# License MIT

import board
from ulab import numpy
from circuitpython_uplot.plot import Plot
from circuitpython_uplot.cartesian import Cartesian


def iterate(initial_vectors: list[numpy.ndarray], steps: int) -> list[numpy.ndarray]:
    vectors = initial_vectors
    for _ in range(steps):
        vectors = iteration_step(vectors)
    return vectors


def iteration_step(vectors: list[numpy.ndarray]) -> list[numpy.ndarray]:
    new_vectors = []
    for i, start_vector in enumerate(vectors[:-1]):
        end_vector = vectors[i + 1]
        new_vectors.append(start_vector)
        difference_vector = end_vector - start_vector
        new_vectors.append(start_vector + difference_vector / 3)
        new_vectors.append(
            start_vector + difference_vector / 3 + rotate(difference_vector / 3, 60)
        )
        new_vectors.append(start_vector + difference_vector * 2 / 3)
    new_vectors.append(vectors[-1])

    return new_vectors


def rotate(vector: numpy.ndarray, angle_in_degrees: float) -> numpy.ndarray:
    theta = numpy.radians(angle_in_degrees)
    c, s = numpy.cos(theta), numpy.sin(theta)
    rotation_matrix = numpy.array(((c, -s), (s, c)))
    return numpy.dot(rotation_matrix, vector)


# Setting up the display
display = board.DISPLAY
plot = Plot(0, 0, 200, 200, padding=0)

# initial triangle of Koch snowflake
VECTOR_1 = numpy.array([0, 0])
VECTOR_2 = numpy.array([0.5, 0.8660254])
VECTOR_3 = numpy.array([1, 0])
INITIAL_VECTORS = [VECTOR_1, VECTOR_2, VECTOR_3, VECTOR_1]
# uncomment for simple Koch curve instead of Koch snowflake
# INITIAL_VECTORS = [VECTOR_1, VECTOR_3]

# Due to memory restrictions the maximum number of iterations is 3.
processed_vectors = iterate(INITIAL_VECTORS, 3)
x_coordinates, y_coordinates = zip(*processed_vectors)

# Adding the Cartesian plot
Cartesian(plot, x_coordinates, y_coordinates)
display.show(plot)
