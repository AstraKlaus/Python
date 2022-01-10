from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import random

root = Tk()
root.geometry("400x550")


def pressToLess(number):
    if number == 1:
        lesson = Toplevel(root, width=350, height=550)

        name = Label(lesson, text="Звезда по имени солнце", font=("Times new roman", 16))
        name.pack()

        canvas = Canvas(lesson, width=300, height=100)
        canvas.pack()
        frameForAccords = LabelFrame(canvas, text="Аккорды", width=300, height=100)
        frameForAccords.pack()
        scrollbar = Scrollbar(canvas, orient=HORIZONTAL, bg = "blue")
        canvas.config(xscrollcommand=scrollbar.set)
        scrollbar.config(command=canvas.xview)
        scrollbar.pack(side=BOTTOM)

        """
        imageBoy = PhotoImage('Бой.png')
        boy = Button(frameForAccords, image=imageBoy, width=30, height=10)
        boy.pack()

        imageAm = PhotoImage('am.png' )
        accordAm = Button(frameForAccords, image=imageAm, width=30, height=10)
        accordAm.pack(side= RIGHT)

        imageDm = PhotoImage('dm.png')
        accordDm = Button(frameForAccords, image=imageDm, width=30, height=10)
        accordDm.pack(side= RIGHT)

        imageC = PhotoImage('c.png')
        accordC = Button(frameForAccords, image=imageC, width=30, height=10)
        accordC.pack(side= RIGHT)

        imageG = PhotoImage('g.png')
        accordG = Button(frameForAccords, image=imageG, width=30, height=10)
        accordG.pack(side= RIGHT)
        """

        textOfSong = Frame(lesson, width=300, height=100)
        textOfSong.pack()
        canvasForText = Canvas(textOfSong, width=300, height=100, scrollregion = canvas.bbox("all"))
        canvasForText.pack()
        textOfSong = Label(canvasForText,text = songsData[0], width=300, height=100)
        textOfSong.pack()
        scrollbarForText = Scrollbar(textOfSong, orient=VERTICAL, bg="blue")
        textOfSong.config(yscrollcommand=scrollbarForText.set)
        scrollbarForText.config(command=canvasForText.yview)
        scrollbarForText.pack(side=RIGHT)







numberOfLesson = IntVar()
but = Button(root, text="Lesson", textvariable=numberOfLesson, command = lambda: pressToLess(1))
but.pack()

songsData = ["""Am(4)
Белый снег, серый лед,
　　　　C(4) 
На растрескавшейся земле. 
　Dm(4)
Одеялом лоскутным на ней -
G(4)
Город в дорожной петле.
　　　Am(4)
А над городом плывут облака,
　　C(4)
Закрывая небесный свет.
　　　 Dm(4) 
А над городом - желтый дым,
G(4)
Городу две тысячи лет,
　Dm(4)
Прожитых под светом Звезды
　　　　Am (4) 
По имени Солнце...

"""]

root.mainloop()
