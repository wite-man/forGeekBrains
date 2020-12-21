money = int(input('Введите значение выручки '))
credit = int(input('Введите значение издержек '))
profit = money - credit
profitability = profit/money

if money > credit:
    print('Поздравляю, ваша компания приносит прибыль!')
    print('Рентабельность составляет ', profitability)
    people = int(input('Введите количество сотрудников '))
    print('Прибыль на каждого сотрудника составляет: ', profit/people)
else:
    print('Закрывайтесь нахрен')
