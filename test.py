from PIL import Image, ImageDraw #Подключим необходимые библиотеки.

#from graphics import *

w = 101 * 5
h = 111 * 5


image = Image.open("map.png") #Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.

filew = open("board.txt","w")
filew.write(str(width)+"\n")
filew.write(str(height)+"\n")

for i in range(0, height-1):
    for j in range(0, width-1):
       # print(pix[i,j])

        if pix[j,i]==(255,255,255,255):
            celcol = 0
        elif pix[j,i]==(0,0,0,255):
            celcol = 1
        elif pix[j,i]==(0,255,0,255):
            celcol = 3
        elif pix[j,i]==(0,0,255,255):
            celcol = 4
        else:
            celcol = 1


        filew.write(str(celcol))
    filew.write('\n')



'''

win = GraphWin("Окно для графики", w,h)
image = "map.png"
myImage = Image(Point(w/2,h/2),image)
myImage.draw(win)
c = Rectangle(Point(105,55),Point(150,450))
#c = Rectangle(Point(4,4),Point(297,893))
c.setFill("Green")

c.draw(win)

win.getMouse()
win.close()
'''