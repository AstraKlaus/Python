a1 = int(input(f"Введите 1 число "))
a2 = int(input(f"Введите 2 число "))
a3 = int(input(f"Введите 3 число "))
a4 = int(input(f"Введите 4 число "))
k = 0
for n in range(int(input("Сколько чисел будет? "))):
    if ((a1 == 0 or a1 == 1) and (a2 >= 0 and a2 < 10)) or (a1 == 2 and (a2 >= 0 and a2 < 5)):
        if (a3>= 0 and a3 < 7) and (a4 >= 0 and a4 < 10):
            print(f"{a1}{a2}:{a3}{a4}")
            k+=1
    a1,a2,a3,a4=a2,a3,a4,a1
    a4 = int(input("Введите следующие число последовательности "))
if ((a1 == 0 or a1 == 1) and (a2 >= 0 and a2 < 10)) or (a1 == 2 and (a2 >= 0 and a2 < 5)):
    if (a3>= 0 and a3 < 7) and (a4 >= 0 and a4 < 10):
        print(f"{a1}{a2}:{a3}{a4}")
        k+=1
print(f"Таких комбинаций {k}")
