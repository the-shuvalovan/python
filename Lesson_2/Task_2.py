i = int(input('Сколько значений в вашем списке? '))
a = i
list = []

while i > 0:
    n = input('Введите элемент для добавления в список: ')
    list.append(n)
    i-=1
print(list)

for b in range(a):
    if b % 2 == 0:
        m = list.pop(b)
        list.insert(b+1, m)
    else: b+=1

print(list)