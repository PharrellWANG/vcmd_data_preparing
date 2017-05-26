from csv_mode_counter import csv_mode_preprocessing

# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/test_data_32x32/33_angular_modes_only_from_testing_32x32_texture_only.csv'
# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/33_angular_modes_only_from_training_32x32_texture_only.csv'
ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/33_angular_modes_train_0-32.csv'
x_ordered_dict = csv_mode_preprocessing(OUTPUT_FILE=ORIG_DATA)
