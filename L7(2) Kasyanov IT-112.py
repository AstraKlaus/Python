import random

def spacing(sal):
    general = int(round(sal // 1, 0))
    extra = int(round((sal % 1) * 100, 0))
    if general < 1000:
        return '{} руб. {} коп.'.format(str(general), extra)
    else:
        return '{} {} руб. {} коп.'.format(general // 1000, str(general)[-3::], extra)

n = int(input("How many cars? "))
speed = [round(random.uniform(20, 150), 2) for i in range(n)]
time = [round(random.uniform(0, 24), 2) for j in range(n)]
way = [round(speed[k] * time[k], 2) for k in range(len(speed))]

print(f"Данные о скорости: {speed} \nДанные о времени: {time} \nДанные о пути: {way}")

mid_speed = 0
for i in speed:
    mid_speed += i
mid_speed = round(mid_speed / len(speed), 2)

mid_time = 0
for i in time:
    mid_time += i
mid_time = round(mid_time / len(time), 2)

mid_way = 0
for i in way:
    mid_way += i
mid_way = round(mid_way / len(way), 2)

lowest = []
middle = []
highest = []

for i in range(len(speed)):
    if speed[i] < mid_speed and time[i] < mid_time and way[i] < mid_way:
        lowest.append(i + 1)
    elif speed[i] > mid_speed and time[i] > mid_time and way[i] > mid_way:
        middle.append(i + 1)
    else:
        highest.append(i + 1)

print(f"Средняя скорость: {mid_speed}\nСреднее время: {mid_time}\nСреднее расстояние: {mid_way}\n")

print(f"Первая группа (номера машин): {lowest}\nВторая группа (номера машин): {middle}\nТретья группа (номера машин): {highest}\n")


orders = [random.randint(1, 100) for i in range(72*3+1)]
positions = [f"Продукт №{i}" for i in range(1, 72*3+2)]
costs = [round(random.uniform(1, 100), 2) for i in range(72*3+1)]

print(f"Дано: \nЗаказы: {orders}\nТовар: {positions}\nЦены: {costs}\n\nВывод программы:\nСмета")

tax = 0
summary_1 = 0
summary_2 = 0
summary_3 = 0
for number in range(0, len(orders)-1, 3):
    company = 1 if number < 72 else 2 if number < 144 else 3
    tax = (tax) % 24 + 1
    print(f"{company} Компания\nЗазказ {tax}\n{positions[number]} - {orders[number]} шт. по {costs[number]} = {spacing(orders[number]*costs[number])}\n"
          f"{positions[number+1]} - {orders[number+1]} шт. по {costs[number+1]} = {spacing(orders[number+1]*costs[number+1])}\n"
          f"{positions[number+2]} - {orders[number+2]} шт. по {costs[number+2]} = {spacing(orders[number+2]*costs[number+2])}\n"
          f"Всего с {tax} заказа {spacing(orders[number]*costs[number]+orders[number+1]*costs[number+1]+orders[number+2]*costs[number+2])}")
    if number < 73:
        for i in range(len(orders)):
            summary_1 += orders[number]*costs[number]+orders[number+1]*costs[number+1]+orders[number+2]*costs[number+2]
    if number == 69:
        print(f"Всего с компании I {spacing(summary_1)}")
    if 145 > number > 73:
        for i in range(len(orders)):
            summary_2 += orders[number]*costs[number]+orders[number+1]*costs[number+1]+orders[number+2]*costs[number+2]
    if number == 141:
        print(f"Всего с компании II {spacing(summary_2)}")
    if number > 145:
        for i in range(len(orders)):
            summary_3 += orders[number]*costs[number]+orders[number+1]*costs[number+1]+orders[number+2]*costs[number+2]
    if number >210:
        print(f"Всего с компании III {spacing(summary_3)}")

print(f"\nВсего со всех компаний {spacing(summary_1 + summary_2 + summary_3)}")