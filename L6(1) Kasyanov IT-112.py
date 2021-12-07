import random

prev_s = 1000
s = 0
e = .001
n = 1

N = int(input('N = '))
sum = 0

for n in range(1, N + 1):
    sum += (1 / (n ** n)) * ((-1) ** (n - 1))
print(round(sum, 3))

n = int(input("Введите количество километрвов: "))
y = int(input("Введите количество процентов: "))
x = int(input("Введите количество дней: "))
total = 0

for day in range(2, x + 1):
    n *= (y ** 00.1) + 1
    total += n
print(f"Суммарный путь {round(total, 2)}")

count = int(input("Введите количество чисел: "))
k = 0
for i in range(1, count + 1):
    number = int(input("Введите простое число: "))
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k += 1
            break
print(f"Количество простых чисел {k}")

n = 64
k = 4
g = 2
f = n // k - 1
for i in range(f + 2):
    a = i
    b = (n - k * a) // g
    print(a, ' Кролик(ов) ', b, ' Гусь(ей)')

for i in range(1, int(input("До какого числа таблицу сложения? ")) + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()

for i in range(1, int(input("До какого числа таблицу умножения? ")) + 1):
    for j in range(1, 10):
        print(i, '*', j, '=', i * j)
    print()

s = 0
for i in range(100, 501):
    s += i
print(f"Сумма всех чисел от 100 до 500 {s}")

sb = 0
for i in range(int(input("a = ")), 501):
    sb += i
print(f"Сумма всех чисел от a до 500 {sb}")

sc = 0
for i in range(-10, int(input("b = ")) + 1):
    sc += i
print(f"Сумма всех чисел от -10 до b {sc}")

sg = 0
for i in range(int(input("a = ")), int(input("b = ")) + 1):
    sg += i
print(f"Сумма всех чисел от a до b {sg}")

summary = 0
for i in range(1, int(input("Введите сколько будет вещественных чисел: ")) + 1):
    n = float(input("Введите вещественное число: "))
    summary += n
print(f"Сумма вещественных чисел: {summary}")

summary = 0
for i in range(1, int(input("Введите сколько будет элементов в цепи: ")) + 1):
    n = float(input("Введите сопротивление элемента: "))
    summary += n
print(f"Общее сопротивление цепи: {summary}")

r = 0.1 / 2
s = 0.005
for i in range(12):
    r += s
    print((4 / 3 * 3.14 * r ** 3) * 1000)

ln = 0
ls = 0
pr = 0
allS = 0
allT = 0
for i in range(1, int(input("Введите сколько будет автомобилей: ")) + 1):
    n = float(input("Введите скорость в км/ч: "))
    s = float(input("Введите путь в км: "))
    if n > ln:
        ln = n
        pr = i
    allS += s
    allT += s / n
print(
    f"Максимальная скорость автомобиля: {ln}\nПорядковый номер автомобиля с максимальной скоростью: {pr}\nСредняя скорость автомобилей: {allS // allT}")

r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12 = random.randint(1, 100000) * 12
k = 1
for zp in r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12:
    print(f"Зарплата {k} сотрудника: {zp}")
    k += 1
print(f"Средняя зарпалата за квартал {(r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11 + r12) // 12}")
print(f"Общая сумма за квартал всем работникам {(r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11 + r12)}")
k = 1
for zp in r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12:
    print(f"Зарплата {k} сотрудника за год: {zp * 4}")
    k += 1
k = 1
for zp in r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12:
    print(f"Отпускные {k} сотрудника: {(zp // 12) + (zp * 0.13)}")
    k += 1

v = random.randint(1, 1000)
print(f"Вес равен {v}")

v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 = 0, 100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000
k = 0
for char0 in v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10:
    for char1 in v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10:
        for char2 in v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10:
            for char3 in v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10:
                for char4 in v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10:
                    for char5 in v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10:
                        for char6 in v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10:
                            for char7 in v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10:
                                for char8 in v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10:
                                    for char9 in v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10:
                                        for char10 in v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10:
                                            if char0 + char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9 + char10 == v:
                                                k += 1
print(f"Число {v} можно сложить {k} раз")