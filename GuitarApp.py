from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
import pygame
import random
from tkinter import messagebox


def pressToLess(number):
    if number == 1:
        lesson = Toplevel(root, width=500, height=550, bg="#f4fef6")

        name = Label(lesson, text="Урок 1: 'Звезда по имени солнце'", font=("Times new roman", 16, "italic"),
                     bg="#f4fef6")
        name.pack(side=TOP)

        complete = Checkbutton(lesson, text="Урок выполнен", justify=RIGHT,
                               fg=f"{'red' if answer.get() == 0 else 'green'}",
                               variable=answer, offvalue=0, onvalue=1,
                               command=lambda: complete.config(fg=f"{'red' if answer.get() == 0 else 'green'}"),
                               bg="#f4fef6", activebackground="#f4fef6")

        complete.pack(side=TOP)

        canvasForAccords = LabelFrame(lesson, height=200, width=500, bg="#f4fef6")
        canvasForAccords.pack()

        AccordBoy = Button(canvasForAccords, image=imageBoy, relief=RIDGE)
        AccordBoy.grid(row=0, column=0)

        AccordAm = Button(canvasForAccords, image=imageAm, relief=RIDGE)
        AccordAm.grid(row=0, column=1)

        AccordC = Button(canvasForAccords, image=imageC, relief=RIDGE)
        AccordC.grid(row=0, column=2)

        AccordDm = Button(canvasForAccords, image=imageDm, relief=RIDGE)
        AccordDm.grid(row=1, column=0)

        AccordG = Button(canvasForAccords, image=imageG, relief=RIDGE)
        AccordG.grid(row=1, column=1)

        frameForMusic = Frame(lesson, bg="#f4fef6")
        frameForMusic.pack()

        songName = Label(frameForMusic, text="Прослушать песню", font=("Times new roman", 14), bg="#f4fef6")
        songName.pack(side=LEFT, anchor="n")

        rewindMusic = Button(frameForMusic, image=imageRewind, command=lambda: rewind(1), bg="#f4fef6")
        rewindMusic.pack(side=RIGHT, anchor="ne")

        stopSong = Button(frameForMusic, image=imageStop, command=stop, bg="#f4fef6")
        stopSong.pack(side=RIGHT, anchor="ne")

        playSong = Button(frameForMusic, image=imagePlay, command=lambda: play(1), bg="#f4fef6")
        playSong.pack(side=RIGHT, anchor="ne")

        generalname = Label(lesson, text="Текст песни: ", font=("Times new roman", 16, "bold"), bg="#f4fef6")
        generalname.pack(side=TOP)

        e = Text(lesson, width=50, height=20, bg="#f4fef6")
        e.insert(1.0, songsData[0])
        e.pack(side=LEFT)
        e.config(state=DISABLED)

        scroll = Scrollbar(lesson, command=e.yview)
        scroll.pack(side=RIGHT, fill=Y)

        e.config(yscrollcommand=scroll.set)

    if number == 2:
        lesson = Toplevel(root, width=500, height=550, bg="#f4fef6")

        name = Label(lesson, text="Урок 2: 'Просвистела'", font=("Times new roman", 16, "italic"), bg="#f4fef6")
        name.pack(side=TOP)

        complete = Checkbutton(lesson, text="Урок выполнен", justify=RIGHT,
                               fg=f"{'red' if answer2.get() == 0 else 'green'}",
                               variable=answer2, offvalue=0, onvalue=1,
                               command=lambda: complete.config(fg=f"{'red' if answer2.get() == 0 else 'green'}"),
                               bg="#f4fef6", activebackground="#f4fef6")
        complete.pack(side=TOP)

        canvasForAccords = LabelFrame(lesson, height=200, width=500, bg="#f4fef6")
        canvasForAccords.pack()

        AccordBoy = Button(canvasForAccords, image=imageBoy2, relief=RIDGE)
        AccordBoy.grid(row=0, column=0)

        AccordAm = Button(canvasForAccords, image=imageEm, relief=RIDGE)
        AccordAm.grid(row=0, column=1)

        AccordC = Button(canvasForAccords, image=imageC, relief=RIDGE)
        AccordC.grid(row=0, column=2)

        AccordH7 = Button(canvasForAccords, image=imageH7, relief=RIDGE)
        AccordH7.grid(row=1, column=0)

        AccordG = Button(canvasForAccords, image=imageG, relief=RIDGE)
        AccordG.grid(row=1, column=1)

        frameForMusic = Frame(lesson, bg="#f4fef6")
        frameForMusic.pack()

        songName = Label(frameForMusic, text="Прослушать песню", font=("Times new roman", 14), bg="#f4fef6")
        songName.pack(side=LEFT, anchor="n")

        rewindMusic = Button(frameForMusic, image=imageRewind, command=lambda: rewind(2), bg="#f4fef6")
        rewindMusic.pack(side=RIGHT, anchor="ne")

        stopSong = Button(frameForMusic, image=imageStop, command=stop, bg="#f4fef6")
        stopSong.pack(side=RIGHT, anchor="ne")

        playSong = Button(frameForMusic, image=imagePlay, command=lambda: play(2), bg="#f4fef6")
        playSong.pack(side=RIGHT, anchor="ne")

        generalname = Label(lesson, text="Текст песни: ", font=("Times new roman", 16, "bold"), bg="#f4fef6")
        generalname.pack(side=TOP)

        e = Text(lesson, width=50, height=20, bg="#f4fef6")
        e.insert(1.0, songsData[1])
        e.pack(side=LEFT)
        e.config(state=DISABLED)

        scroll = Scrollbar(lesson, command=e.yview)
        scroll.pack(side=RIGHT, fill=Y)

        e.config(yscrollcommand=scroll.set)
    if number == 3:
        lesson = Toplevel(root, width=500, height=550, bg="#f4fef6")

        name = Label(lesson, text="Урок 3: 'Лирика'", font=("Times new roman", 16, "italic"), bg="#f4fef6")
        name.pack(side=TOP)

        complete = Checkbutton(lesson, text="Урок выполнен", justify=RIGHT,
                               fg=f"{'red' if answer3.get() == 0 else 'green'}",
                               variable=answer3, offvalue=0, onvalue=1,
                               command=lambda: complete.config(fg=f"{'red' if answer3.get() == 0 else 'green'}"),
                               bg="#f4fef6", activebackground="#f4fef6")
        complete.pack(side=TOP)

        canvasForAccords = LabelFrame(lesson, height=200, width=500, bg="#f4fef6")
        canvasForAccords.pack()

        AccordBoy = Button(canvasForAccords, image=imageBoy7, relief=RIDGE)
        AccordBoy.grid(row=0, column=0)

        AccordAm = Button(canvasForAccords, image=imageAm, relief=RIDGE)
        AccordAm.grid(row=0, column=1)

        AccordC = Button(canvasForAccords, image=imageTonal, relief=RIDGE)
        AccordC.grid(row=0, column=2, rowspan=2)

        AccordH7 = Button(canvasForAccords, image=imageG, relief=RIDGE)
        AccordH7.grid(row=1, column=0)

        AccordG = Button(canvasForAccords, image=imageDm, relief=RIDGE)
        AccordG.grid(row=1, column=1)

        frameForMusic = Frame(lesson, bg="#f4fef6")
        frameForMusic.pack()

        songName = Label(frameForMusic, text="Прослушать песню", font=("Times new roman", 14), bg="#f4fef6")
        songName.pack(side=LEFT, anchor="n")

        rewindMusic = Button(frameForMusic, image=imageRewind, command=lambda: rewind(3), bg="#f4fef6")
        rewindMusic.pack(side=RIGHT, anchor="ne")

        stopSong = Button(frameForMusic, image=imageStop, command=stop, bg="#f4fef6")
        stopSong.pack(side=RIGHT, anchor="ne")

        playSong = Button(frameForMusic, image=imagePlay, command=lambda: play(3), bg="#f4fef6")
        playSong.pack(side=RIGHT, anchor="ne")

        generalname = Label(lesson, text="Текст песни: ", font=("Times new roman", 16, "bold"), bg="#f4fef6")
        generalname.pack(side=TOP)

        e = Text(lesson, width=50, height=20, bg="#f4fef6")
        e.insert(1.0, songsData[2])
        e.pack(side=LEFT)
        e.config(state=DISABLED)

        scroll = Scrollbar(lesson, command=e.yview)
        scroll.pack(side=RIGHT, fill=Y)

        e.config(yscrollcommand=scroll.set)
    if number == 4:
        lesson = Toplevel(root, width=500, height=550, bg="#f4fef6")

        name = Label(lesson, text="Урок 4: 'Мое сердце'", font=("Times new roman", 16, "italic"), bg="#f4fef6")
        name.pack(side=TOP)

        complete = Checkbutton(lesson, text="Урок выполнен", justify=RIGHT,
                               fg=f"{'red' if answer4.get() == 0 else 'green'}",
                               variable=answer4, offvalue=0, onvalue=1,
                               command=lambda: complete.config(fg=f"{'red' if answer4.get() == 0 else 'green'}"),
                               bg="#f4fef6", activebackground="#f4fef6")
        complete.pack(side=TOP)

        canvasForAccords = LabelFrame(lesson, height=200, width=500, bg="#f4fef6")
        canvasForAccords.pack()

        AccordBoy = Button(canvasForAccords, image=imageBoy, relief=RIDGE)
        AccordBoy.grid(row=0, column=0)

        AccordAm = Button(canvasForAccords, image=imageG, relief=RIDGE)
        AccordAm.grid(row=0, column=1)

        AccordC = Button(canvasForAccords, image=imagePerebor, relief=RIDGE)
        AccordC.grid(row=0, column=2, rowspan=2)

        AccordH7 = Button(canvasForAccords, image=imageG, relief=RIDGE)
        AccordH7.grid(row=1, column=0)

        AccordG = Button(canvasForAccords, image=imageEm, relief=RIDGE)
        AccordG.grid(row=1, column=1)

        frameForMusic = Frame(lesson, bg="#f4fef6")
        frameForMusic.pack()

        songName = Label(frameForMusic, text="Прослушать песню", font=("Times new roman", 14), bg="#f4fef6")
        songName.pack(side=LEFT, anchor="n")

        rewindMusic = Button(frameForMusic, image=imageRewind, command=lambda: rewind(4), bg="#f4fef6")
        rewindMusic.pack(side=RIGHT, anchor="ne")

        stopSong = Button(frameForMusic, image=imageStop, command=stop, bg="#f4fef6")
        stopSong.pack(side=RIGHT, anchor="ne")

        playSong = Button(frameForMusic, image=imagePlay, command=lambda: play(4), bg="#f4fef6")
        playSong.pack(side=RIGHT, anchor="ne")

        generalname = Label(lesson, text="Текст песни: ", font=("Times new roman", 16, "bold"), bg="#f4fef6")
        generalname.pack(side=TOP)

        e = Text(lesson, width=50, height=20, bg="#f4fef6")
        e.insert(1.0, songsData[3])
        e.pack(side=LEFT)
        e.config(state=DISABLED)

        scroll = Scrollbar(lesson, command=e.yview)
        scroll.pack(side=RIGHT, fill=Y)

        e.config(yscrollcommand=scroll.set)


