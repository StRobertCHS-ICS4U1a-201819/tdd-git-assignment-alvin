import math

def median(num):

    if len(num) % 2 == 1:
        num = num[(int(len(num)/2))]

    elif len(num) == 0:
        return "Error: Empty List"

    else:
        num = (num[int(len(num)/2) - 1] + num[int(len(num)/2)])/2

    return num


def ranges(num):

    num_list = list(num)

    if len(num_list) >= 2:
        return num_list[len(num_list) - 1] - num_list[0]

    elif len(num_list) == 1:
        return num_list[0]

    else:
        return "Error: Empty List"


def variance(list):

    len_list = len(list)
    mean = sum(list)/len(list)
    datapoint_mean_diff = []
    datapoint_squared = []

    a = 0
    while a <= len_list - 1:
        x = list[a] - mean
        datapoint_mean_diff.append(x)
        a = a + 1

    b = 0
    while b <= len_list - 1:
        y = datapoint_mean_diff[b] * datapoint_mean_diff[b]
        datapoint_squared.append(y)
        b = b + 1

    sum_datapoint_squared = sum(datapoint_squared)
    number = (sum_datapoint_squared / (len_list - 1))
    return number


def standard_deviation(list):

    len_list = len(list)
    mean = sum(list)/len(list)
    datapoint_mean_diff = []
    datapoint_squared = []

    a = 0
    while a <= len_list - 1:
        x = list[a] - mean
        datapoint_mean_diff.append(x)
        a = a + 1

    b = 0
    while b <= len_list - 1:
        y = datapoint_mean_diff[b] * datapoint_mean_diff[b]
        datapoint_squared.append(y)
        b = b + 1

    sum_datapoint_squared = sum(datapoint_squared)
    number = (sum_datapoint_squared / (len_list - 1))

    return float("%0.2f" % (math.sqrt(number)))
