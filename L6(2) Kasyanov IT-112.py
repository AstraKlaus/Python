import random

x = int(input(f"Введите число: "))
while x > 0:
    print(x%10, end='')
    x//=10

x = int(input(f"Введите число отличное от 0: "))
while x != 1:
    if x % 2 == 0:
        x //= 2
    elif x % 2 != 0:
        x = (x * 3 + 1) // 2
print(x)

count = int(input("Введите количество чисел: "))
k = 0
for i in range(1, count + 1):
    number = int(input("Введите простое число: "))
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k += 1
            break
print(f"Количество простых чисел {k}")


x = int(input(f"Введите число: "))
ls=0
while x > 0:
    if x%10 == 8:
        ls = k
    x //=10
print(f"Номер цифры 8: {ls}")

a_1 = 0
b_2 = 0
while True:
    a = int(input("команда 1: "))
    b = int(input("команда 2: "))
    if a == 0 and b == 0:
        break
    a_1 += a
    b_2 += b
    print("1 команда - ", a_1, "/", b_2, " - команда 2")

if a_1 > b_2:
    print("победила команда номер 1 со счетом", a_1, "/", b_2)
elif a_1 == b_2:
    print("ничья со счетом", b_2, "/", a_1)
else:
    print("победила команда номер 2 со счетом", b_2, "/", a_1)

 v1, v2, v3, v4, v5, v6, v7, = 0,0,0,0,0,0,0

n = random.randint(1,200)

while n != 0:
    while n - 64 > 0:
        n -= 64
        v7 += 1
    while n - 32 > 0:
        n -= 32
        v6 += 1
    while n - 16 > 0:
        n -= 16
        v5 += 1
    while n - 8 > 0:
        n -= 8
        v4 += 1
    while n - 4 > 0:
        n -= 4
        v3 += 1
    while n - 2 > 0:
        n -= 2
        v2 += 1
    while n - 1 > 0:
        n -= 1
        v1 += 1
print(f"Использованные купюры:\nКупюры по 1: {v1}\nКупюры по 2: {v2}\nКупюры по 4: {v3}\nКупюры по 8: {v4}\nКупюры по 16: {v5}\nКупюры по 32: {v6}\nКупюры по 64: {v7}\nОбщее количество куплюр: {v1+v2+v3+v4+v5+v6+v7}")

x = random.randint(100,100000)
summary = 0
m = int(input("Введите сколько надо суммировать последних цифр"))
while m>0:
    summary += x%10
    x //= 10
    m-=1
print(f"Сумма равна {summary}")

n = int(input("Введите число"))
i = 2
while i <= n:
    i = i + 1
    if n % i == 0:
        print(f"Минимальный делитель: {i}")
        break

x = int(input("Введите число х: "))
a = int(input("Введите число а: "))
k = int(input("Введите число k: "))
b = int(input("Введите число b: "))
o = j = 0
while x > 0:
    if x%10 == a:
        print("1) Да")
        j += 1
    if j > k:
        print("2) Да")
    if x%10 == b:
        o += 1
    if j > 0 and o > 0:
        print("3) Да")

x = random.randint(1,30)
y = random.randint(1,30)
z = random.randint(1,30)

k = 0
while x > 0:
    while y > 0
        while z > 0:
            if x**2 + y ** 2 == z ** 2 or z**2 + y ** 2 == x ** 2 or x**2 + z ** 2 == y ** 2:
                k += 1
            z -= 1
        y -= 1
    x -= 1
print(f"Всего {k} пифагоровы тройки")


n = int(input("Введите число: "))

i=0
j=0
k=0
while i != 9:
    while j != 9:
        while k != 9:
            if i+j+k==n:
                print(i*100+j*10+k)
            i +=1
            j +=1
            k +=1
        k=0
    j = 0












