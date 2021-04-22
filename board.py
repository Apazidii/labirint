from graphics import *

boardfile = "board.txt"






def NewBoard(boardfile):
    print("Введите ширину доски: ")
    W = int(input())
    H = int(input())
    filew = open(boardfile,"w")




    filew.close()











#функция на вход получает путь к файлу с доской
#На выход выдает двухмерный массив с доской
# 0 - пусто
# 1 - стена
# 2 - путь
# 3 - старт
# 4 - финиш
def GetBoard(boardfile):
    filer = open(boardfile,"r")
    a = (filer.read().split("\n"))
    k = int(a[1])

    a = a[2:]
    for i in range(0,k ):
        a[i] = list(map(int,a[i]))
    filer.close()
    return a

#функция на вход получает путь к файлу с доской
#На выход выдает массив с двумя числами - шириной и высотой доски
def GetBoardSize(boardfile):
    filer = open(boardfile,"r")
    a = (filer.read().split("\n"))
    a = a[:2]
    a = list(map(int,a))
    filer.close()
    return a


#   Функция закрашивает клетку на доске соответствующим цветом
#   Функция получает на вход:
#   координата X (int)
#   координата Y (int)
#   цвет клетки (string)
#   окно для графики (win)
#   На выход ничего не возвращает
def PaintCell(x, y, color, win):
    obj = Rectangle(Point(50 + x * 25, 50 + y * 25), Point(50 + x * 25 + 25, 50 + y * 25 + 25))
    obj.setFill(color)

    obj.draw(win)


#Функция перерисовыет на доске все клетки согласно базе
# на вход получает путь до файла с базой, массив с доской и саму доску
# Использует метод PaintCell
# на выход ничего не возвращает
def RePaintCells(boardfile,boardarr,win):
    sizes = GetBoardSize(boardfile)
    W = sizes[0]
    H = sizes[1]

    for i in range(0, H):
        for j in range(0, W):
            k = boardarr[i][j]
            if k == 0:
                PaintCell(j, i, "White", win)
            elif k == 1:
                PaintCell(j, i, "grey", win)
            elif k == 2:
                PaintCell(j, i, "yellow", win)
            elif k == 3:
                PaintCell(j, i, "Red", win)
            elif k == 4:
                PaintCell(j, i, "lime", win)

#   Функция сделана по аналогу с PaintCell
#   Используется в функции ReNumberCell
#   Вместо color тут запрашивается число d (int)
def NumberCell(x, y, d, win):
    text = Text(Point(50+(25/2)+25*x,50+(25/2)+25*y),d)
    text.setTextColor('black')
    text.setSize(10)
    text.draw(win)

#   функция сделанна по аналогу RePrintCell, но должна писать число d прямо внутри клеток
#   И нужна для помощи написания алгоритма
#   В релизной версии удалить или не вызывать
def ReNumberCells(boardfile,boarD,win):
    sizes = GetBoardSize(boardfile)
    W = sizes[0]
    H = sizes[1]

    for i in range(0, H):
        for j in range(0, W):
            n = boarD[i][j][1]
            NumberCell(j,i,n,win)



#Функция на вход получает массив доски
#Функция создает и отображает доску в окне для графики
#на выход возвращает объект с окном
def ShowBoard(boardarr,boardfile):
    sizes = GetBoardSize(boardfile)
    W = sizes[0]
    H = sizes[1]

    win = GraphWin("Окно для графики", ((W*25)+100), ((H*25)+100))



    for i in range(0,H+1):
        obj = Line(Point(50,50+(i*25)),Point((W*25)+100-50,50+(25*i)))
        obj.draw(win)

    for i in range(0,W+1):
        obj = Line(Point((50+(i*25)),50),Point((50+(25*i)),(H*25)+100-50))
        obj.draw(win)



    return win