def play(choose):
    if isPlaying:
        if choose == 1:
            pygame.mixer.music.load("Звезда по имени солнце.mp3")
            pygame.mixer.music.play(loops=0)
        elif choose == 2:
            pygame.mixer.music.load("Просвистела.mp3")
            pygame.mixer.music.play(loops=0)
        elif choose == 3:
            pygame.mixer.music.load("Лирика.mp3")
            pygame.mixer.music.play(loops=0)
        elif choose == 4:
            pygame.mixer.music.load("Мое сердце.mp3")
            pygame.mixer.music.play(loops=0)
    else:
        pygame.mixer.music.unpause()


def stop():
    global isPlaying
    isPlaying = False
    pygame.mixer.music.pause()


def rewind(choose):
    global isPlaying
    isPlaying = True
    if choose == 1:
        pygame.mixer.music.load("Звезда по имени солнце.mp3")
    elif choose == 2:
        pygame.mixer.music.load("Просвистела.mp3")
    elif choose == 3:
        pygame.mixer.music.load("Лирика.mp3")
    elif choose == 4:
        pygame.mixer.music.load("Мое сердце.mp3")
    pygame.mixer.music.play()


def fullScreen(image):
    window = Toplevel(root, width=350, height=500)
    BigAccord = Button(window, image=image, command=lambda: window.destroy())
    BigAccord.pack()


