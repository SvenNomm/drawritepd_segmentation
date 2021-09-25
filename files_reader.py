#this function warps data reading from the file, calling processing functions and returns arrays of feature values for further processing

import os
import data_reader
import settings
import segmenter_discrete
import pandas as pd


def data_loader(PATH, depict, export, units, number_of_intervals, test_name):
    subjects_list = os.listdir(PATH)
    collections_of_single_intervals = {}
    collections_of_cumulative_intervals = {}

    for subject in subjects_list:
        print(subject)

        if ('KT' in subject) or ('PD' in subject):

            path_to_subject = PATH + subject + '/'
            test_files = os.listdir(path_to_subject)

            for test_file in test_files:
                if test_name in test_file:
                    # read the data from this file
                    file_name = path_to_subject + test_file
                    print('reading data from ', file_name)
                    print('File size is', os.path.getsize(file_name))

                    # compute features and add to the corresponding vector

                    test_data = data_reader.data_reader(file_name)
                    collections_of_single_intervals[subject], collections_of_cumulative_intervals[subject] = segmenter_discrete.segmenter_discrete(test_data, number_of_intervals, units)

    return collections_of_single_intervals, collections_of_cumulative_intervals
