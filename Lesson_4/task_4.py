my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
sup_list = [n for i, n in enumerate(my_list) if n in my_list[:i]]
result = [n for n in my_list if n not in sup_list]
print(result)