root = Tk()
root.geometry("500x550")

pygame.mixer.init()

notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, pady=10)

section = Frame(notebook, width=550, height=500, bg="#f4fef6")
section.grid(row=0, column=0)
notebook.add(section, text='Уроки')

accords = Frame(notebook, width=550, height=500, bg="#f4fef6")
accords.grid(row=0, column=1, pady=10)
notebook.add(accords, text='Аккорды')

answer = IntVar()
answer2 = IntVar()
answer3 = IntVar()
answer4 = IntVar()

isPlaying = True

p1 = PhotoImage(file='first.png').subsample(9, 9)
p2 = PhotoImage(file='second.png').subsample(4, 4)
p3 = PhotoImage(file='third.png').subsample(3, 3)
p4 = PhotoImage(file='fourth.png').subsample(10, 10)

first = Button(section, image=p1, text="Первый урок", bg="#e8f6f4",font=("Times New Roman", 12), height=100, width=250, relief=RIDGE,
               compound=BOTTOM, command=lambda: messagebox.showerror("Покупка", message = "Сначала надо приобрести урок") if freePass["relief"] == RAISED else pressToLess(1))
first.grid(row=0, column=0, padx=20, pady=10)

second = Button(section, image=p2, text="Второй урок", font=("Times New Roman", 12), height=100, width=250,
                relief=RIDGE,
                compound=BOTTOM, command=lambda: messagebox.showerror("Покупка", message = "Сначала надо приобрести урок") if purchaseSecond["relief"] == RAISED else pressToLess(2),
                      bg = '#e8f6f4')
