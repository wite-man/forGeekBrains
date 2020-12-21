UserAnswer=int(input('Введите количество секунд: '))
hour=str(UserAnswer//3600)
minute=(UserAnswer//60)%60
second=UserAnswer%60
if minute<10:
    minute='0'+str(minute)
else:
    minute=str(minute)
if second<10:
    second='0'+str(second)
else:
    second=str(second)
print(hour+':'+minute+':'+second)
