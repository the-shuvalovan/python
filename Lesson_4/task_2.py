my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [x for y, x in zip(my_list, my_list[1:]) if x > y]
print(result)