second.grid(row=1, column=0, padx=20, pady=10)

third = Button(section, image=p3, text="Третий урок",bg="#e8f6f4", font=("Times New Roman", 12), height=100, width=250, relief=RIDGE,
               compound=BOTTOM, command=lambda: messagebox.showerror("Покупка", message = "Сначала надо приобрести урок") if purchaseThird["relief"] == RAISED else pressToLess(3))
third.grid(row=2, column=0, padx=20, pady=10)

fourth = Button(section, image=p4, text="Четверый урок",bg="#e8f6f4", font=("Times New Roman", 12), height=100, width=250,
                relief=RIDGE,
                compound=BOTTOM, command=lambda: messagebox.showerror("Покупка", message = "Сначала надо приобрести урок") if purchaseFourth["relief"] == RAISED else pressToLess(4))
fourth.grid(row=3, column=0, padx=20, pady=10)

free = PhotoImage(file="free.png").subsample(20, 20)
purchase = PhotoImage(file="purchase.png").subsample(2,2)

freePass = Button(section, image=free, text="Бесплатно", compound=LEFT, font=("Times New Roman", 12),bg = "#b3d5e9",
                   relief=RAISED, command=lambda: (freePass.config(relief=SUNKEN, state = DISABLED), first.config(bg="#b1e1a2")))
