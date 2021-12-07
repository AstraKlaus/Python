from tkinter import *

root = Tk()
root.title('OptionMenu')
root.geometry('400x300')
root.config(bg='#F26849')

def change_width(choice):
    choice = variable.get()
    label.config(width=choice)
def change_color(choice):
    choice = color.get()
    label.config(bg=choice)
def change_colorFG(choice):
    choice = colorFG.get()
    label.config(fg=choice)

width_size = [10, 20, 30, 40, 50]
colorsData = ["Green", "Black", "Yellow", "Pink", "Blue"]
colorsDataFG = ["Green", "Black", "Yellow", "Pink", "Blue"]


variable = IntVar()
color = StringVar()
colorFG = StringVar()

lb1 = Label(root, text = "Изменить размер окна:").pack(anchor = W)
dropdown = OptionMenu(
    root,
    variable,
    *width_size,
    command=change_width
).pack(anchor = W)
lb2 = Label(root, text = "Изменить фон:").pack(anchor = W)
colorPicker = OptionMenu(
    root,
    color,
    *colorsData,
    command=change_color
).pack(anchor = W)
lb3 = Label(root, text = "Изменить цвет текста:").pack(anchor = W)
colorPickerFG = OptionMenu(
    root,
    colorFG,
    *colorsDataFG,
    command=change_colorFG
).pack(anchor = W)


label = Label(root,text="Текст",width = 10,fg = "Black",bg="White")
label.pack(anchor = W)

root.mainloop()