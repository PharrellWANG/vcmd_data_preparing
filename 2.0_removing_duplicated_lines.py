# inFile = '/Users/Pharrell_WANG/PycharmProjects/tf_dp/data/2.csv'
#
# outFile = '/Users/Pharrell_WANG/PycharmProjects/tf_dp/data/3.csv'


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
                # print(line)  # skip duplicate
                continue

            seen.add(line)
            out_file.write(line)
