from translate import Translator

translator = Translator(from_lang="english", to_lang="russian")

with open('file_4.txt', 'r') as f:
    content = f.readlines()
    print(content)
    for n in content:
        trcontent = []
        l = n.split()
        for i in l:
            t = translator.translate(i)
            trcontent.append(t)
        translation = "".join(trcontent)
        out_f = open("file_4_2.txt", "a")
        out_f.writelines(f'{translation} \n')
        out_f.close()
