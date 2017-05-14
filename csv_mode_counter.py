from collections import OrderedDict


def csv_mode_preprocessing(OUTPUT_FILE):
    x = OrderedDict()

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

    with open(OUTPUT_FILE, 'r') as r:
        cnt = 0
        for num, line in enumerate(r):
            cnt += 1
            if line[-3:-2] == ',':
                # print("yes, it is a comma.===============!!~~~~~~~~")
                last_char_in_line = int(line[-2:-1])
            else:
                # print("no, not comma.-------------~~~~~~~~`")
                last_char_in_line = int(line[-3:-1])

            mode = last_char_in_line

            if mode == 0:
                mode_0 += 1
            elif mode == 1:
                mode_1 += 1
            elif mode == 2:
                mode_2 += 1
            elif mode == 3:
                mode_3 += 1
            elif mode == 4:
                mode_4 += 1
            elif mode == 5:
                mode_5 += 1
            elif mode == 6:
                mode_6 += 1
            elif mode == 7:
                mode_7 += 1
            elif mode == 8:
                mode_8 += 1
            elif mode == 9:
                mode_9 += 1
            elif mode == 10:
                mode_10 += 1
            elif mode == 11:
                mode_11 += 1
            elif mode == 12:
                mode_12 += 1
            elif mode == 13:
                mode_13 += 1
            elif mode == 14:
                mode_14 += 1
            elif mode == 15:
                mode_15 += 1
            elif mode == 16:
                mode_16 += 1
            elif mode == 17:
                mode_17 += 1
            elif mode == 18:
                mode_18 += 1
            elif mode == 19:
                mode_19 += 1
            elif mode == 20:
                mode_20 += 1
            elif mode == 21:
                mode_21 += 1
            elif mode == 22:
                mode_22 += 1
            elif mode == 23:
                mode_23 += 1
            elif mode == 24:
                mode_24 += 1
            elif mode == 25:
                mode_25 += 1
            elif mode == 26:
                mode_26 += 1
            elif mode == 27:
                mode_27 += 1
            elif mode == 28:
                mode_28 += 1
            elif mode == 29:
                mode_29 += 1
            elif mode == 30:
                mode_30 += 1
            elif mode == 31:
                mode_31 += 1
            elif mode == 32:
                mode_32 += 1
            elif mode == 33:
                mode_33 += 1
            elif mode == 34:
                mode_34 += 1
            elif mode == 35:
                mode_35 += 1
            elif mode == 36:
                mode_36 += 1

                # print("last char in line: " + str(last_char_in_line))
                # print("type : " + str(type(last_char_in_line)))
                # print('')
        # x["mode_0"] = mode_0
        x['mode__0'] = mode_0
        x['mode__1'] = mode_1
        x['mode__2'] = mode_2
        x['mode__3'] = mode_3
        x['mode__4'] = mode_4
        x['mode__5'] = mode_5
        x['mode__6'] = mode_6
        x['mode__7'] = mode_7
        x['mode__8'] = mode_8
        x['mode__9'] = mode_9
        x['mode_10'] = mode_10
        x['mode_11'] = mode_11
        x['mode_12'] = mode_12
        x['mode_13'] = mode_13
        x['mode_14'] = mode_14
        x['mode_15'] = mode_15
        x['mode_16'] = mode_16
        x['mode_17'] = mode_17
        x['mode_18'] = mode_18
        x['mode_19'] = mode_19
        x['mode_20'] = mode_20
        x['mode_21'] = mode_21
        x['mode_22'] = mode_22
        x['mode_23'] = mode_23
        x['mode_24'] = mode_24
        x['mode_25'] = mode_25
        x['mode_26'] = mode_26
        x['mode_27'] = mode_27
        x['mode_28'] = mode_28
        x['mode_29'] = mode_29
        x['mode_30'] = mode_30
        x['mode_31'] = mode_31
        x['mode_32'] = mode_32
        x['mode_33'] = mode_33
        x['mode_34'] = mode_34
        x['mode_35'] = mode_35
        x['mode_36'] = mode_36

        veri_1 = 0

        for m, n in x.items():
            print(str(m) + " :   " + str(n) + '   <<------ ||-------->>      ' + str(m) + " / total (%) :   " + str(
                float(n) / float(cnt)))
            veri_1 += float(n) / float(cnt)

        print('===================')
        print("veri_1 (should be nearly equal to 1 or 0.999999..) : " + str(veri_1))
        print('===================')

        sorted_x = OrderedDict(sorted(x.items(), key=lambda t: t[1]))

        print("")
        print("------------beautiful cutting line, above is unsorted, below is sorted-----------")
        print("")

        veri_2 = 0
        for m, n in sorted_x.items():
            print(str(m) + " :   " + str(n) + '  <<------ ||-------->> ' + str(m) + " / total (%) :   " + str(
                float(n) / float(cnt)))
            veri_2 += float(n) / float(cnt)

        print('===================')
        print("veri_2 (should be nearly equal to 1 or 0.999999..) : " + str(veri_2))
        print('===================')

        print("total lines : " + str(cnt))

        return x
