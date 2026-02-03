from statistics import mean #Giver en nemmere måde at regne gennemsnittet af lister på.
from PIL import Image
import pygame, sys
import random
from pygame.locals import *


class Object:
    def __init__(self,R,G,B):
        self.colorR = R
        self.colorG = G
        self.colorB = B

ObjectList = []
ObjectFarveListe = []
Screenx = 600
Screeny = 600
ScreenSize = Screenx*Screeny
ObjectLengthX = 10
ObjectLengthY = 10
ObjectSize = ObjectLengthX*ObjectLengthY
ObjectYpos = 0
ObjectXpos = 0
ObjectMax = 200
ControlPointx = 150
ControlPointy = 150
ControlPointWidthx = 300
ControlPointWidthy = 300
ControlPointSize = ControlPointWidthx*ControlPointWidthy
ScoreList = []
for i in range(int(ScreenSize/ObjectSize)): 
    object = Object(random.randrange(255),random.randrange(255),random.randrange(255))
    ObjectList.append(object) 
print("Færdig")
pygame.init()


Window = pygame.display.set_mode((Screenx, Screeny))
Window.fill((255, 255, 255))
x=0
Ypos = 0
Xpos = 0
for i in ObjectList:  
    
    ob = i
    
    Ypos = (x*10 >= Screenx*(Ypos+10)/10 and 10) + Ypos
    Xpos = x*10 - Screenx*Ypos/10
    pygame.draw.rect(Window, (ob.colorR,ob.colorG,ob.colorB), [Xpos, Ypos, 10, 10], 5)
    x=x+1
pygame.draw.rect(Window, (random.randrange(255), random.randrange(255), random.randrange(255)), [ControlPointx,ControlPointy,ControlPointWidthx,ControlPointWidthy],int(ControlPointWidthy/2))



pygame.display.update()
pygame.image.save(Window, "William/Min egen prototype/ImageForRoconizion.png")
with Image.open("William/Min egen prototype/ImageForRoconizion.png") as billede:
    billede = billede.convert("RGB")  # Sikrer at vi arbejder i RGB
    bredde, højde = billede.size       # Gemmer bredde og højde i pixels (size er en attribut)

    PixelListe = []  # Tom liste til de nye pixels
    for y in range(højde):
        for x in range(bredde):
            r, g, b = billede.getpixel((x, y))
            PixelFarve = [r,g,b]
            PixelListe.append(PixelFarve)
    
    
    for u in range(int(ScreenSize/ObjectSize)):
        ObjectPixels = []
        for z in range(ObjectSize):
            LengthCapX = ObjectLengthX + u*ObjectLengthX
            ObjectYpos = (z >= LengthCapX*(ObjectYpos+1)) + ObjectYpos   
            ObjectXpos = z - LengthCapX*ObjectYpos
            NumberInList = (ObjectXpos + ObjectYpos*Screenx)
            ObjectPixels.append(PixelListe[NumberInList])

        
        RListe = []
        GListe = []
        BListe = []
        FarveGennemsnit = []
        for i in range(ObjectSize):
            RListe.append(ObjectPixels[i][0])
            GListe.append(ObjectPixels[i][1])
            BListe.append(ObjectPixels[i][2])
        FarveGennemsnit.append(mean(RListe))
        FarveGennemsnit.append(mean(GListe))
        FarveGennemsnit.append(mean(BListe))
        ObjectFarveListe.append(FarveGennemsnit)
        rControl,gControl,bControl = billede.getpixel((ControlPointx,ControlPointy))
    Index = 0
    for i in ObjectFarveListe:
        r = i[0]
        g = i[1]
        b = i[2]
        rScore = abs((r-rControl)/rControl)
        gScore = abs((g-gControl)/gControl)
        bScore = abs((b-bControl)/bControl)
        FinalScore = (rScore+gScore+bScore)/3
        if (FinalScore != 0.000):
            ScoreList.append(FinalScore)
        Index=Index+1
    print(ScoreList)
    



        





pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
