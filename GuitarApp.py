from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
import random



def pressToLess(number):
    if number == 1:
        lesson = Toplevel(root, width=500, height=550, bg = "lavender")

        name = Label(lesson, text="Урок 1: 'Звезда по имени солнце'", font=("Times new roman", 16, "italic"), bg = "lavender")
        name.pack(side=TOP)


        complete = Checkbutton(lesson, text="Урок выполнен", justify=RIGHT, fg= f"{'red' if answer.get() == 0 else 'green'}",
                               variable=answer, offvalue=0, onvalue=1, command= lambda: complete.config(fg = f"{'red' if answer.get() == 0 else 'green'}"), bg = "lavender",activebackground="lavender")

        complete.pack(side=TOP)

        canvasForAccords = Canvas(lesson, height=200, width=500, bg = "lavender")
        canvasForAccords.pack()

        canvasForAccords.create_image(70, 50, image=imageBoy)
        canvasForAccords.create_image(220, 50, image=imageAm)
        canvasForAccords.create_image(360, 50, image=imageC)
        canvasForAccords.create_image(70, 140, image=imageDm)
        canvasForAccords.create_image(225, 140, image=imageG)

        generalname = Label(lesson, text="Текст песни: ", font=("Times new roman", 16, "bold"), bg = "lavender")
        generalname.pack(side=TOP)

        e = Text(lesson, width=50, height=20, bg = "lavender")
        e.insert(1.0, songsData[0])
        e.pack(side=LEFT)
        e.config(state=DISABLED)

        scroll = Scrollbar(lesson, command=e.yview)
        scroll.pack(side=RIGHT, fill=Y)

        e.config(yscrollcommand=scroll.set)

    if number == 2:
        lesson = Toplevel(root, width=500, height=550, bg = "lavender")

        name = Label(lesson, text="Урок 2: 'Просвистела'", font=("Times new roman", 16, "italic"), bg = "lavender")
        name.pack(side=TOP)


        complete = Checkbutton(lesson, text="Урок выполнен", justify=RIGHT, fg= f"{'red' if answer2.get() == 0 else 'green'}",
                               variable=answer2, offvalue=0, onvalue=1, command= lambda: complete.config(fg = f"{'red' if answer2.get() == 0 else 'green'}"), bg = "lavender",activebackground="lavender")
        complete.pack(side=TOP)

        canvasForAccords = Canvas(lesson, height=200, width=500, bg = "lavender")
        canvasForAccords.pack()

        canvasForAccords.create_image(70, 50, image=imageBoy2)
        canvasForAccords.create_image(220, 50, image=imageEm)
        canvasForAccords.create_image(360, 50, image=imageC)
        canvasForAccords.create_image(70, 140, image=imageG)
        canvasForAccords.create_image(225, 140, image=imageH7)


        generalname = Label(lesson, text="Текст песни: ", font=("Times new roman", 16, "bold"), bg = "lavender")
        generalname.pack(side=TOP)

        e = Text(lesson, width=50, height=20, bg = "lavender")
        e.insert(1.0, songsData[1])
        e.pack(side=LEFT)
        e.config(state=DISABLED)

        scroll = Scrollbar(lesson, command=e.yview)
        scroll.pack(side=RIGHT, fill=Y)

        e.config(yscrollcommand=scroll.set)
    if number == 3:
        lesson = Toplevel(root, width=500, height=550, bg = "lavender")

        name = Label(lesson, text="Урок 3: 'Лирика'", font=("Times new roman", 16, "italic"), bg = "lavender")
        name.pack(side=TOP)


        complete = Checkbutton(lesson, text="Урок выполнен", justify=RIGHT, fg= f"{'red' if answer3.get() == 0 else 'green'}",
                               variable=answer3, offvalue=0, onvalue=1, command= lambda: complete.config(fg = f"{'red' if answer3.get() == 0 else 'green'}"), bg = "lavender",activebackground="lavender")
        complete.pack(side=TOP)

        canvasForAccords = Canvas(lesson, height=200, width=500, bg = "lavender")
        canvasForAccords.pack()

        canvasForAccords.create_image(70, 50, image=imageBoy7)
        canvasForAccords.create_image(225, 50, image=imageAm)
        canvasForAccords.create_image(390, 100, image=imageTonal)
        canvasForAccords.create_image(70, 140, image=imageG)
        canvasForAccords.create_image(225, 140, image=imageDm)


        generalname = Label(lesson, text="Текст песни: ", font=("Times new roman", 16, "bold"), bg = "lavender")
        generalname.pack(side=TOP)

        e = Text(lesson, width=50, height=20, bg = "lavender")
        e.insert(1.0, songsData[2])
        e.pack(side=LEFT)
        e.config(state=DISABLED)

        scroll = Scrollbar(lesson, command=e.yview)
        scroll.pack(side=RIGHT, fill=Y)

        e.config(yscrollcommand=scroll.set)
    if number == 4:
        lesson = Toplevel(root, width=500, height=550, bg = "lavender")

        name = Label(lesson, text="Урок 4: 'Мое сердце'", font=("Times new roman", 16, "italic"), bg = "lavender")
        name.pack(side=TOP)


        complete = Checkbutton(lesson, text="Урок выполнен", justify=RIGHT, fg= f"{'red' if answer4.get() == 0 else 'green'}",
                               variable=answer4, offvalue=0, onvalue=1, command= lambda: complete.config(fg = f"{'red' if answer4.get() == 0 else 'green'}"), bg = "lavender",activebackground="lavender")
        complete.pack(side=TOP)

        canvasForAccords = Canvas(lesson, height=200, width=500, bg = "lavender")
        canvasForAccords.pack()

        canvasForAccords.create_image(70, 50, image=imageBoy)
        canvasForAccords.create_image(225, 53, image=imageG)
        canvasForAccords.create_image(390, 100, image=imagePerebor)
        canvasForAccords.create_image(70, 140, image=imageG)
        canvasForAccords.create_image(220, 145, image=imageEm)


        generalname = Label(lesson, text="Текст песни: ", font=("Times new roman", 16, "bold"), bg = "lavender")
        generalname.pack(side=TOP)

        e = Text(lesson, width=50, height=20, bg = "lavender")
        e.insert(1.0, songsData[3])
        e.pack(side=LEFT)
        e.config(state=DISABLED)

        scroll = Scrollbar(lesson, command=e.yview)
        scroll.pack(side=RIGHT, fill=Y)

        e.config(yscrollcommand=scroll.set)


