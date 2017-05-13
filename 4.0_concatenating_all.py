import csv
import datetime
import sys
import glob
import itertools
from collections import defaultdict

# Raw data files have the format like '2013-06-04'.
# To be able to use this script during the whole of 2013,
# the glob is set to search for the pattern '2013-*.csv'

files = [f for f in glob.glob('/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/raw_data_3536/training_data_16_*.csv')]
# Output file looks like '20130620-filtered.csv'
outfile = '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/' \
          'raw_data_concat_all/{:%Y%m%d}_16_merged_from_8_sequences.csv'.format(datetime.datetime.now())

with open(outfile, 'w') as w:
    for input_file in files:
        with open(input_file, 'r') as r:
            # cnt = 0
            for num, line in enumerate(r):
                # cnt += 1
                w.write(line)
