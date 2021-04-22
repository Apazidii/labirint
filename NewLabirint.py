from graphics import *
from board import *

def NewBoard(boardfile):
    print("Введите ширину доски: ",end="")
    W = int(input())
    print("Введите высоту доски: ",end='')
    H = int(input())
    filew = open(boardfile,"w")
    filew.write(str(W)+'\n')
    filew.write(str(H)+'\n')
    boardarr = []

    for i in range(0,H):
        temp = []
        for i in range(0,W):
            temp.append(0)
        boardarr.append(temp)


    win = GraphWin("Окно для графики", ((W*25)+100), ((H*25)+100))
    for i in range(0,H+1):
        obj = Line(Point(50,50+(i*25)),Point((W*25)+100-50,50+(25*i)))
        obj.draw(win)

    for i in range(0,W+1):
        obj = Line(Point((50+(i*25)),50),Point((50+(25*i)),(H*25)+100-50))
        obj.draw(win)

    def b1(event):
        x =event.x
        y =event.y
        if x< 50 and y<50:
            win.close()
        if (x>=50) and (x<=50+W*25) and (y>=50)and(y<=50+H*25):
            x = x-50
            y = y-50
            x = x//25
            y = y//25
            if boardarr[y][x]<=3:
                boardarr[y][x]+=1
            else: boardarr[y][x]=0

            if boardarr[y][x]==2:
                boardarr[y][x]=3
            k = boardarr[y][x]

            if k == 0:
                PaintCell(x, y, "White", win)
            elif k == 1:
                PaintCell(x, y, "grey", win)
            elif k == 2:
                PaintCell(x, y, "Yellow", win)
            elif k == 3:
                PaintCell(x, y, "Red", win)
            elif k == 4:
                PaintCell(x, y, "lime", win)


    def b3(event):
        for i in range(0,H):
            for j in range(0,W):
                filew.write(str(boardarr[i][j]))
            filew.write('\n')
        win.close()
    win.bind('<Button-1>', b1)
    win.bind('<Button-3>', b3)





    win.getMouse()
    win.close()
    filew.close()





NewBoard('board.txt')
print(123213)