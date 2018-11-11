def median(num):
    # list created to determine median
    num_list = list(num)
    # length of created list
    len_num_list = len(num_list)

    if len_num_list % 2 == 1:
        list_median = num_list[(int(len_num_list/2))]

    elif len_num_list == 0:
        list_median = 0

    else:
        list_median = (num_list[int(len_num_list/2) - 1] + num_list[int(len_num_list/2)])/2

    return list_median


def range(num):

    num_list = list(num)

    if len(num_list) >= 2:
        return num_list[len(num_list) - 1] - num_list[0]

    elif len(num_list) == 1:
        return num_list[0]

    else:
        return 0