freePass.grid(row=0, column=1)

purchaseSecond = Button(section, image=purchase, text="Купить", compound=LEFT, font=("Times New Roman", 12),bg = "#b3d5e9",
                   width= 130,height=40, relief=RAISED, command=lambda: (purchaseSecond.config(relief=SUNKEN, state = DISABLED), second.config(bg="#b1e1a2")))
purchaseSecond.grid(row=1, column=1)

purchaseThird = Button(section, image=purchase, text="Купить", compound=LEFT, font=("Times New Roman", 12),bg = "#b3d5e9",
                   relief=RAISED,width= 130,height=40, command=lambda: (purchaseThird.config(relief=SUNKEN, state = DISABLED), third.config(bg="#b1e1a2")))
purchaseThird.grid(row=2, column=1)

purchaseFourth = Button(section, image=purchase, text="Купить", compound=LEFT, font=("Times New Roman", 12), bg = "#b3d5e9",
                   relief=RAISED,width= 130,height=40, command=lambda: (purchaseFourth.config(relief=SUNKEN, state = DISABLED), fourth.config(bg="#b1e1a2")))
purchaseFourth.grid(row=3, column=1)

imageBoy = PhotoImage(file='Бой.png').subsample(3, 3)

imageAm = PhotoImage(file='am.png').subsample(16, 16)
imageAmBar = PhotoImage(file='am(баррэ).png').subsample(6, 6)
imageABar = PhotoImage(file='a(баррэ).png').subsample(11, 11)
imageASharp = PhotoImage(file='a#.png').subsample(10, 10)
imageA = PhotoImage(file='a.png').subsample(10, 10)

imageDm = PhotoImage(file='dm.png').subsample(10, 10)
imageD = PhotoImage(file='d.png').subsample(10, 10)
imageDmSharp = PhotoImage(file='dm(баррэ).png').subsample(10, 10)

imageC = PhotoImage(file='c.png').subsample(10, 10)
imageCSharp = PhotoImage(file='c(баррэ).png').subsample(10, 10)

imageG = PhotoImage(file='g.png').subsample(10, 10)
imageGm = PhotoImage(file='gm.png').subsample(10, 10)

iamgeF = PhotoImage(file="f.png").subsample(10, 10)

imageBoy2 = PhotoImage(file='Бой2.png').subsample(3, 3)

imageBoy7 = PhotoImage(file='Бой7.png').subsample(3, 3)

imageEm = PhotoImage(file='em.png').subsample(10, 10)
imageE = PhotoImage(file='e.png').subsample(10, 10)
imageE7 = PhotoImage(file='e7.png').subsample(6, 6)

imageH7 = PhotoImage(file='h7.png').subsample(10, 10)
imageHm = PhotoImage(file='hm.png').subsample(10, 10)

imageTonal = PhotoImage(file='Тоника.png').subsample(2, 2)

imagePerebor = PhotoImage(file='Перебор.png').subsample(3, 3)

imagePlay = PhotoImage(file="play.png").subsample(35, 35)

imageStop = PhotoImage(file="stop.png").subsample(35, 35)

imageRewind = PhotoImage(file="rewind.png").subsample(35, 35)

aAccords = LabelFrame(accords, text="Аккорды А (Ля)", bg="#f4fef6")
aAccords.pack(padx=20, pady=3)

subA = Button(aAccords, image=imageA, command=lambda: fullScreen(imageA), relief=RIDGE)
subA.grid(row=0, column=0)

subAm = Button(aAccords, image=imageAm, command=lambda: fullScreen(imageAm), relief=RIDGE)
subAm.grid(row=0, column=1)

subASharp = Button(aAccords, image=imageASharp, command=lambda: fullScreen(imageASharp), relief=RIDGE)
subASharp.grid(row=0, column=2)

