# this function segments the test into the intervals
import settings
import noise_filter
import pandas as pd


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
