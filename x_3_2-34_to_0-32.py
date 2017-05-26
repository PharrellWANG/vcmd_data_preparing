# import csv
import pandas as pd

input_files = [
    '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/33_angular_modes_only_from_training_32x32_texture_only.csv',
    '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/test_data_32x32/33_angular_modes_only_from_testing_32x32_texture_only.csv'
]

output_files = [
    '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/33_angular_modes_train_0-32.csv',
    '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/test_data_32x32/33_angular_modes_test_0-32.csv',
]

for file_index in range(len(input_files)):
    print("now we are reading: " + str(input_files[file_index]))
    df = pd.read_csv(input_files[file_index], header=None)

    number_of_rows = len(df.index)
    print('=======================')
    print('number_of_rows : ' + str(number_of_rows))
    print('=======================')

    cnt_37 = 0
    cnt_38 = 0

    for x in range(number_of_rows):
        if x % 1000 == 0:
            print('row index x now is : ' + str(x))
            print('---------------------------------')
        df[1025][x] -= 2
    print('=======================')
    print('')
    print('now we are writing: ' + str(output_files[file_index]) + ' . Please wait a few seconds...')
    print('............')
    df.to_csv(output_files[file_index], header=None, index=False)