cAccords = LabelFrame(accords, text="Аккорды С (До)", bg="#f4fef6")
cAccords.pack(padx=20, anchor="w", pady=3)

subC = Button(cAccords, image=imageC, command=lambda: fullScreen(imageC), relief=RIDGE)
subC.grid(row=0, column=0)

subCBar = Button(cAccords, image=imageCSharp, command=lambda: fullScreen(imageCSharp), relief=RIDGE)
subCBar.grid(row=0, column=1)

dAccords = LabelFrame(accords, text="Аккорды D (Ре)", bg="#f4fef6")
dAccords.pack(padx=20, pady=3)

subD = Button(dAccords, image=imageD, command=lambda: fullScreen(imageD), relief=RIDGE)
subD.grid(row=0, column=0)

subDm = Button(dAccords, image=imageDm, command=lambda: fullScreen(imageDm), relief=RIDGE)
subDm.grid(row=0, column=1)

subDmSharp = Button(dAccords, image=imageDmSharp, command=lambda: fullScreen(imageDmSharp), relief=RIDGE)
subDmSharp.grid(row=0, column=2)

eAccords = LabelFrame(accords, text="Аккорды E (Ми)", bg="#f4fef6")
eAccords.pack(padx=20, pady=3)

subE = Button(eAccords, image=imageE, command=lambda: fullScreen(imageE), relief=RIDGE)
subE.grid(row=0, column=0)

subEm = Button(eAccords, image=imageEm, command=lambda: fullScreen(imageEm), relief=RIDGE)
subEm.grid(row=0, column=1)

subE7 = Button(eAccords, image=imageE7, command=lambda: fullScreen(imageE7), relief=RIDGE)
subE7.grid(row=0, column=2)

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

　 　 　Am(4)
И две тысячи лет - война,
　　　　C(4) 
Война без особых причин.
　Dm(4)
Война - дело молодых,
G(4)
Лекарство против морщин.
　 　 　Am(4)
Красная, красная кровь –
　　　　C(4)
Через час уже просто земля,
　　　 Dm(4)
Через два на ней цветы и трава,
G(4)
Через три она снова жива
　Dm(4)
И согрета лучами Звезды
　 　 　Am(4)
По имени Солнце...

　 　 　Am(4)
И мы знаем, что так было всегда,
　　　　C(4)
Что судьбою больше любим,
　　　 Dm(4)
Кто живет по законам другим
G(4)
И кому умирать молодым.
　 　 　Am(4) 
Он не помнит слово "да" и слово "нет",
　　　　C(4)
Он не помнит ни чинов, ни имен.
　　　 Dm(4)
И способен дотянуться до звезд,
G(4)
Не считая, что это сон,
　　　 Dm(4)
И упасть, опаленным Звездой
　 　 　Am(4)
По имени Солнце...
""", """Em 　　 С 　G　H7　　　　Em 
Просвистела и упала на столе,
　　　C　 G　　　H7　　　　　Em 
Чуть поела, да скатилась по золе.
　　　　C　 G 　　　　H7　　　　Em
Убитых песен, да - мне нечего терять.
　　　　 C　 G　　　　　H7　　　　Em 
Мир так тесен - дай-ка, брат, тебя обнять.
　С　G　H7　　Em
Оо о-о о-о-о-о о-о

Em 　　 С 　G　H7　　　　Em 
Всюду черти - надави, брат, на педаль.
　　　C　 G　　　H7　　　　　Em 
Час до смерти, да сгоревшего не жаль,
　　　C　 G　　　H7　　　　　Em 
А в чистом поле - ангелочки, васильки.
　　　C　 G　　　H7　　　　　Em 
Мы на воле, и нет ни гари, ни тоски.
　С　G　H7　　Em
Оо о-о о-о-о-о о-о

