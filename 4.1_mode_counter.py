from csv_mode_counter import csv_mode_preprocessing

ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/' \
            '5_concatenating_all_32x32/32x32_merged.csv'

x_ordered_dict = csv_mode_preprocessing(OUTPUT_FILE=ORIG_DATA)
