from b__mode_counter import csv_mode_preprocessing

ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/' \
            'raw_data_concat_all/20170427_16_merged_from_8_sequences.csv'

TRAINING_DATA = '/Users/Pharrell_WANG/PycharmProjects/proj_vcmd/train_data/training_16by16_fewer.csv'

def data_generator(ORIG_DATA, TRAINING_DATA, x_ordered_dict):
    with open(ORIG_DATA, 'r') as orig_data, open(TRAINING_DATA, 'w') as training_data:
        mode_0 = 0
        mode_1 = 0
        mode_2 = 0
        mode_3 = 0
        mode_4 = 0
        mode_5 = 0
        mode_6 = 0
        mode_7 = 0
        mode_8 = 0
        mode_9 = 0
        mode_10 = 0
        mode_11 = 0
        mode_12 = 0
        mode_13 = 0
        mode_14 = 0
        mode_15 = 0
        mode_16 = 0
        mode_17 = 0
        mode_18 = 0
        mode_19 = 0
        mode_20 = 0
        mode_21 = 0
        mode_22 = 0
        mode_23 = 0
        mode_24 = 0
        mode_25 = 0
        mode_26 = 0
        mode_27 = 0
        mode_28 = 0
        mode_29 = 0
        mode_30 = 0
        mode_31 = 0
        mode_32 = 0
        mode_33 = 0
        mode_34 = 0
        mode_35 = 0
        mode_36 = 0

        for line in orig_data:

            if line[-3:-2] == ',':
                # print("yes, it is a comma.")
                last_char_in_line = int(line[-2:-1])
            else:
                last_char_in_line = int(line[-3:-1])

            mode = last_char_in_line

            if mode == 0:
                mode_0 += 1
                if mode_0 <= 26286:
                    training_data.write(line)

            elif mode == 1:
                mode_1 += 1
                if mode_1 <= 26286:
                    training_data.write(line)

            elif mode == 2:
                mode_2 += 1
                if mode_2 <= 26286:
                    training_data.write(line)

            elif mode == 3:
                mode_3 += 1
                if mode_3 <= 26286:
                    training_data.write(line)

            elif mode == 4:
                mode_4 += 1
                if mode_4 <= 26286:
                    training_data.write(line)

            elif mode == 5:
                mode_5 += 1
                if mode_5 <= 26286:
                    training_data.write(line)

            elif mode == 6:
                mode_6 += 1
                if mode_6 <= 26286:
                    training_data.write(line)

            elif mode == 7:
                mode_7 += 1
                if mode_7 <= 26286:
                    training_data.write(line)

            elif mode == 8:
                mode_8 += 1
                if mode_8 <= 26286:
                    training_data.write(line)

            elif mode == 9:
                mode_9 += 1
                if mode_9 <= 26286:
                    training_data.write(line)

            elif mode == 10:
                mode_10 += 1
                if mode_10 <= 26286:
                    training_data.write(line)

            elif mode == 11:
                mode_11 += 1
                if mode_11 <= 26286:
                    training_data.write(line)

            elif mode == 12:
                mode_12 += 1
                if mode_12 <= 26286:
                    training_data.write(line)

            elif mode == 13:
                mode_13 += 1
                if mode_13 <= 26286:
                    training_data.write(line)

            elif mode == 14:
                mode_14 += 1
                if mode_14 <= 26286:
                    training_data.write(line)

            elif mode == 15:
                mode_15 += 1
                if mode_15 <= 26286:
                    training_data.write(line)

            elif mode == 16:
                mode_16 += 1
                if mode_16 <= 26286:
                    training_data.write(line)

            elif mode == 17:
                mode_17 += 1
                if mode_17 <= 26286:
                    training_data.write(line)

            elif mode == 18:
                mode_18 += 1
                if mode_18 <= 26286:
                    training_data.write(line)

            elif mode == 19:
                mode_19 += 1
                if mode_19 <= 26286:
                    training_data.write(line)

            elif mode == 20:
                mode_20 += 1
                if mode_20 <= 26286:
                    training_data.write(line)

            elif mode == 21:
                mode_21 += 1
                if mode_21 <= 26286:
                    training_data.write(line)

            elif mode == 22:
                mode_22 += 1
                if mode_22 <= 26286:
                    training_data.write(line)

            elif mode == 23:
                mode_23 += 1
                if mode_23 <= 26286:
                    training_data.write(line)

            elif mode == 24:
                mode_24 += 1
                if mode_24 <= 26286:
                    training_data.write(line)

            elif mode == 25:
                mode_25 += 1
                if mode_25 <= 26286:
                    training_data.write(line)

            elif mode == 26:
                mode_26 += 1
                if mode_26 <= 26286:
                    training_data.write(line)

            elif mode == 27:
                mode_27 += 1
                if mode_27 <= 26286:
                    training_data.write(line)

            elif mode == 28:
                mode_28 += 1
                if mode_28 <= 26286:
                    training_data.write(line)

            elif mode == 29:
                mode_29 += 1
                if mode_29 <= 26286:
                    training_data.write(line)

            elif mode == 30:
                mode_30 += 1
                if mode_30 <= 26286:
                    training_data.write(line)

            elif mode == 31:
                mode_31 += 1
                if mode_31 <= 26286:
                    training_data.write(line)

            elif mode == 32:
                mode_32 += 1
                if mode_32 <= 26286:
                    training_data.write(line)

            elif mode == 33:
                mode_33 += 1
                if mode_33 <= 26286:
                    training_data.write(line)

            elif mode == 34:
                mode_34 += 1
                if mode_34 <= 26286:
                    training_data.write(line)

            elif mode == 35:
                mode_35 += 1
                if mode_35 <= 26286:
                    training_data.write(line)

            elif mode == 36:
                mode_36 += 1
                if mode_36 <= 26286:
                    training_data.write(line)


x_ordered_dict = csv_mode_preprocessing(OUTPUT_FILE=ORIG_DATA)
data_generator(ORIG_DATA=ORIG_DATA, TRAINING_DATA=TRAINING_DATA,
               x_ordered_dict=x_ordered_dict,
               )
