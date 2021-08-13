out_f = open("file_1.txt", "w")
while True:
    wr_str = input('Введите данные для записи: ')
    out_f.writelines(f'{wr_str} \n')
    if not wr_str:
        print('Ввод данных завершен.')
        break
out_f.close()
