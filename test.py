
from graphics import *

win = GraphWin("Окно для графики", 1010,1110)
image = "map2.png"
myImage = Image(Point(1010/2-4,1110/2-4),image)
myImage.draw(win)
c = Rectangle(Point(209,109),Point(297,893))
#c = Rectangle(Point(4,4),Point(297,893))
c.setFill("Green")

c.draw(win)

win.getMouse()
win.close()