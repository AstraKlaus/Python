from tkinter import *

tk = Tk()
tk.geometry("400x455")
tk.resizable(width= False, height= False)
tk.title("Калькулятор")

def btn_click(item):
    global answer
    if len(answer) == 0:
        if item not in ['/','*','**','.','-','+']:
            answer = answer + str(item)
            textvariable.set(answer)
            return
        else: return
    if item == '.':
        try:
            result = eval(answer+item)
            answer = answer + str(item)
            textvariable.set(answer)
        except: return
    if answer[-1] not in ['/','*','**','.','-','+']:
        answer = answer + str(item)
        textvariable.set(answer)
    elif answer[-1] in ['/','*','**','.','-','+'] and item not in ['/','*','**','.','-','+']:
        answer = answer + str(item)
        textvariable.set(answer)
    else: return

def btn_sqrt():
    global answer
    if eval(answer) > 0:
        result = str(round(float(eval(answer + "**0.5")),2))
        textvariable.set(result)
        answer = result
    return

def bt_clear():
    global answer
    answer = ""
    textvariable.set("")

def bt_equal():
    global answer
    result = str(round(float(eval(entry.get())),2))
    textvariable.set(result)
    answer = result

answer = ""
textvariable = StringVar()
frame = Frame(tk, width=300, height=50, highlightbackground="black", highlightcolor="black",
                     padx=2, pady=2)

frame.pack()
entry = Entry(frame, font=('arial', 20, 'bold'), textvariable=textvariable, width=50, highlightbackground="black",
                    justify=RIGHT)

entry.grid(row=0, column=0)
entry.pack(ipady=10)
frame_bt = Frame(tk, width=300, height=270, highlightbackground="grey")
frame_bt.pack()
clear = Button(frame_bt, text="C", fg="black", width=10, height=3,  highlightbackground="black",
               command=lambda: bt_clear()).grid(row=0, column=0, padx=1, pady=1)

sqrt = Button(frame_bt, text="sqrt", fg="black", width=10, height=3,  highlightbackground="black",
               command=lambda: btn_sqrt()).grid(row=0, column=1, padx=1, pady=1)

square = Button(frame_bt, text="^", fg="black", width=10, height=3,  highlightbackground="black",
                command=lambda: btn_click("**")).grid(row=0, column=2, padx=1, pady=1)

divide = Button(frame_bt, text="/", fg="black", width=10, height=3,  highlightbackground="black",
                command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)



seven = Button(frame_bt, text="7", fg="black", width=10, height=3,  highlightbackground="black",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

eight = Button(frame_bt, text="8", fg="black", width=10, height=3,  highlightbackground="black",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

nine = Button(frame_bt, text="9", fg="black", width=10, height=3,  highlightbackground="black",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

power = Button(frame_bt, text="*", fg="black", width=10, height=3,  highlightbackground="black",
                  command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)


four = Button(frame_bt, text="4", fg="black", width=10, height=3,  highlightbackground="black",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

five = Button(frame_bt, text="5", fg="black", width=10, height=3,  highlightbackground="black",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

six = Button(frame_bt, text="6", fg="black", width=10, height=3,  highlightbackground="black",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(frame_bt, text="-", fg="black", width=10, height=3,  highlightbackground="black",
               command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)


one = Button(frame_bt, text="1", fg="black", width=10, height=3,  highlightbackground="black",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

two = Button(frame_bt, text="2", fg="black", width=10, height=3, highlightbackground="black",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

three = Button(frame_bt, text="3", fg="black", width=10, height=3,  highlightbackground="black",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(frame_bt, text="+", fg="black", width=10, height=3,  highlightbackground="black",
              command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)


zero = Button(frame_bt, text="0", fg="black", width=24, height=3,  highlightbackground="black",
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

dot = Button(frame_bt, text=".", fg="black", width=10, height=3,  highlightbackground="black",
               command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(frame_bt, text="=", fg="black", width=10, height=3,  highlightbackground="black",
                command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

tk.mainloop()
