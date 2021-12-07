from tkinter import *
import time

def body():
    label.config(text = "")
    label1.config(text = "")
    label2.config(text = "")
    if var.get() == 1:
        label.config(text = "Зеленый", fg = "green")
        cir = c.create_oval(10,70,60,20, fill = "green")
        cir1 = c.create_oval(10,70,60,120, fill = "gray")
        cir2 = c.create_oval(10,120,60,170, fill = "gray")
        while label['text'] == "Зеленый":
            for i in range(400):
                if road.bbox(car2)[0] == 300:
                    if road.bbox(car1)[0] < 300:
                        if label['text'] == "Зеленый":
                            road.move(car1,1,0)
                            root.update()
                            time.sleep(0.005)
                    else:
                        road.move(car1, -400, 0)
                        root.update()
                        break
                else: continue
            for i in range(400):
                if road.bbox(car2)[0] > - 100:
                    if label['text'] == "Зеленый":
                        road.move(car2,-1,0)
                        root.update()
                        time.sleep(0.005)
                else:
                    road.move(car2, 400, 0)
                    root.update()
                    break
    if var.get() == 2:
        label1.config(text = "Желтый", fg = "yellow")
        cir = c.create_oval(10,70,60,20, fill = "gray")
        cir1 = c.create_oval(10,70,60,120, fill = "yellow")
        cir2 = c.create_oval(10,120,60,170, fill = "gray")
    if var.get() == 3:
        label2.config(text = "Красный", fg = "red")
        cir = c.create_oval(10,70,60,20, fill = "gray")
        cir1 = c.create_oval(10,70,60,120, fill = "gray")
        cir2 = c.create_oval(10,120,60,170, fill = "red")

root = Tk()
root.geometry("300x400")
root.resizable(width = False, height = False)
root.config(bg = "lavender")
var = IntVar()
c = Canvas(root,width = 70, height = 190, bg = "black")
c.pack(anchor = W)
cir = c.create_oval(10,70,60,20, fill = "green")
cir1 = c.create_oval(10,70,60,120, fill = "yellow")
cir2 = c.create_oval(10,120,60,170, fill = "red")
road = Canvas(root,width = 370, height = 50, bg = "black")
road.pack(anchor = W)
img1 = PhotoImage(file = 'car1.png')
img2 = PhotoImage(file = 'car2.png')
car1 = road.create_image(-100,10, anchor='nw',image=img1)
car2 = road.create_image(300,10, anchor='nw',image=img2)

rb1 = Radiobutton(text = "  \n  ",bg="green",variable = var, value = 1, command = body)
rb1.pack(anchor = W)
rb2 = Radiobutton(text = "  \n  ",bg="yellow",variable = var, value = 2, command = body)
rb2.pack(anchor = W)
rb3 = Radiobutton(text = "  \n  ",bg="red",variable = var, value = 3, command = body)
rb3.pack(anchor = W)

label = Label(root, bg = "lavender", font="Times 14")
label.place(x = 120, y = 45, anchor = CENTER)
label1 = Label(root, bg = "lavender", font="Times 14")
label1.place(x = 120, y = 95, anchor = CENTER)
label2 = Label(root, bg = "lavender", font="Times 14")
label2.place(x = 120, y = 145, anchor = CENTER)

root.mainloop()