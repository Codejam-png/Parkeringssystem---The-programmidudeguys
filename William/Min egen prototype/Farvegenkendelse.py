from statistics import mean #Giver en nemmere måde at regne gennemsnittet af lister på.
from PIL import Image
from flask import json
import pygame, sys
import random
from pygame.locals import *
import sqlite3
class Object:
    def __init__(self,R,G,B):
        self.colorR = R
        self.colorG = G
        self.colorB = B
def get_db_connection():
    conn = sqlite3.connect("Stefan/ParkeringsDatabase.db")
    conn.row_factory = sqlite3.Row
    return conn

def Change_db(i,Agenda):
    conn= get_db_connection()
    conn.execute(
        f"""
        UPDATE ParkeringsDatabase
        SET Ledig = {Agenda}
        WHERE {PladsNrpixelsDict[i]}
        """
    )
    conn.commit() 
    conn.close()
with open("William/Min egen prototype/PladsNRpixelsDict.json", "r") as f:
    PladsNrpixelsDict = json.load(f)

with open("William/FalskFilPlacering >:( ", "r") as g:
    KontrolPladsDict = json.load(f)
ObjectList = []
ObjectFarveListe = []

PixelListeKontrol = []
Pladsfarve = []
PrecisionFactor = 0.15
ScoreList = []


    


with Image.open("William/Min egen prototype/ParkeringspladsOriginal.JPG") as billede:
    billede = billede.convert("RGB")  # Sikrer at vi arbejder i RGB
    bredde, højde = billede.size       # Gemmer bredde og højde i pixels (size er en attribut)
    PixelListe = []  # Tom liste til de nye pixels 
    for y in range(højde):
        for x in range(bredde):
            r, g, b = billede.getpixel((x, y))
            PixelFarve = [r,g,b]
            PixelListe.append(PixelFarve)
    
    for i in KontrolPladsDict:
        Plads = KontrolPladsDict[i]
        for x in Plads:
            billede.getpixel
            r, g, b = billede.getpixel((x, y))
            PixelFarveKontrol = [r,g,b]
            PixelListeKontrol.append(PixelFarve)
        Pladsfarve.append(PixelListeKontrol)

    ObjectPosY = 0
    for i in PladsNrpixelsDict:
        for x in PladsNrpixelsDict[i]:
            pass
        if(4 == 4):
            Agenda = 1
        else:
            Agenda = 0
        Change_db(i,Agenda)



        
    


        





pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
