from random import uniform

# s = 0
# k = 0
# for i in range(1, 1001):
#     if i % 10 == 9:
#         print(i)
#         k += 1
#         s += i
# print(s)
# print(k)

# Таблица сложения
# for i in range(1,10):
#     for j in range(1,10):
#         print('{}+{}={}'.format(i,j,i+j))
#     print('-'*10)

# n = int(input('Введите кол-во автомобилей: '))
# maxx = 0
# sum_t = 0
# sum_s = 0
# for i in range(1, n + 1):
#     delta = 40000
#     t = uniform(3600, 100000); t = round(t / 3600, 2)
#     s = uniform(t * delta, t * delta + 100000); s = round(s / 1000, 2)
#     v = round(s / t, 2)
#     print(f'автомобиль {i} прошел время расстояние {s} км со скоростью {v} км/ч и временем {t} ч')
#     if maxx < v:
#         maxx = v
#         num = i
#     sum_s+=s
#     sum_t+=t
# print(f'Максимальная скорость автомобиля {num} равна {v}')
# print(f'Средняя скорость {round(sum_s/sum_t, 2)} км/ч')

name_1 = 'Ф1 И1 О1'
name_2 = 'Ф2 И2 О2'
name_3 = 'Ф3 И3 О3'
k = 0
m = 0
for worker in name_1, name_2, name_3:
    k += 1
    m = 0
    summary_oklad = 0
    summary= 0
    premia = 0
    premia_ndfl = 0
    file = open("C:/Users/Xaser/PycharmProjects/Laborant/"+worker+".txt","w")
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
        file.write(
        f'\tРассченый листок за {month} 2021\n'+
              f'\t№ {k} - {worker}\n'+
              f'\tНачислено:\n'+
              f'\tОплата по окладу: {int(oklad // 1)} руб {int(oklad % 1 * 100)} коп.\n'+
              f'\tВыплата аванса: {int(avans // 1)} руб {int(avans % 1 * 100)} коп.\n'+
              f'\tВыплата зарплаты: {int(payment // 1)} руб {int(payment % 1 * 100)} коп.'+
            f'\tПремия: {int(premia_ndfl // 1)} руб {int(premia_ndfl % 1 * 100)} коп.' if premia != 0 else ""+
        f'\tУдержано(НДФЛ): {int(ndfl // 1)} руб {int(ndfl % 1 * 100)} коп.\n'+
              f'\tВыплачено: {int((avans + payment + premia_ndfl) // 1)} руб {int((avans + payment + premia_ndfl) % 1 * 100)} коп.\n'+
              f'\tОбщий облагаемый доход: {round(summary, 2)}'+
        '-' * 50+
        '_' * 50)
        premia = 0
