
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.


image = Image.open("lab.jpg") #Открываем изображение.
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования.
width = image.size[0] #Определяем ширину.
height = image.size[1] #Определяем высоту.
pix = image.load() #Выгружаем значения пикселей.
k =1
st = 120

for i in range(st,height-210):

    for j in range(st,width):
        if k % 2 ==0:
            if (i - st) % 64 == 0 or i == st:
                pix[j,i]=(255,0,0)
                k+=1
        else:
            if (i - st) % 22 == 0 or i == st:
                pix[j,i]=(255,0,0)
                k+=1
        if (j - st) % 64 == 0 or j == st:

            pix[j,i]=(255,0,0)
image.show()