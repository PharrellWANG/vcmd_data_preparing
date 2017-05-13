import csv

input_files = [
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_no_duplication_now/training_data_16_kendo.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_no_duplication_now/training_data_16_balloon.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_no_duplication_now/training_data_16_gt_fly.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_no_duplication_now/training_data_16_newspaper.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_no_duplication_now/training_data_16_poznan_hall2.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_no_duplication_now/training_data_16_poznan_street.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_no_duplication_now/training_data_16_shark.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_no_duplication_now/training_data_16_undo_dancer.csv']

output_files = [
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_3536/training_data_16_kendo.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_3536/training_data_16_balloon.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_3536/training_data_16_gt_fly.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_3536/training_data_16_newspaper.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_3536/training_data_16_poznan_hall2.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_3536/training_data_16_poznan_street.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_3536/training_data_16_shark.csv',
    '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_3536/training_data_16_undo_dancer.csv']

for file_index in range(len(input_files)):
    r = csv.reader(open(input_files[file_index]))  # Here your csv file
    data = list(r)
    row_count = len(data)
    print(row_count)

    lines = [l for l in r]
    print(lines[1])
    # print(len(lines))
    print(lines[1][257])
    # print(type(lines[10][257]))

    for i in range(row_count):

        if int(lines[i][257]) == 37:
            lines[i][257] = str(35)
        elif int(lines[i][257]) == 38:
            lines[i][257] = str(36)
    writer = csv.writer(open(output_files[file_index], 'w'))
    writer.writerows(lines)
