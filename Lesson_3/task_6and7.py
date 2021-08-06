alf = ('abcdefghijklmnopqrstuvwxyz')
alf = list(alf)
result = []


def int_func(a):
    b = a.split()
    for c in b:
        d = list(c)
        alf = ('abcdefghijklmnopqrstuvwxyz')
        alf = list(alf)
        word = []
        theword = 0
        for i in d:
            if i in alf:
                word.append(i)
                theword = ''.join(word)
            else:
                theword = 0
                break
        if theword != 0:
            result.append(theword)
        else:
            pass
    theresult = ' '.join(result)
    return theresult.title()


print(int_func(input("Введите строку из слов: ")))
