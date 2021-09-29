# this function plots intervals just to verify  segmentation

import pandas as pd
import matplotlib.pyplot as plt


def plot_intervals(collection_of_intervals):
    keys = list(collection_of_intervals)
    for i in keys:
        segments = collection_of_intervals[i]
        number_of_intervals = len(segments)
        for j in range(0, number_of_intervals):
            segment = segments[j]
            if segment.empty:
                print('segment', j, "is empty")
            else:
                plt.close('all')
                fig1, axis = plt.subplots()
                plt.plot(segment['x'],segment['y'])
                plt.show()
