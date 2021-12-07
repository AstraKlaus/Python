import math
import random

t = float(input("Введите температуру: "))
if t > 10:
    print("Хорошая погода!")
else:
    print("Плохая погода!")

P = int(input("Введите оценку: "))
if P == 5:
    print("Молодец!")
elif P == 4:
    print("Хорошо!")
else:
    print("Лентяй!")

number = int(input("Введите натуральное число: "))
if number % 4 == 0:
    print("Число четное и кратное 4")
if number % 2 != 0 and number % 5 == 0:
    print("Число нечетное и кратное 5")

D = float(input("Введите Диаметр поперечного сечения: "))
A = float(input("Введите Ширинy квадратного бруса: "))
d = A * math.sqrt(5)
print(f"Диагональ бруса = {d}")
if D >= d:
    print("Можно")
if D < d:
    print("Нельзя")

x = random.randint(1, 100)
print(f"Выбранное место {x}")
if x > 36:
    print("Боковое")
else:
    print("Купе")
if x % 2 == 0:
    print("Верхнее")
else:
    print("Нижнее")

M = random.randint(1, 5000)
if M % 2 == 0:
    print("Сумма денег: " + str(M))
    A = M % 500
    A1 = M // 500
    print("500: " + str(A1))
    B = A % 100
    B1 = A // 100
    print("100:" + str(B1))
    C = B % 10
    C1 = B // 10
    print("10:" + str(C1))
    D1 = C // 2
    print("2:" + str(D1))
else:
    print("Невозможно")

A = random.randint(1, 10)
Cube = A ** 3
print("V Cube = " + str(Cube))

H = random.randint(1, 10)
R = random.randint(1, 10)
pi = math.pi
Cylinder = pi * R ** 2 * H
print("Объем цилиндра = " + str(Cylinder))

M = random.randint(1, 100)
print("Объем воды = " + str(M))

if Cube >= M:
    print("Вода поместится в куб,")
elif Cube == M:
    print("Вода поместится в цилиндр,")
elif Cylinder == M:
    if Cylinder >= M:
        print("Вода поместится в куб и цилиндр")
elif Cylinder < M:
    if Cube < M:
        print("Вода не поместится в куб и цилиндр")

X = int(input("Введите первую сторону треугольника"))
Y = int(input("Введите вторую сторону треугольника"))
Z = int(input("Введите третью сторону треугольника"))
if X + Y <= Z or Y + Z <= X or X + Z <= Y:
    print('невозможен')
elif (X * X + Y * Y == Z * Z) or (X * X + Z * Z == Y * Y) or (Z * Z + Y * Y == X * X):
    print("прямоугольный")

x = int(input("Введите число:"))
a = int(input("Введите начало промежутка"))
b = int(input("Введите конец промежутка"))
if x in range(a, b + 1):
    print("Число принадлежит промежутку")
else:
    print("Число не принадлежить промежутку")

A = random.randint(-100, 100)
print("A= " + str(A))
B = random.randint(-100, 100)
print("B= " + str(B))
C = random.randint(-100, 100)
print("C= " + str(C) + "\n")
print("A < B  B > C""\n")
defer = False
if A < B and B < C:
    print("Первое условие выполняется")
    defer = True
if A > B and B > C:
    print("Второе условие выполняется")
    defer = True
if defer == False:
    print("Ниодно из условий не выполняется")

x1, y1, a1, b1 = map(int, input('Введите координаты левого нижнего угла и длины сторон первого прямоугольника').split())
x2, y2, a2, b2 = map(int, input('Введите координаты левого нижнего угла и длины сторон второго прямоугольника').split())
if x1 + a1 > x2 + a2:
    x3 = x1 + a1
else:
    x3 = x2 + a2
if y1 + b1 > y2 + b2:
    y3 = y1 + b1
else:
    y3 = y2 + b2
print(f'Координаты правого верхнего угла общего прямоугольника x= {x3} y= {y3}')

n = int(input("Введите двузначное число: "))
a = n / 10
b = n % 10
if (n ** 2 == 4 * (a ** 3 + b ** 3)):
    print("Да")
else:
    print("Нет")
b = 0
a = 0

while (b < 0) and (a < b):
    a, b = map(int, input('Введите через пробел размеры стола a>b: ').split())
while (b < 0) and (c < d):
    c, d = map(int, input('Введите через пробел размеры стола c>d: ').split())

