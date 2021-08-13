with open('file_3.txt', 'r') as f:
    content = f.readlines()
    salaries = []
    for line in content:
        l = line.split()
        name = l[0]
        salary = float(l[1])
        salaries.append(salary)
        if salary < 20000:
            print(f'{name} получает зарплату менее 20 тыс.')
    salary = 0
    everage = 0
    for n in salaries:
        salary += n
    n = len(salaries)
    everage = salary / n
    print(f'Средняя зарплата: {everage}.')
