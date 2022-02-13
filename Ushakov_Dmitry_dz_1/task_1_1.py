#1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
while True:
    seconds = int(input('Введите число: '))
    t = seconds
    d, h, m, s = round(t // (24 * 3600)), t // 3600, (t % 3600) // 60, t % 60
    if t < 60:
        print(s,'cек')
    elif t >= 60 and t < 3600:
        print(m,'мин',s,'cек')
    elif t >= 3600 and t < 86400:
        print(h,'час',m, 'мин',s,'cек')
    else:
        print(d,'дн',h,'час',m, 'мин',s,'cек')

