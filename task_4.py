number=int(input('Введите целое положительное число: '))
result=0
while number > 0:
    i = number % 10
    if i >= result: result=i
    number //= 10
print(f"Самая большая цифра в вашем числе - {result}")