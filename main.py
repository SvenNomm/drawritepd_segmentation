
import json
import os
import pickle
import settings
import files_reader
import plot_intervals_for_verefication

test_names = settings.test_names()
test_nr = 3

number_of_intervals = 10

PATH_PD = '/Users/sven/kohalikTree/Data/MeDiag/DATA/PD/'
PATH_KT = '/Users/sven/kohalikTree/Data/MeDiag/DATA/KT/'
PATH = '/Users/sven/kohalikTree/Data/MeDiag/DATA/interval_analysis/'

collections_of_single_intervals, collections_of_cumulative_intervals = files_reader.data_loader(PATH_KT, False, False, 'mm', number_of_intervals, test_names[test_nr])
plot_intervals_for_verefication.plot_intervals(collections_of_single_intervals)
print('Thats all folks!')