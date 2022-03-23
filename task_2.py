number = int(input('Введите время в секундах: '))
hours = number // 3600
sec = number % 3600
minutes = sec // 60
seconds = sec % 60

print (hours, minutes, seconds)
print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))