Em 　　 С 　G　H7　　　　Em 
А на небе встретят Сашка, да Илья, 
　　　C　 G　　　H7　　　　　Em 
Хватит хлеба, да сто грамм - без них нельзя.
　　　C　 G　　　H7　　　　　Em 
Что нам плакать, здесь не срам, чего страдать.
　　　C　 G　　　H7　　　　　Em 
Рай не слякоть, вьюга - наша благодать.
　С　G　H7　　Em
Оо о-о о-о-о-о о-о

Em 　　 С 　G　H7　　　　Em 
Все расскажем про восход и про закат,
　　　C　 G　　　H7　　　　　Em 
Горы сажи, да про горький мармелад,
　　　C　 G　　　H7　　　　　Em 
Что доели, когда закончили войну.
　　　C　 G　　　H7　　　　　Em 
То как сели мы на Родине - в плену.
 　С　G　H7　　Em
Оо о-о о-о-о-о о-о

Em 　　 С 　G　H7　　　　Em 
Просвистела и упала на столе.
　　　C　 G　　　H7　　　　　Em 
Чуть поела, да скатилась по золе.
　　　C　 G　　　H7　　　　　Em 
Убитых песен, да мне нечего терять.
　　　C　 G　　　H7　　　　　Em 
Мир так тесен, дай-ка, брат, тебя обнять.
　С　G　H7　　Em
""", """
1 куплет / играем перебором

　　 Am　　　　　　　　G
Сигаpета мелькает во тьме,
　　　Dm　　　　　　　　　　Am
Ветеp пепел в лицо швыpнyл мне.
　　Am　　　　　　　　 G　　　　　　　　　　Dm　　Am
И обyгленный фильтp на пальцах мне оставил ожо-ог...
　　　　　Am　　　　　　　　G
Скpипнyв сталью, откpылася двеpь. 
　　 Dm　　　　　　Am
Ты идешь, ты моя тепе-е-еpь,
　　　Am　　　　　　　G　　　　　　　Dm　　Am
Я пpиятнyю дpожь ощyщаю с головы до ног...

Припев / Играем боем

　　　　С　　　　　　　 G
Ты со мною забyдь обо всем.
　　 Dm　　　　　　　　　Am
Эта ночь нам покажется сном. 
　　　C　　　　　　　G　　　　　　　Am (2)
Я возьмy тебя и пpижмy как pоднyю дочь!
　　　C　　　　　　 G
Hас окyтает дым сигаpет.
　　　Dm　　　　　　　　　 Am
Ты yйдешь, как настанет pассвет.
　　　C　　　　　　　G　　　　　　　　　　　Am (2)
И следы на постели напомнят пpо счастливyю ночь.

Am         G   
Эротичный лунный свет
      Dm          Am  
Запретит сказать тебе "нет".
    Am           G         Dm        Am   
И опустится плавно на пол все твое белье-о-о-о.
Am           G   
Шум деревьев и ветер ночной
     Dm          Am  
Стон заглушат твой и мой
       Am       G        Dm      Am   
И биение сердца, пылающего адским огнем!

Припев / Играем боем

　　　　С　　　　　　　 G
Ты со мною забyдь обо всем.
　　 Dm　　　　　　　　　Am
Эта ночь нам покажется сном. 
　　　C　　　　　　　G　　　　　　　Am (2)
Я возьмy тебя и пpижмy как pоднyю дочь!
　　　C　　　　　　 G
Hас окyтает дым сигаpет.
　　　Dm　　　　　　　　　 Am
Ты yйдешь, как настанет pассвет.
　　　C　　　　　　　G　　　　　　Am (2)
И следы на постели напомнят пpо счастливyю ночь.

Am         G   
Твои бедра - сиянье луны -
       Dm          Am  
Так прекрасны и мне так нужны.
           Am          G                Dm Am   
Кровь тяжелым напором ударит прямо в сердце мне.
Am                   G   
Груди плавно качнутся в ночи.
       Dm               Am  
Слышишь, как мое сердце стучит.
    Am              G                 Dm Am   