root = Tk()
root.geometry("350x550")

notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, pady=10)

section = Frame(notebook, width=350, height=500)
section.grid(row=0, column=0)
notebook.add(section, text='Уроки')

accords = Frame(notebook, width=350, height=500)
accords.grid(row=0, column=1, pady=10)
notebook.add(accords, text='Аккорды')

answer = IntVar()
answer2 = IntVar()
answer3 = IntVar()
answer4 = IntVar()

p1 = PhotoImage(file='first.png').subsample(9, 9)

first = Button(section, image=p1, text="Первый урок", font=("Times New Roman", 12), height=100, width=250,
               compound=BOTTOM, command=lambda: pressToLess(1))
first.pack(side=TOP, pady=10)

p2 = PhotoImage(file='second.png').subsample(4, 4)

second = Button(section, image=p2, text="Второй урок", font=("Times New Roman", 12), height=100, width=250,
                compound=BOTTOM, command=lambda: pressToLess(2))
second.pack(side=TOP, pady=10)

p3 = PhotoImage(file='third.png').subsample(3, 3)

third = Button(section, image=p3, text="Третий урок", font=("Times New Roman", 12), height=100, width=250,
               compound=BOTTOM, command=lambda: pressToLess(3))
third.pack(side=TOP, pady=10)

p4 = PhotoImage(file='fourth.png').subsample(10, 10)

fourth = Button(section, image=p4, text="Четверый урок", font=("Times New Roman", 12), height=100, width=250,
                compound=BOTTOM, command=lambda: pressToLess(4))
fourth.pack(side=TOP, pady=10)

imageBoy = PhotoImage(file='Бой.png').subsample(3, 3)

imageAm = PhotoImage(file='am.png').subsample(16, 16)

imageDm = PhotoImage(file='dm.png').subsample(10, 10)

imageC = PhotoImage(file='c.png').subsample(11, 11)

imageG = PhotoImage(file='g.png').subsample(10, 10)

imageBoy2 = PhotoImage(file='Бой2.png').subsample(3, 3)

imageBoy7 = PhotoImage(file='Бой7.png').subsample(3, 3)

imageEm = PhotoImage(file='em.png').subsample(11, 11)

imageH7 = PhotoImage(file='h7.png').subsample(10, 10)

imageTonal = PhotoImage(file='Тоника.png').subsample(2, 2)

imagePerebor = PhotoImage(file='Перебор.png').subsample(3, 3)

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
""","""Em 　　 С 　G　H7　　　　Em 
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
""","""
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
""","""1 куплет/ играется боем с перебором

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
