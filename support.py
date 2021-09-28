# this file contains codes of support functions

import numpy as np
import pandas as pd
import settings


def plotting_length(dataset):
    rows = len(dataset)
    consequent_distances = np.zeros((rows))
    for i in range(1, rows):
        consequent_distances[i] = np.sqrt(
            (dataset.loc[i, 'x'] - dataset.loc[i - 1, 'x']) ** 2 + (dataset.loc[i, 'y'] - dataset.loc[i - 1, 'y']) ** 2)

    plot_length = sum(consequent_distances)
    return plot_length


def spiral_generator(a, b, center, angle_0, angle_1, nr_of_points):
    full_difference = angle_1 - angle_0
    theta = np.linspace(angle_0, angle_1, nr_of_points, endpoint=True)
    r = a + b * theta
    x = (-1) * r * np.cos(theta) + center[0]
    y = r * np.sin(theta) + center[1]
    spiral_length = b / 2 * (full_difference * np.sqrt(1 + (full_difference ** 2)) +
                             np.log(full_difference + (1 + (full_difference ** 2))))
    print("Spiral arc length = ", spiral_length)

    dataset = pd.DataFrame(columns=['x', 'y'])
    dataset['x'] = x
    dataset['y'] = y
    plot_length = plotting_length(dataset)
    print("Plot length = ", plot_length)
    return x, y


def create_spiral(center, nr_of_points):
    a, b, angle_0, angle_1 = settings.spiral_parameters()
    full_difference = angle_1 - angle_0
    x, y = spiral_generator(a, b, center, angle_0, angle_1, nr_of_points)
    # total length of the spiral
    return x, y


def get_spiral_segments(center, number_of_points, number_of_intervals):
    a, b, angle_0, angle_1 = settings.spiral_parameters()
    step_angle = (angle_1 - angle_0) / number_of_intervals
    points_per_segment = np.int(number_of_points / number_of_intervals)
    segmenting_points = pd.DataFrame(columns = ['x', 'y'])
    segmenting_points.loc[0, 'x'] = center[0]
    segmenting_points.loc[0, 'y'] = center[1]

    for i in range(0, number_of_intervals):
        angle_start = angle_0 + step_angle * i
        angle_end = angle_start + step_angle
        x, y = spiral_generator(a, b, center, angle_start, angle_end, points_per_segment)
        segmenting_points.loc[i + 1, 'x'] = x[-1]
        segmenting_points.loc[i + 1, 'y'] = y[-1]

    return segmenting_points
