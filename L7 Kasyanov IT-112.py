import random

def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


A = [-1, 19, 8, 12, 7, 17, 20, 11, 13, 4, 7, 1, 4, 5, 20, 1, 4, 9, 12, 18, 1, 3, 8, 7, 10, 11, 15, 5, 19, 7, 18, 15, 2, 7, 13, 8, 18, 5, 13, 6, 20, 4, 10, 13, 1, 2, 19, 18, 19, 17, 17, 12, 14, 8, 12, 4, 19, 7, 7, 8, 2, 16, 1, 8, 3, 9, 11,0, 9, 15, 15, 14, 9, 18, 15, 9, 20, 17, 18, 3, 12, 9, 8, 8, 3, 1, 3, 7, 15, 12, 2, 5, 4, 5, 7, 2, 12, 1, 4, 12, 6, 7, 6, 10, 9, 2, 3, 1, 8, 4, 17, 16, 10, 12, 12, 6, 12, 15, 1, 5, 16, 17, 1, 20, 13, 11, 18, 15, 20, 16, 20, 3, 6, 16, 15, 10, 16, 6, 17, 4, 16, 10, 17, 20, 18, 10, 13, 1, 16, 2, 2, 14, 20, 10, 18, 6, 5, 11, 5, 6, 9, 11, 15, 14, 11, 2, 17, 3, 9, 12, 7, 15, 7, 7, 7, 14, 10, 13, 18, 7, 14, 17, 9, 10, 10, 5, 2, 9, 16, 10, 2, 13, 14, 3, 14, 2, 6, 6, 14, 11, 1, 1, 8, 9, 6, 13, 16, 13, 14, 12, 16, 3, 10, 11, 17, 6, 11,30]
#1
#a
summary = 0
for i in range(len(A)-1):
    if i % 2 == 0 and A[i] % 2 == 0:
        summary += A[i]
print(f"Сумма всех чётных элементов массива, стоящих на чётных местах, то есть имеющие чётные номера {summary}")
#b
summary_1 = 1
summary_2 = 0
for i in range(5):
    summary_1 *= A[i]
    summary_2 += A[i]
print(f"Сумма {summary_2} произведение первых пяти элементов массива {summary_1}")
#c
k1 = k2 = -1
while k1 < 0 and k2 > len(A) and k1 > k2:
    k1 = int(input("Введите левую границу (к1)"))
    k2 = int(input("Введите правую границу (к2)"))
summary = 0
for i in range(k1,k2+1):
    summary += A[i]
print(f"Сумма элементов с к1 по к2 {summary}")

#d
summary = 0
maximus = int(input("Введите число А"))
for i in range(len(A)-1):
    if A[i] > maximus:
        summary += A[i]
print(f"Сумма элементов, больших данного числа А {summary}")
#e
summary = 0
k1 = k2 = -1
while k1 < 0 and k2 > len(A) and k1 > k2:
    k1 = int(input("Введите левую границу (А)"))
    k2 = int(input("Введите правую границу (В)"))

for i in range(k1,k2+1):
    summary += A[i]
print(f"Сумма элементов с А по В {summary}")

#2
#a
for i in range(len(A)-1):
    if A[i] < 0:
        print(f"Номер отрицательного числа {i} само число {A[i]}")

#b
maximus = 0
for i in range(len(A)-1):
    if A[i] > maximus:
        maximus = A[i]
print("Номерa всех элементов с максимальным значением ",end="")
for i in range(len(A)-1):
    if A[i] == maximus:
        print(i,end=" ")
#c
count = 0
print()
print("Номерa всех элементов кратные 3 или 5 ",end="")
for i in range(len(A)-1):
    if A[i] % 3 == 0 or A[i] % 5 == 0:
        count += 1
        print(i,end=" ")
print("Их ", count)
#3
count = 0
power = 1
summary = 0
for i in range(len(A)-1):
    if A[i] < 0:
        power *= A[i]
        count += 1
        summary += A[i]
print(f"Количество {count} и произведение отрицательных элементов {power}, а также суммa нечетных элементов {summary}")


maximus = 0
minimus = 10**4
for i in range(len(A)-1):
    if A[i] > maximus:
        maximus = i
    if A[i] < minimus:
        minimus = i
B = []
B.append(A[:minimus])
B.append(A[minimus:maximus:-1])
B.append(A[maximus:])
print("Измененный массив: ", B)

n = 5
b = []
for i in range(2*n+1):
    b.append(i)
for i in range(n+1):
    b.append(i)
print("Измененный массив: ", b)

delete = int(input("Какой элемент удалить? "))
B[delete] = random.randint(1,20)

k = int(input("С какого элемента перевернуть список? "))
print(f"{A[:k]}{A[:k:-1]}")











