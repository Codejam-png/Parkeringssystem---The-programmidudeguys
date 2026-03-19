from statistics import mean #Giver en nemmere måde at regne gennemsnittet af lister på.
from PIL import Image
from flask import json
import pygame, sys
import random
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

with open("William/Min egen prototype/AsfaltOmrådepixelsDict.json", "r") as g:
    KontrolPladsDict = json.load(g)
ObjectList = []
ObjectFarveListe = []

PixelListeKontrolr = []
PixelListeKontrolg = []
PixelListeKontrolb = []
Pladsfarve = []
PrecisionFactor = 0.15
ErrorMargin = 0.2
ScoreList = []


    


with Image.open("William/ParkeringspladsOriginal.jpg") as billede:
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
        for h in Plads:
            r, g, b = billede.getpixel((h))

            PixelListeKontrolr.append(r)
            PixelListeKontrolg.append(g)
            PixelListeKontrolb.append(b)
        PixelListeKontrol = [mean(PixelListeKontrolr), mean(PixelListeKontrolg), mean(PixelListeKontrolb)]
        Pladsfarve.append(PixelListeKontrol)
        

    for i in PladsNrpixelsDict:
        for x in PladsNrpixelsDict[i]:
            r, g, b = billede.getpixel((x))
            ErrorCount = 0
            PixelCount = 0
            for Kontrol in Pladsfarve:
                rScore = abs((r-Kontrol[0])/Kontrol[0])
                gScore = abs((g-Kontrol[1])/Kontrol[1])
                bScore = abs((b-Kontrol[2])/Kontrol[2])
                FinalScore = (rScore+gScore+bScore)/3
                if (FinalScore <= PrecisionFactor):
                     ErrorCount = ErrorCount - 1
                     break
            ErrorCount +=  1
            PixelCount +=  1
        Agenda = (ErrorCount/PixelCount <= ErrorMargin) 
        Change_db(i,Agenda)

