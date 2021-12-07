from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.geometry("400x555")
tk.resizable(width=False, height=False)
tk.title("Калькулятор")


def btn_click(item):
    global answer
    global charmax
    if item in ['-', '+']:
        if str(textvariable.get())[0] in ['-', '+']:
            answer = item + answer[1:]
            textvariable.set(item + answer[1:])
        return
    if item == '.':
        try:
            result = eval(answer + item)
            answer = answer + str(item)
            textvariable.set(answer)
        except:
            return
    if item not in ['/', '*', '**', '.', '-', '+']:
        answer = answer + str(item)
        textvariable.set(answer)
        if charmax < int(item):
            charmax = int(item)


def bt_clear():
    global answer
    global charmax
    answer = "+"
    textvariable.set("+")
    charmax = 0


def convert():
    if len(textvariable.get()) > 1:
        if charmax > int(variable.get()):
            if eval(textvariable.get()) % 1 == 0:
                num = eval(textvariable.get())
                base = int(variable.get())
                newNum = ""
                while num > 0:
                    newNum = str(num % base) + newNum
                    num //= base
                textvar.set(newNum)
            else:
                num = eval(textvariable.get())
                base = int(variable.get())
                generalnum = int(num // 1)
                newNum = ""
                while generalnum > 0:
                    newNum = str(generalnum % base) + newNum
                    generalnum //= base
                num = eval(textvariable.get())
                extranum = round(num%1,8)
                #extranum *= 10* (len(str(extranum))-2)
                base = int(variable.get())
                newNum += "."
                print(num,generalnum,extranum,base,newNum,end="\n")
                while extranum%1 != 0:
                    extranum *= base
                    newNum += str(int(extranum//1))
                    print(extranum,newNum,end="\n")
                textvar.set(newNum)
        else: messagebox.showinfo("Информация", "Невозможно перевести в эту систему счисления")
charmax = 0
answer = "+"
textvariable = StringVar()
textvariable.set(answer)
frame = Frame(tk, width=300, height=50, highlightbackground="black", highlightcolor="black",
              padx=2, pady=2)

frame.pack()
entry = Entry(frame, font=('arial', 20, 'bold'), textvariable=textvariable, width=50, highlightbackground="black",
              justify=RIGHT)

entry.grid(row=0, column=0)
entry.pack(ipady=10)
frame_bt = Frame(tk, width=300, height=270, highlightbackground="grey")
frame_bt.pack()
clear = Button(frame_bt, text="C", fg="black", width=10, height=3, highlightbackground="black",
               command=lambda: bt_clear()).grid(row=0, column=2, padx=1, pady=1)

seven = Button(frame_bt, text="7", fg="black", width=10, height=3, highlightbackground="black",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(frame_bt, text="8", fg="black", width=10, height=3, highlightbackground="black",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(frame_bt, text="9", fg="black", width=10, height=3, highlightbackground="black",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

four = Button(frame_bt, text="4", fg="black", width=10, height=3, highlightbackground="black",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(frame_bt, text="5", fg="black", width=10, height=3, highlightbackground="black",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(frame_bt, text="6", fg="black", width=10, height=3, highlightbackground="black",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(frame_bt, text="-", fg="black", width=10, height=3, highlightbackground="black",
               command=lambda: btn_click("-")).grid(row=0, column=1, padx=1, pady=1)

one = Button(frame_bt, text="1", fg="black", width=10, height=3, highlightbackground="black",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(frame_bt, text="2", fg="black", width=10, height=3, highlightbackground="black",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(frame_bt, text="3", fg="black", width=10, height=3, highlightbackground="black",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(frame_bt, text="+", fg="black", width=10, height=3, highlightbackground="black",
              command=lambda: btn_click("+")).grid(row=0, column=0, padx=1, pady=1)

zero = Button(frame_bt, text="0", fg="black", width=24, height=3, highlightbackground="black",
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

dot = Button(frame_bt, text=".", fg="black", width=10, height=3, highlightbackground="black",
             command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)


lb1 = Label(frame_bt,text="В какую систему счисления перевести?: ").grid(row=5, columnspan=3, padx=1, pady=1)
variable = IntVar()
width_size = [2, 3, 4, 5, 6, 7, 8, 9]
variable.set(2)
dropdown = OptionMenu(
    frame_bt,
    variable,
    *width_size
).grid(row=6, column=0, padx=1, pady=1)
otvet = Button(frame_bt, text="Перевести", fg="black", width=10, height=1, highlightbackground="black",
             command=lambda: convert()).grid(row=6, column=1, padx=1, pady=1)
textvar = StringVar()
lb2 = Label(frame_bt, text="Ответ: ", textvariable = textvar).grid(row=7, columnspan=3, padx=1, pady=1)

tk.mainloop()
