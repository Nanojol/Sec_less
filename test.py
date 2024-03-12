def min_value(list):
    # set first element as min
    min = list[0]
    print(min)
    # print(i)
    for i in list:
        # check if the current element is less than min
        if i < min:
            print(min)
            print(i)
            min = i
    return min

num = [12, 65, 54, 39, 102, 37, 72, 33, 5, -11, 0, 15]
print(min_value(num))