Два пылающих тела сольются в ночной тишине!

Припев / Играем боем
Куплет:

　　　　С　　　　　　　 G
Ты со мною забyдь обо всем.
　　 Dm　　　　　　　　　Am
Эта ночь нам покажется сном. 
　　　C　　　　　　　G　　　　　　　Am (2)
Я возьмy тебя и пpижмy как pоднyю дочь!
　　　C　　　　　　 G
Hас окyтает дым сигаpет.
　　　Dm　　　　　　　　　 Am
Ты yйдешь, как настанет pассвет.
　　　C　　　　　　　G　　　　　　　　　　　Am (2)
И следы на постели напомнят пpо счастливyю ночь.
""", """1 куплет/ играется боем с перебором

　　　　G (2)　　　　　　C　　　G
Мы не знали друг друга до этого лета
　　　　C　　　　 G　　　 D　　　Em
Мы болтались по свету, земле и воде
　　　　G (2)　　　　　　　 C　　　G
И совершенно случайно мы взяли билеты
　　　C　　　 G　　　　　　 D　　　Em
На соседнее кресло на большой высоте

Припев:/ боем 1

　　 G (2)　C　　　G
Мое сердце остановилось,
　　 G (2)　D　　Em
Мое сердце замерло,
　　 G (2)　C　　　G
Мое сердце остановилось,
　　 G (2)　D　　Em
Мое сердце замерло.

　　　　G (2)　　　　　　C　　　G
И ровно тысячу лет мы просыпаемся вместе
　　　　C　　　　 G　　　 D　　　Em
Даже если уснули в разных местах.
　　　　G (2)　　　　　　　 C　　　G
Мы идём ставить кофе под Элвиса Пресли,
　　　C　　　 G　　　　　　 D　　　Em
Кофе сбежал под PropellerHeads, ах!

Припев:/ боем 1

　　 G (2)　C　　　G
Мое сердце остановилось,
　　 G (2)　D　　Em
Мое сердце замерло,
　　 G (2)　C　　　G
Мое сердце остановилось,
　　 G (2)　D　　Em
Мое сердце замерло.

　　　　G (2)　　　　　　C　　　G
И, может быть, ты не стала звездой в Голливуде
　　　　C　　　　 G　　　 D　　　Em
Не выходишь на подиум в нижнем белье
　　　　G (2)　　　　　　　 C　　　G
У тебя не берут автографы люди,
　　　C　　　 G　　　　　　 D　　　Em
И поёшь ты чуть тише, чем Монсерат Кобалье

　　　　G (2)　　　　　　C　　　G
Ну так и я,слава Богу, не Ricky, не Martin,
　　　　C　　　　 G　　　 D　　　Em
Не выдвигался на Оскар, французам не забивал
　　　　G (2)　　　　　　　 C　　　G
Моим именем не назван город на карте,
　　　C　　　 G　　　　　　 D　　　Em
Но задёрнуты шторы и разложен диван

Припев:/ боем 1

　　 G (2)　C　　　G
Мое сердце остановилось,
　　 G (2)　D　　Em
Мое сердце замерло,
　　 G (2)　C　　　G
Мое сердце остановилось,
　　 G (2)　D　　Em
Мое сердце замерло.

Проигрыш: G  C  G  D  Em }x2

     G (2)                C             G
Я наяву вижу то, что многим даже не снилось,
     C            G        D               Em
Не являлось под кайфом, не стучалось в стекло.
          G (2)           C             G
Мое сердце остановилось, отдышалось немного                   
Куплет:
C   G  D  Em
И снова пошло.

Припев:/ боем 1

　　 G (2)　C　　　G
Мое сердце остановилось,
　　 G (2)　D　　Em
Мое сердце замерло,
　　 G (2)　C　　　G
Мое сердце остановилось,
　　 G (2)　D　　Em
Мое сердце замерло."""]

root.mainloop()
