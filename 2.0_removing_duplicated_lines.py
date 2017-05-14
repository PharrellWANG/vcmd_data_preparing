# from more_itertools import unique_everseen
#
# with open(inFile, 'r') as f, open(outFile, 'w') as out_file:
#     out_file.writelines(unique_everseen(f))


def duplication_remover(inFile, outFile):
    with open(inFile, 'r') as in_file, open(outFile, 'w') as out_file:
        seen = set()  # set for fast O(1) amortized lookup
        for line in in_file:
            # print("all lines: =====>   " + str(line))
            if line in seen:
                print('-----   got one -----')  # skip duplicate
                print('')
                continue

            seen.add(line)
            out_file.write(line)

list_of_input_files = [
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_balloon.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_gt_fly.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_kendo.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_newspaper.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_poznan_hall2.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_poznan_street.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_shark.csv',
                        '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/2_no_comma_32x32/no_comma_all_data_32_undo_dancer.csv'
                        ]

list_of_output_files = [
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_balloon.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_gt_fly.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_kendo.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_newspaper.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_poznan_hall2.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_poznan_street.csv',
                        # '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_shark.csv',
                        '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/3_no_duplicated_lines_32x32/no_dup_all_data_32_undo_dancer.csv'
                        ]

for x in range(len(list_of_output_files)):
    duplication_remover(list_of_input_files[x], list_of_output_files[x])
