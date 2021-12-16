from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.geometry("340x130")
window.title('Инженерный калькулятор')
window.resizable(width = False, height = False)

def translate():
    stm = int(stm_combo_box.get())
    stm_new = int(stm_new_combo_box.get())
    num_10_entry.delete(0, "end")
    answer_entry.delete(0, "end")
    num = num_entry.get()
    fake = False
    for i in num[1:]:
        if i not in "1234567890.":
            fake = True
            break
    digitMax = 0
    for i in str(num):
        if i.isdigit():
            if int(i) > digitMax:
                digitMax = int(i)
    if num.count(".") < 2 and not fake and num[0] != '.' and digitMax < stm and num[0] in "-123456789":
        if num[0] != '-':
            if num.count(".") == 1:
                num = num.split(".")
                one_num = int(num[0])
                two_num = num[1]
                if two_num != '' or two_num != " ":
                    new_num_one = translate_cell_10(one_num, stm)
                    new_num_two = translate_vsh_10(two_num, stm)
                    num_10_entry.insert(0, str(new_num_one + new_num_two))
                    answer_entry.insert(0, str(
                        translate_cell_10_to(new_num_one, stm_new) + "." + translate_vsh_10_to(new_num_two, stm_new)))
                else:
                    num_10_entry.delete(0, "end")
                    answer_entry.delete(0, "end")
                    messagebox.showinfo('Информация', 'Ошибка')
            else:
                one_num = int(num)
                new_num_one = translate_cell_10(one_num, stm)
                num_10_entry.insert(0, str(new_num_one))
                answer_entry.insert(0, str(translate_cell_10_to(new_num_one, stm_new)))
        elif num[0] == '-':
            if num.count(".") == 1:
                num = num.split(".")
                one_num = int(num[0])
                two_num = num[1]
                if two_num != '' or two_num != " ":
                    dv_cell = int(translate_black_to_2(int(one_num), stm))
                    dv_vsh = int(translate_black_vsh_to_2(int(two_num), stm))
                    new_one_num = translate_cell_10(dv_cell, 2)
                    new_two_num = translate_vsh_10(str(dv_vsh), 2)
                    num_10_entry.insert(0, str(new_one_num + new_two_num))
                    answer_entry.insert(0, str(translate_cell_10_to(new_one_num, stm_new) + '.' + translate_vsh_10_to(new_two_num, stm_new)))
                else:
                    num_10_entry.delete(0, "end")
                    answer_entry.delete(0, "end")
                    messagebox.showinfo('Информация', 'Ошибка')
            else:
                one_num = int(num[1:])
                dv = int(translate_black_to_2(one_num, stm))
                num_10_entry.insert(0, translate_cell_10(dv, 2))
                answer_entry.insert(0, translate_10_to(translate_cell_10(dv, 2), stm_new))
        else:
            num_10_entry.delete(0, "end")
            answer_entry.delete(0, "end")
            messagebox.showinfo('Информация', 'Ошибка')

    else:
        num_10_entry.delete(0, "end")
        answer_entry.delete(0, "end")
        messagebox.showinfo('Информация', 'Ошибка')


def translate_cell_10(one_num, ss):
    new_one_num = 0
    i = 0
    while one_num != 0:
        new_one_num += one_num % 10 * ss ** i
        i += 1
        one_num //= 10
    return new_one_num


def translate_vsh_10(two_num, ss):
    new_two_num = 0
    i = 1
    while len(two_num) != 0:
        new_two_num += int(two_num[0]) * ss ** (i * (-1))
        two_num = two_num[1:]
        i += 1
    return float(str(new_two_num)[:6])


def translate_10_to(num, ss):
    new_num = ''
    while num != 0:
        new_num = str(num % ss) + new_num
        num //= ss
    return new_num


def translate_cell_10_to(one_num, ss):
    new_one_num = ''
    while one_num != 0:
        new_one_num = str(one_num % ss) + new_one_num
        one_num //= ss
    return new_one_num


def translate_vsh_10_to(two_num, ss):
    new_two_num = ''
    i = 0
    while i != 5:
        new_two_num += str(int((two_num * ss) // 1))
        two_num = (two_num * ss) % 1
        if two_num == 0:
            break
        i += 1
    return new_two_num


def translate_black_to_2(just_num, ss):
    cell_num = translate_cell_10(just_num, ss)
    bin_num = translate_cell_10_to(cell_num, 2)
    new_bin_num = ''
    for i in range(len(str(bin_num))):
        if str(bin_num)[i] == '1':
            new_bin_num += '0'
        else:
            new_bin_num += '1'
    return '1' + new_bin_num


def translate_black_vsh_to_2(two_num, ss):
    cell_two_num = translate_vsh_10(str(two_num), ss)
    bin_two_num = translate_vsh_10_to(cell_two_num, 2)
    new_bin_two_num = ''
    for i in range(len(str(bin_two_num))):
        if str(bin_two_num)[i] == '1':
            new_bin_two_num += '0'
        else:
            new_bin_two_num += '1'
    return new_bin_two_num


num_entry = Entry(window, font=(10), width=15)
num_entry.grid(row=0, column=0,  stick="wens")

variable = [i for i in range(2, 10)]  # [2, 3, 4, 5, 6, 7, 8, 9]
stm_combo_box = ttk.Combobox(window, values=variable, font=(1), width=5)  # ДОБАВЛЕНИЕ ЧИСЕЛ В КОМБОБОХ ИЗ МАССИВА variable
stm_combo_box.grid(row=0, column=1, stick="wens")

translate_button = Button(window, text="Перевести", command=translate, font=(10))
translate_button.grid(row=1, column=0, stick="wens")

answer_entry = Entry(window, font=(10), width=15)
answer_entry.grid(row=2, column=0,  stick="wens")

stm_new_combo_box = ttk.Combobox(window, values=variable, font=(10), width=5)  # ДОБАВЛЕНИЕ ЧИСЕЛ В КОМБОБОХ ИЗ МАССИВА variable
stm_new_combo_box.grid(row=2, column=1, stick="wens")

num_10_entry = Entry(window, font=(10), width=15)
num_10_entry.grid(row=4, column=0,  stick="wens")

dec_l = Label(window, text='Десятичная СС', font=(10))
dec_l.grid(row=4, column=1)

stairs = Canvas(window, width = 40, height = 40)
stairs.grid(row=1, column=1)

img = PhotoImage(file = 'down.png')
down = stairs.create_image(0, 20, anchor='w', image=img)

window.mainloop()