j1 = (a // c) * (b // d)
j2 = (a // d) * (b // c)
print(f'Длинной стороной вдоль длинной стороны стола= {j1}')
print(f'Длинной стороной вдоль короткой стороны стола= {j2}')
if j1 > j2:
    print('Длинной стороной вдоль длинной стороны стола больше')
elif j2 > j1:
    print('Длинной стороной вдоль короткой стороны стола больше')
else:
    print('При разном расположении одинаково')

t = int(input('сколько минут прошло с начала часа? - '))
if (t % 5) in range(1, 4):
    print('Горит зеленый сигнал')
else:
    print('Горит красный сигнал')

a1, b1, a2, b2 = map(int, input('Введите размеры сторон первого и второго прямоугольника').split())
if (((a1 ** 2) + (b1 ** 2)) <= ((a2 ** 2) + (b2 ** 2))):
    print("Дa")
else:
    print("Нет")

while n not in range(1, 13):
    n = int(input("Введите номер месяца: "))
if n == 1:
    print("Январь.")


elif n == 2:
    print("Февраль.")


elif n == 3:
    print("Март.")


elif n == 4:
    print("Апрель.")


elif n == 5:
    print("Май.")


elif n == 6:
    print("Июнь.")


elif n == 7:
    print("Июль.")


elif n == 8:
    print("Август.")


elif n == 9:
    print("Сентябрь.")


elif n == 10:
    print("Октябрь.")


elif n == 11:
    print("Ноябрь.")


elif n == 12:
    print("Декабрь.")
k = 0
while k not in range(6, 15):
    k = int(input('Введите номер масти: '))
if k == 6:
    print("Шестерка ", end="")
elif k == 7:
    print("Семерка ", end="")
elif k == 8:
    print("Восьмерка ", end="")
elif k == 9:
    print("Девятка ", end="")
elif k == 10:
    print("Десятка ", end="")
elif k == 11:
    print("Валет ", end="")
elif k == 12:
    print("Дама ", end="")
elif k == 13:
    print("Король ", end="")
elif k == 14:
    print("Туз ", end="")
n = 0
while n not in range(1, 5):
    n = int(input('Введите номер масти: '))
if n == 1:
    print('пики')
elif n == 2:
    print('трефы')
elif n == 3:
    print('бубны')
elif n == 4:
    print('червы')

year = int(input('Введите номер года: '))
g = 0
while g < 1:
    g = int(input('Введите год: '))
vis = ((g % 100 != 0) and (g % 4 == 0)) or (g % 400 == 0)

m = 0
while m not in range(1, 13):
    m = int(input('Введите номер месяца: '))

n = 0
while ((m not in [1, 3, 5, 7, 8, 10, 12]) and (n not in range(1, 32)) or (
        (m not in [4, 6, 9, 11]) and (n not in range(1, 31))) or (
               (m != 2) and (not vis) and (n not in range(1, 30))) or ((m != 2) and vis and (n not in range(1, 29)))):
    n = int(input("Введите номер дня состветвующий месяцу и году: "))

if (m == 1) and (n == 1):
    np = 31
    mp = 12
    gp = g - 1
elif ((m in [5, 7, 10, 12]) and (n == 1)):
    np = 30
    mp = m
    gp = g
elif ((m in [2, 4, 6, 8, 9, 11]) and (n == 1)):

    np = 31
    mp = m
    gp = g
elif (m == 3) and (n == 1):
    if vis:
        np = 29
    else:
        np = 28
    mp = m
    gp = g
else:
    np = n - 1
    mp = m
    gp = g

print('Предыдущая дата:')
if np < 10:
    print('0', np, '.')
else:
    print(np, '.')
if mp < 10:
    print('0', mp, '.')
else:
    print(mp, '.')
print(gp)

k = int(input('Введите количество грибов: '))

if k in range(10, 21):
    print(f'Мы нашли {k} грибов в лесу')
elif k % 10 == 1:
    print(f'Мы нашли {k} гриб в лесу')
elif k % 10 in range(2, 5):
    print(f'Мы нашли {k} гриба в лесу')
else:
    print(f'Мы нашли {k} грибов в лесу')

sell = float(input("Сколько стоит товар? "))
print(f'Товар стоит {sell // 100} рублей {sell % 100} копеек.')

g1, m1 = map(int, input('Введите год и месяц рождения через пробел').split())
g2, m2 = map(int, input('Введите текущий год и месяц через пробел').split())
v = g2 * 12 + m2 - g1 * 12 - m1
g = v // 12
m = v % 12
print(f'Возраст {g} лет {m} мес.')

g1, m1, d1 = map(int, input('Введите год, месяц и день рождения первого человека через пробел').split())
g2, m2, d2 = map(int, input('Введите год, месяц и день рождения второго человека через пробел').split())

if g1 > g2:
    print('Второй человек старше')
elif g1 < g2:
    print('Первый человек старше')
else:
    if m1 > m2:
        print('Второй человек старше')
    elif m1 < m2:
        print('Первый человек старше')
    else:
        if d1 > d2:
            print('Второй человек старше')
        elif d1 < d2:
            print('Первый человек старше')
        else:
            print('Одинаковая дата рождения у обоих')
