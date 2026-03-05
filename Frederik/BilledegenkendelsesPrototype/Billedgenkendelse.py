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
ObjectLengthx = 60
ObjectLengthy = 60
ObjectAmountX = Screenx/ObjectLengthx
ObjectAmountY = Screeny/ObjectLengthy
ObjectSize = ObjectLengthy*ObjectLengthx
ObjectYpos = 0
ObjectXpos = 0
ControlPointx = 1500
ControlPointy = 100
ControlPointWidthx = 300
ControlPointWidthy = 300
ControlPointSize = ControlPointWidthx*ControlPointWidthy
PrecisionFactor = 1
ScoreList = []
NumberToLetter ={
    "0" : "A", "1" : "B", "2" : "C", "3" : "D", "4" : "E", "5" : "F", "6" : "G", "7" : "H", "8" : "I", "9" :"J"
}


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
    
    Ypos = (x*ObjectLengthx >= Screenx*(Ypos+ObjectLengthy)/ObjectLengthy and ObjectLengthy) + Ypos
    Xpos = x*ObjectLengthx - Screenx*Ypos/ObjectLengthy
    pygame.draw.rect(Window, (ob.colorR,ob.colorG,ob.colorB), [Xpos, Ypos, ObjectLengthx, ObjectLengthy], ObjectLengthx*2)
    x=x+1
pygame.draw.rect(Window, (random.randrange(255), random.randrange(255), random.randrange(255)), [ControlPointx,ControlPointy,ControlPointWidthx,ControlPointWidthy],int(ControlPointWidthy/2))



pygame.display.update()
#pygame.image.save(Window, "ImageForRoconizion.png")
with Image.open("ImageForRoconizion.png") as billede:
    billede = billede.convert("RGB")  # Sikrer at vi arbejder i RGB
    bredde, højde = billede.size       # Gemmer bredde og højde i pixels (size er en attribut)
    rControl,gControl,bControl = billede.getpixel((ControlPointx,ControlPointy))
    PixelListe = []  # Tom liste til de nye pixels
    for y in range(højde):
        for x in range(bredde):
            r, g, b = billede.getpixel((x, y))
            PixelFarve = [r,g,b]
            PixelListe.append(PixelFarve)
    
    ObjectPosY = 0
    for u in range(int(ScreenSize/ObjectSize)):
        ObjectPixels = []
        for z in range(ObjectSize):
            LengthCapX = ObjectLengthx + u*ObjectLengthx
            ObjectYpos = (z >= LengthCapX*(ObjectYpos+1)) + ObjectYpos   
            ObjectXpos = z - LengthCapX*ObjectYpos
            NumberInList = (ObjectXpos + ObjectYpos*Screenx)
            ObjectPixels.append(PixelListe[NumberInList])

        
        RListe = []
        GListe = []
        BListe = []
        FarveGennemsnit = []
        ErrorCount = 0
        for i in range(ObjectSize):
            RPixel = ObjectPixels[i][0]
            GPixel = ObjectPixels[i][1]
            BPixel = ObjectPixels[i][2]
            RListe.append(RPixel)
            ErrorCount = ((RPixel-rControl)/rControl > 0.50 and 1 ) + ErrorCount
            GListe.append(GPixel)
            ErrorCount = ((GPixel-gControl)/gControl > 0.50 and 1 ) + ErrorCount
            BListe.append(BPixel)
            ErrorCount = ((BPixel-bControl)/bControl > 0.50 and 1 ) + ErrorCount
        if (ErrorCount <= ObjectSize*PrecisionFactor):
            FarveGennemsnit.append(mean(RListe))
            FarveGennemsnit.append(mean(GListe))
            FarveGennemsnit.append(mean(BListe))
            ObjectPosY = (u >= ObjectAmountX*(ObjectPosY+1) and 1)+ObjectPosY
            NumberInRow = int(u-ObjectAmountX*(ObjectPosY+1))
            if (ObjectPosY < 10):
                Row = NumberToLetter[f"{ObjectPosY}"] #Mangler Dict til at få det til bogstav
            else:
                Row = "¤"   
            StringNumber = f"{Row}{NumberInRow}"
            FarveGennemsnit.append(StringNumber)
            ObjectFarveListe.append(FarveGennemsnit)
        
    Index = 0
    for i in ObjectFarveListe:
        r = i[0]
        g = i[1]
        b = i[2]
        rScore = abs((r-rControl)/rControl)
        gScore = abs((g-gControl)/gControl)
        bScore = abs((b-bControl)/bControl)
        FinalScore = (rScore+gScore+bScore)/3
        if (FinalScore != 0.000 and FinalScore < PrecisionFactor*2):
            
            ScoreList.append(i[3])
            Index=Index+1
    
    ScoreList.sort()  
    print(ScoreList)
    print(Index)
    #hvis der ikke kommer mange objekter, eller slet ingen som havner på ScoreList, så fygt ej. Det er precisionFactor-variablen der afgør hvor stor precisionen skal være. Der skal være få resultater her, da farverne af kasserne er tilfældige

'''
    for i in ScoreList:  
    
        
        ob = i

        Ypos = (x*1 >= Screenx*(Ypos+1)/1 and 1) + Ypos
        Xpos = x*1 - Screenx*Ypos/1
        pygame.draw.rect(Window, (ObjectFarveListe[x][0],ObjectFarveListe[x][1],ObjectFarveListe[x][2]), [x, x, 1, 1], 1)#Formålet er at vi genskaber billedet med de værdier vi har fra scorelist, altså farve og placering. Den skal laves til dict før fungerer
        x=x+1 # vores iterator
'''



        





pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
