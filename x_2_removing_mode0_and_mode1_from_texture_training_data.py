# inFile = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/training_32x32_texture_only.csv'
inFile = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/test_data_32x32/testing_32x32_texture_only.csv'

# outFile = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/train_data_32x32/33_angular_modes_only_from_training_32x32_texture_only.csv'
outFile = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/test_data_32x32/33_angular_modes_only_from_testing_32x32_texture_only.csv'


def separate_texture_depth(a, b):
    with open(a, 'r') as in_file, open(b, 'w') as out_file:
        cnt = 0
        for line in in_file:
            cnt += 1
            if cnt % 100 == 0:
                print('---------------------------------')
                print('Now now is : ' + str(cnt))
            if (line[-3:-2] == ',' and int(line[-2:-1]) != 0 and int(line[-2:-1]) != 1) or (line[-4:-3] == ','):
                out_file.write(line)


separate_texture_depth(inFile, outFile)
