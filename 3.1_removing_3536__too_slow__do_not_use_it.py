# import csv
import pandas as pd

input_files = [
    '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/training_32x32_equal.csv'
]

output_files = [
    '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/training_32x32_equal_without_3536.csv'
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
        if x % 10 == 0:
            print('---------------------------------')
            # print(x % 10000)
            print('row index x now is : ' + str(x))
        if df[1025][x] == 35 or df[1025][x] == 36:
            print('now drop row: ' + str(x))
            df.drop(df.index[[x, ]])
    print('')
    print('=======================')
    print('')
    print('now we are writing: ' + str(output_files[file_index]) + ' . Please wait a few seconds...')
    print('............')
    df.to_csv(output_files[file_index], header=None, index=False)
    print('Done. Congrats.')
