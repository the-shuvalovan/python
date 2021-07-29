revenue=int(input('Введите значение выручки: '))
costs=int(input('Введите значение издержек: '))
if revenue>costs:
    income = revenue - costs
    profit = (income % revenue)
    print(f"Вы в прибыли. Ваша рентабельность - {round(profit, 0)}%.")
    staff=int(input('Укажите число сотрудников: '))
    revenue_per_employee = income / staff
    print(f"Ваша прибыль в расчете на одного сотрудника - {round(revenue_per_employee, 2)}")
elif revenue<costs:
    print('Ваши издержки больше выручки.')
else:
    print('Вы работаете в ноль.')