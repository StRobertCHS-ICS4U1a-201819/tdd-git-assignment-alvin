def mean(my_list):
    total = 0
    for i in range(len(my_list)):
        total += my_list[i]
    return total/len(my_list)