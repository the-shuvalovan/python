def my_func(**kwargs):
    print(str(kwargs))
    return kwargs


my_func(name=input('Введите ваше имя: '),
        fname=input('Введите вашу фамилию: '),
        year=int(input('Введите год вашего рождения: ')),
        city=input('Введите город вашего проживания: '),
        email=input('Введите ваш E-mail: '),
        tel=input('Введите ваш номер телефона: '))
