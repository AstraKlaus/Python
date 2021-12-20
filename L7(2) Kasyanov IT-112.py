import random

n = int(input("How many cars?"))
speed = [round(random.uniform(20, 150), 2) for i in range(n)]
time = [round(random.uniform(0, 24), 2) for j in range(n)]
way = [k * p for k in speed for p in time]

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
