a,b,c,d = map(int, input('Введите через пробел углы четырехугольника: ').split())
if (a + b + c + d) == 360:
    if (a + b == 180 and c + d == 180 and (a + c) != 180 and (b + d) != 180 and (a + d) != 180 and (b + c) != 180) or (a + c == 180 and b + d == 180 and (a + b) != 180 and (b + c) != 180 and (a + d) != 180 and (c + d) != 180) or (a + d == 180 and c + b == 180and (a + d) != 180 and (c + d) != 180and (a + c) != 180 and (b + d) != 180):
       print("Возможно")
    elif (a == b and a != c and a != d and c == d) or (a == c and a != b and a != d and b == d) or (a == d and a != c and a != b and c == b):
        print("Возможно, но это может быть и параллелограм")
    elif (a == 90 and a == b and a != c and a != d) or (a == 90 and a == c and b != c and a != d) or (a == 90 and a == d and a != c and a != b):
        print("Возможно")
    else: print("Это не трапеция")
else:
    print("Данные углы не образуют четырехугольник")

a,b,c = map(int, input('Введите через пробел тройку чисел: ').split())
char1 = 0
char2 = 0
char3 = 0
for i1 in a,b,c:
    for i2 in a,b,c:
        for i3 in a,b,c:
            if i1 != i2 and i1 != i3 and i2 != i3:
                if i1>i2 and i1 > i3:
                    char1 = i1
                    if i2 < i3:
                        char3 = i2
                        char2 = i3
                    else:
                        char2 = i2
                        char3 = i3
                if i2>i1 and i2 > i3:
                    char1 = i2
                    if i1 < i3:
                        char3 = i1
                        char2 = i3
                    else:
                        char2 = i1
                        char3 = i3
                if i3>i2 and i3 > i1:
                    char1 = i3
                    if i2 < i1:
                        char3 = i2
                        char2 = i1
                    else:
                        char2 = i2
                        char3 = i1
                if (((char1 / char2) == (char2 / char3)) or ((char2 / char1) == (char1 / char3)) or ((char1 / char3) == (char3 / char2))) and (char1 / char2) != 1 and (char1 // char2) != 0:
                    print(f"Тройка чисел {char3,char2,char1}")
