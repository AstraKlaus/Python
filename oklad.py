from random import *

mass = 0
count = 0
for i in range(1, 1001):
    if i % 10 == 9:
        mass += i
        count += 1
        print(mass, count)

# Таблица умножения
for i in range(1, 10):
    for j in range(1, 10):
        print("{}+{}={}".format(i, j, i + j))
    print('-' * 5)

count = int(input("Введите количество автомобилей: "))
maxSpeed = 0
maxCount = 0
sumTime = 0
sumSpeed = 0
time = 1
speed = 10 ** 10
for i in range(1, count + 1):
    time = 1
    speed = 10 ** 10
    while (time * speed / time) > 170:
        time = round(uniform(1, 100000) / 1000, 2)
        speed = round(uniform(1, 100000) / 3600, 2)
        sumSpeed += speed
        sumTime += time
        if speed > maxSpeed:
            maxSpeed = speed
            maxCount = i
    print(
        f"Автомобиль с порядковым номером {i} прошел {round(time * speed, 2)} км со скоростью: {speed}км/ч за {time} часа")
print(f"Максимальная скорость: {maxSpeed}км/ч")
print(f"Среднаяя скорость: {round(sumSpeed / sumTime, 2)}км/ч")

card_1 = 'Ф1 И1 О1'
card_2 = 'Ф2 И2 О2'
card_3 = 'Ф3 И3 О3'
k = 0
m = 0
premia = 0
for worker in card_1, card_2, card_3:
    k += 1
    m = 0
    summary_oklad = 0
    summary= 0
    premia_ndfl = 0
    for month in 'Январь Февраль Март Апрель Май Июнь Июль Август Сентябрь Октябрь Ноябрь Декабрь'.split():
        m += 1
        if m == 3:
            oklad = round(uniform(10000, 25000), 2)
            summary_oklad += oklad
            premia = round(summary_oklad * 0.15, 2)
            ndfl = round((oklad + premia) * 0.13, 2)
            avans = round((oklad - ndfl) * 0.43, 2)
            payment = round((oklad - ndfl) * 0.57, 2)
            premia_ndfl = premia - ndfl
            summary_oklad = 0
            m = 0
        else:
            oklad = round(uniform(10000, 25000), 2)
            ndfl = round(oklad * 0.13, 2)
            avans = round((oklad - ndfl) * 0.43, 2)
            payment = round((oklad - ndfl) * 0.57, 2)
            summary_oklad += oklad
        summary += oklad
        print(f'\tРассченый листок за {month} 2021\n'
              f'\t№ {k} - {worker}\n'
              f'\tНачислено:\n'
              f'\tОплата по окладу:  {str(int(oklad // 1))[:-3]} {str(int(oklad // 1))[-3:]} руб {str(int(oklad % 1 * 100))} коп.\n'
              f'\tВыплата аванса: {int(avans // 1)} руб {int(avans % 1 * 100)} коп.\n'
              f'\tВыплата зарплаты: {int(payment // 1)} руб {int(payment % 1 * 100)} коп.')
        if premia != 0:
            print(f'\tПремия: {int(premia_ndfl // 1)} руб {int(premia_ndfl % 1 * 100)} коп.')
        print(f'\tУдержано(НДФЛ): {int(ndfl // 1)} руб {int(ndfl % 1 * 100)} коп.\n'
              f'\tВыплачено: {int((avans + payment + premia_ndfl) // 1)} руб {int((avans + payment + premia_ndfl) % 1 * 100)} коп.\n'
              f'\tОбщий облагаемый доход: {round(summary, 2)}')
        print('-' * 50)
        print('_' * 50)
        premia = 0
