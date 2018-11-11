def mean(my_list):
    total = 0
    if len(my_list) == 0:
        return "Error: Empty List"
    for i in range(len(my_list)):
        total += my_list[i]
    return total/len(my_list)
