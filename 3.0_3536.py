# import csv
import pandas as pd

input_files = [
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_balloon.csv',
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_gt_fly.csv',
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_kendo.csv',
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_newspaper.csv',
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_poznan_hall2.csv',
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_poznan_street.csv',
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_shark.csv',
    '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_undo_dancer.csv'
]

output_files = [
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/4_3738_to_3536_32x32/3536_all_data_32_balloon.csv',
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/4_3738_to_3536_32x32/3536_all_data_32_gt_fly.csv',
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/4_3738_to_3536_32x32/3536_all_data_32_kendo.csv',
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/4_3738_to_3536_32x32/3536_all_data_32_newspaper.csv',
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/4_3738_to_3536_32x32/3536_all_data_32_poznan_hall2.csv',
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/4_3738_to_3536_32x32/3536_all_data_32_poznan_street.csv',
    # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/4_3738_to_3536_32x32/3536_all_data_32_shark.csv',
    '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/4_3738_to_3536_32x32/3536_all_data_32_undo_dancer.csv'
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
        if x % 10000 == 0:
            print('---------------------------------')
            # print(x % 10000)
            print('row index x now is : ' + str(x))
            print('---------------------------------')
        if df[1024][x] == 37:
            cnt_37 += 1
            # print('got one for 37 to 35: ' + str(x))
            df[1024][x] = 35
        if df[1024][x] == 38:
            cnt_38 += 1
            # print('got one for 38 to 36: ' + str(x))
            df[1024][x] = 36
    print('')
    print('=======================')
    print('cnt_37 is : ' + str(cnt_37))
    print('cnt_38 is : ' + str(cnt_38))
    print('=======================')
    print('')
    print('now we are writing: ' + str(output_files[file_index]) + ' . Please wait a few seconds...')
    print('............')
    df.to_csv(output_files[file_index], header=None, index=False)
