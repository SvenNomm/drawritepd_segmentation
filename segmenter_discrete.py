# this function segments the test into the intervals
import numpy as np

import settings
import noise_filter
import pandas as pd
import json
import matplotlib.pyplot as plt
import support


def segmenter_discrete(dataset, number_of_intervals, units):
    # based on the screen resolution perform drawing segmentation
    screen_x_max, screen_y_max = settings.screen_resolution()
    interval_length = screen_x_max / number_of_intervals

    single_intervals = {}
    cumulative_intervals = {}

    for i in range(0, number_of_intervals):
        single_intervals[i] = pd.DataFrame()
        cumulative_intervals[i] = pd.DataFrame()

    for i in range(0, number_of_intervals):
        interval_min = i * interval_length
        interval_max = interval_min + interval_length
        interval_data_cumulative = dataset.loc[dataset['x'] < interval_max]
        interval_data_single = interval_data_cumulative.loc[interval_data_cumulative['x'] > interval_min]

        cumulative_intervals[i] = noise_filter.noise_filter(interval_data_cumulative)
        single_intervals[i] = noise_filter.noise_filter(interval_data_single)

    return single_intervals, cumulative_intervals


def plotting_length_based_segmentation(dataset, nr_of_segments):
    rows = len(dataset)
    consequent_distances = np.zeros(rows)
    for i in range(1, rows):
        print(i)
        if i == 1:
            print("fff", dataset.loc[i, 'x'], "fff",dataset.loc[i - 1, 'x'], "fff", dataset.loc[i, 'y'], "fff", dataset.loc[i - 1, 'y'])
        consequent_distances[i] = np.sqrt(
            (dataset.loc[i, 'x'] - dataset.loc[i - 1, 'x']) ** 2 + (dataset.loc[i, 'y'] - dataset.loc[i - 1, 'y']) ** 2)

    plot_length = sum(consequent_distances)
    segment_length = plot_length / nr_of_segments
    segmenting_points = pd.DataFrame(columns=['idx','x', 'y'])
    #segmenting_points = np.zeros((nr_of_segments+1, 2))
    segmenting_points.loc[0, 'x'] = dataset.loc[0, 'x']
    segmenting_points.loc[0, 'y'] = dataset.loc[0, 'y']
    segmenting_points.loc[0, 'idx'] = 0
    k = 1 # index of segmenting points
    current_segment_length = 0
    for i in range(1, rows):
        current_segment_length = current_segment_length + consequent_distances[i]
        if current_segment_length >= segment_length:
            print("Current segment length = ", current_segment_length)
            current_segment_length = 0
            segmenting_points.loc[k, 'x'] = dataset.loc[i, 'x']
            segmenting_points.loc[k, 'y'] = dataset.loc[i, 'y']
            segmenting_points.loc[k, 'idx'] = i
            k = k + 1
    # just in case be sure that we have last point as well
    segmenting_points.loc[k+1, 'x'] = dataset.loc[rows-1, 'x']
    segmenting_points.loc[k+1, 'y'] = dataset.loc[rows-1, 'y']
    segmenting_points.loc[k+1, 'idx'] = rows-1

    single_intervals = {}
    cumulative_intervals = {}

    for i in range(0, nr_of_segments):
        single_intervals[i] = pd.DataFrame()
        cumulative_intervals[i] = pd.DataFrame()

    for i in range(1, nr_of_segments):
        interval_data_single = dataset.loc[segmenting_points.loc[i - 1, 'idx']:segmenting_points.loc[i, 'idx'], :]
        interval_data_cumulative = dataset.loc[0:segmenting_points.loc[i, 'idx'], :]

        cumulative_intervals[i] = noise_filter.noise_filter(interval_data_cumulative)
        single_intervals[i] = noise_filter.noise_filter(interval_data_single)

    return segmenting_points, cumulative_intervals, single_intervals


def spiral_segmenter_discrete(dataset, number_of_segments, units):
    # based on the screen resolution perform drawing segmentation

    screen_x_max, screen_y_max = settings.screen_resolution()
    #interval_length = screen_x_max / number_of_intervals

    single_intervals = {}
    cumulative_intervals = {}

    # this part is for testing and verification purposes
    PATH_to_ref = '/Users/sven/kohalikTree/Data/MeDiag/reference-shapes/'
    ref_file_name = PATH_to_ref + 'spiral.json'
    with open(ref_file_name) as reference_file:
        ref_data = json.load(reference_file)

        for j in ref_data['data']:
            ref_pattern = pd.DataFrame(j)

    number_of_points = len(ref_pattern)
    print("number_of_points = ", number_of_points)
    center = [ref_pattern.loc[0,'x'], ref_pattern.loc[0,'y']]
    x, y = support.create_spiral(center, number_of_points)
    #segmenting_points = support.get_spiral_segments(center, number_of_points, number_of_intervals)
    segmenting_points, cumulative_intervals, single_intervals = plotting_length_based_segmentation(dataset, number_of_segments)
    print(center)
    fig, axs = plt.subplots()
    plt.plot(dataset['x'], dataset['y'] * (-1), linewidth=5, color='gold', alpha=0.7)
    #plt.plot(x, y * (-1), linewidth=5, color='red', alpha=0.7)
    plt.scatter(segmenting_points['x'], segmenting_points['y'] * (-1), s=20, c='red', marker='*')
    plt.plot(ref_pattern['x'], ref_pattern['y'] * (-1), linewidth=1, color='blue', alpha=1)
    plt.axis('equal')
    plt.show()
    return cumulative_intervals, single_intervals

