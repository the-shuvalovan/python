import json

with open("file_7.txt") as f:
    content = f.readlines()
    dictionary = {}
    av_inc = []
    for i in content:
        l = i.split()
        income = int(l[2])
        spent = int(l[3])
        profit = income - spent
        dictionary.update({l[0]: profit})
        if profit >= 0:
            av_inc.append(profit)
    average_profit = sum(av_inc) / len(av_inc)
    dictionary2 = {'average_profit': average_profit}
    result = [dictionary, dictionary2]
    with open("file_7.json", "w") as write_f:
        json.dump(result, write_f)
