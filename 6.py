firstDay = int(input('Сколько вы пробежали в первый день: '))
finalDay = int(input('Какое растояние вы хотите пробежать? '))
resultDay = firstDay/100*10
day = 0
while firstDay <= finalDay:
    day += 1
    firstDay+=resultDay
    print('Количество дней до победного результата: ', day)