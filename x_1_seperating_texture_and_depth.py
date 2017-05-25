inFile = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/test_data_32x32/testing_32x32.csv'
outFile_depth = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/test_data_32x32/testing_32x32_depth_only.csv'
outFile_texture = '/Users/Pharrell_WANG/PycharmProjects/vcmd_data_prepare/test_data_32x32/testing_32x32_texture_only.csv'


def separate_texture_depth(a, b, c):
    with open(a, 'r') as in_file, open(b, 'w') as out_file_d, open(c, 'w') as out_file_t:
        cnt = 0
        for line in in_file:
            cnt += 1
            if cnt % 100 == 0:
                print('---------------------------------')
                print('Now now is : ' + str(cnt))
            if int(line[:1]) == 0:
                out_file_d.write(line)
            else:
                out_file_t.write(line)


separate_texture_depth(inFile, outFile_depth, outFile_texture)
