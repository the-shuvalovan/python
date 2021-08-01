string = input('Введите строку из нескольких слов, разделённых пробелами: ')
list = string.split()
n = 0
for i in list:
    print(list[n][:10])
    n+=1