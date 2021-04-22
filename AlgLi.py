from board import *




boardfile = "board.txt"
boardarr = GetBoard(boardfile)
win = ShowBoard(boardarr,boardfile)
RePaintCells(boardfile,boardarr,win)

boardD = []
sizes = GetBoardSize(boardfile)
W = sizes[0]
H = sizes[1]

for i in range(0,H):
    temp = []
    for j in range(0,W):
        temp.append([False,0])
    boardD.append(temp)


finish = []
start = []

for i in range(0,H):
    for j in range(0,W):
        k = boardarr[i][j]
        if k == 0:
            boardD[i][j][1] = W*H
        elif k == 1:
            boardD[i][j][0] = True
            boardD[i][j][1] = "W"
        elif k == 2:
            boardD[i][j][1] = W*H
        elif k == 3:
            start.append(i)
            start.append(j)
            boardD[i][j][0]=True
            boardD[i][j][1] = 0
        elif k == 4:
            finish.append(i)
            finish.append(j)
            boardD[i][j][1] = 100







nowTips = [start]
nextTips = []
pp = 0
while (boardD[finish[0]][finish[1]][0] == False) and (len(nowTips) !=0):

    for i in range(0,len(nowTips)):
        nowStep = nowTips[i]
        if (nowStep[0] != 0):
            if boardD[nowStep[0] - 1][ nowStep[1]][0] == False:
                if  (boardD[nowStep[0] - 1][ nowStep[1]][1] > boardD[nowStep[0]][nowStep[1]][1]+1):
                    boardD[nowStep[0] - 1][ nowStep[1]][1] = boardD[nowStep[0]][nowStep[1]][1]+1
                    boardD[nowStep[0] - 1][ nowStep[1]][0] = True
                    nextTips.append([nowStep[0] - 1,nowStep[1]])

        if (nowStep[0] != H - 1):
            if boardD[nowStep[0] + 1][nowStep[1]][0] == False:
                if  (boardD[nowStep[0] + 1][ nowStep[1]][1] > boardD[nowStep[0]][nowStep[1]][1]+1):
                    boardD[nowStep[0] + 1][ nowStep[1]][1] = boardD[nowStep[0]][nowStep[1]][1]+1
                    boardD[nowStep[0] + 1][ nowStep[1]][0] = True
                    nextTips.append([nowStep[0] + 1, nowStep[1]])


        if (nowStep[1] != 0):
            if boardD[nowStep[0]][nowStep[1]-1][0] == False:
                if  (boardD[nowStep[0]][ nowStep[1] - 1][1] > boardD[nowStep[0]][nowStep[1]][1]+1):
                    boardD[nowStep[0]][ nowStep[1] - 1][1] = boardD[nowStep[0]][nowStep[1]][1]+1
                    boardD[nowStep[0]][ nowStep[1] - 1][0] = True
                    nextTips.append([nowStep[0], nowStep[1]-1])

        if (nowStep[1] != W - 1):
            if boardD[nowStep[0] ][nowStep[1]+1][0] == False:
                if  (boardD[nowStep[0]][ nowStep[1] + 1][1] > boardD[nowStep[0]][nowStep[1]][1]+1):
                    boardD[nowStep[0]][ nowStep[1] + 1][1] = boardD[nowStep[0]][nowStep[1]][1]+1
                    boardD[nowStep[0]][ nowStep[1] + 1][0] = True
                    nextTips.append([nowStep[0], nowStep[1]+1])


    nowTips = nextTips.copy()
    nextTips.clear()



nStp = boardD[finish[0]][finish[1]][1]
nowStep = finish.copy()
for i in range(0,nStp-1):


    if (nowStep[0] != 0):
        if boardD[nowStep[0] - 1][nowStep[1]][1] != "W":
            if (boardD[nowStep[0] - 1][nowStep[1]][1] == boardD[nowStep[0]][nowStep[1]][1] - 1):
                nowStep = [nowStep[0] - 1,nowStep[1]].copy()
                boardarr[nowStep[0] ][nowStep[1]]=2
                continue

    if (nowStep[0] != H - 1):
        if boardD[nowStep[0] + 1][nowStep[1]][1] != "W":
            if (boardD[nowStep[0] + 1][nowStep[1]][1] == boardD[nowStep[0]][nowStep[1]][1] -1):
                nowStep = [nowStep[0] + 1, nowStep[1]].copy()
                boardarr[nowStep[0] ][nowStep[1]] = 2
                continue

    if (nowStep[1] != 0):
        if boardD[nowStep[0]][nowStep[1] - 1][1] != "W":
            if (boardD[nowStep[0]][nowStep[1] - 1][1] == boardD[nowStep[0]][nowStep[1]][1] - 1):
                nowStep = [nowStep[0],nowStep[1] - 1].copy()
                boardarr[nowStep[0] ][nowStep[1] ] = 2
                continue

    if (nowStep[1] != W - 1):
        if boardD[nowStep[0]][nowStep[1] + 1][0] != "W":
            if (boardD[nowStep[0]][nowStep[1] + 1][1] == boardD[nowStep[0]][nowStep[1]][1] - 1):
                nowStep = [nowStep[0],nowStep[1] + 1].copy()
                boardarr[nowStep[0] ][nowStep[1] ] = 2
                continue




RePaintCells(boardfile,boardarr,win)
ReNumberCells(boardfile,boardD,win)

win.getMouse()
win.close()

