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
Screenx = 6000
Screeny = 1260
ScreenSize = Screenx*Screeny
ObjectLengthX = 10
ObjectLengthY = 10
ObjectSize = ObjectLengthX*ObjectLengthY
ObjectYpos = 0
ObjectXpos = 0
ObjectMax = 200
ControlPointx = 1500
ControlPointy = 100
ControlPointWidthx = 10
ControlPointWidthy = 10
ControlPointSize = ControlPointWidthx*ControlPointWidthy
ScoreList = []
PixelListeWPlacement = []

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
#pygame.image.save(Window, "William/Min egen prototype/ImageForRoconizion.png")
with Image.open("ImageForRoconizion.png") as billede:
    billede = billede.convert("RGB")  # Sikrer at vi arbejder i RGB
    bredde, højde = billede.size       # Gemmer bredde og højde i pixels (size er en attribut)

    PixelListe = []  # Tom liste til de nye pixels
    for y in range(højde):
        for x in range(bredde):
            r, g, b = billede.getpixel((x, y))
            PixelFarve = [r,g,b]
            PixelListe.append(PixelFarve)
            PixelListeWPlacement.append({"Farve":PixelFarve, "Placering":(x,y)}) #Denne sætning tilføjer pixlens farveværdi og dens placering til "PixelListeWPlacement"
    
    
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
        FinalScoreRGBValue = (str(r) + ", " + str(g) + ", " + str(b))
        FinalScorePixel = PixelListeWPlacement[1] #henter pixlen fra PixelListeWPlacement. Lige nu kan jeg ikke iterere på den da i er et objekt i en liste og ikke en iterator. Så snart jeg kan iterere burde det fungere
        FinalScorePixelPlacement = FinalScorePixel[2] # henter placeringen fra pixlen DET ER I BEGGE DISSE DER HAR MED PIXELPLACEMENT AT GØRE AT FEJLEN LIGGER
        if (FinalScore != 0.000):
            if(FinalScore <=0.5):
                ScoreList.append(str(FinalScore) + "; " + str(FinalScoreRGBValue) + "; " + str(FinalScorePixelPlacement)) #lige nu fungerer dette halvt. Det ser rigtigt ud, men for at kunne bruge det skal "ScoreList" laves til en liste af dictionaries. "str(FinalScore) + "; " + str(FinalScoreRGBValue) + "; " + str(FinalScorePixelPlacement)" skal altså derfor laves til et dict. Når dict logikken er sat op burde hver finalScore have både en farve og en placering koblet på sig som så derefter kan "tegnes" på skærmen

            
        Index=Index+1
    print(ScoreList)
    print(rControl,gControl,bControl)

    pygame.draw.rect(Window, (rControl, bControl, gControl), [ControlPointx,ControlPointy,ControlPointWidthx,ControlPointWidthy],int(ControlPointWidthy/2))
    pygame.display.update()

'''
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

Denne logik kan bruges på finalscores oprindelige værdier for at se hvilken farve vores gennemsnit er.

Kan man lave en visuel repræsentation af hele 6000*1260 griddet af pixels men hvor det kun er de områder med en værdi på 0,5 eller derunder i finalscore der vises med farve og alt andet er hvidt? 
Denne visuelle repræsentation kan bruges til fintuning af vores finalscore tolerance og den kan bruges til at kortlægge hvorhenne på skærmen de frie pladser ligger henne, altså deres x*y værdier som kan kædes sammen med en båsplads i virkeligheden.

Mangler: måde at henvise tilbage til den oprindelige pixel der har den viste finalscore.
'''



Window = pygame.display.set_mode((Screenx, Screeny))
Window.fill((255, 255, 255))
pygame.display.update()
'''
for i in pixelList: #her er pixelList en liste over ALLE pixels på hele billedet
    
    Når der er en pixel der har en finalscore værdi lavere end eller lig 0,5 skal den pixel sættes til farven som har givet den denne finalscore værdi
    Vi ender med den del af billedet hvor finalscore passer bedst. Altså kan det vi får bruges til at fintune finalscore. Det der ligger bag er det vi skal bruge til at vide hvor båsen er (altså x*y)

''' 



        




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
