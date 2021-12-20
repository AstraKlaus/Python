import random

n = int(input("How many cars? "))
speed = [round(random.uniform(20, 150), 2) for i in range(n)]
time = [round(random.uniform(0, 24), 2) for j in range(n)]
way = [round(speed[k] * time[k],2) for k in range(len(speed))]

print(f"Данные о скорости: {speed} \nДанные о времени: {time} \nДанные о пути: {way}")

mid_speed = 0
for i in speed:
    mid_speed += i
mid_speed = round(mid_speed / len(speed), 2)

mid_time = 0
for i in speed:
    mid_time += i
mid_time = round(mid_time / len(time), 2)

mid_way = 0
for i in speed:
    mid_way += i
mid_way = round(mid_way / len(way), 2)

lowest = []
middle = []
highest = []

for i in range(len(speed)):
    if speed[i] < mid_speed and time[i] < mid_time and way[i] < mid_way:
        lowest.append(i+1)
    elif speed[i] > mid_speed and time[i] > mid_time and way[i] > mid_way:
        middle.append(i+1)
    else: highest.append(i+1)

print(f"Средняя скорость: {mid_speed}\nСреднее время: {mid_time}\nСреднее расстояние: {mid_way}\n")

print(f"Первая группа (номера машин): {lowest}\nВторая группа (номера машин): {middle}\nТретья группа (номера машин): {highest}")



