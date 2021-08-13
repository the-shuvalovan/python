with open("file_6.txt") as f:
    content = f.readlines()
    dictionary = {}
    for i in content:
        i = i.replace(':', ' ')
        i = i.replace('(', ' ')
        i = i.replace(')', ' ')
        l = i.split()
        result = 0
        for k in l:
            try:
                n = int(k)
                result += n
            except:
                pass
        dictionary.update({l[0]: result})
print(dictionary)
