out_f = open("file_5.txt", "w")
wr_str = input('Введите числа, разделенные пробелом: ')
out_f.writelines(f'{wr_str} \n')
out_f.close()

with open('file_5.txt', 'r') as f:
    content = f.read()
    l = content.split()
    result = 0
    for i in l:
        try:
            n = int(i)
            result += n
        except:
            pass
    print(result)
