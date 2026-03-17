from statistics import mean #Giver en nemmere måde at regne gennemsnittet af lister på.
from PIL import Image
from flask import json
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

ControlPointx = 150
ControlPointy = 150
ControlPointWidthx = 300
ControlPointWidthy = 300
ControlPointSize = ControlPointWidthx*ControlPointWidthy
PrecisionFactor = 0.15
ScoreList = []

PladsFarver = json.load(open("William/Min egen prototype/PladsFarver.json", "r")) # Læser json filen med farverne for hver plads ind i et dictionary



with Image.open("William/Min egen prototype/ParkeringspladsOriginal.JPG") as billede:
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
    


        





pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
