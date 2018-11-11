def median(num):

    num_list = list(num)
    numbers = len(num_list)

    if numbers % 2 == 1:
        list_median = num_list[(int(numbers/2))]

    elif numbers == 0:
        list_median = 0

    else:
        list_median = (num_list[int(numbers/2) - 1] + num_list[int(numbers/2)])/2

    return list_median
