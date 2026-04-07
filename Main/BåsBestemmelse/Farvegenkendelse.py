from statistics import mean #Giver en nemmere måde at regne gennemsnittet af lister på.
from PIL import Image
from flask import json
import random
import sqlite3
class Object:
    def __init__(self,R,G,B):
        self.colorR = R
        self.colorG = G
        self.colorB = B
def get_db_connection():
    conn = sqlite3.connect("ParkeringsDatabase.db")
    conn.row_factory = sqlite3.Row
    return conn

def Change_db(i,Agenda):
    conn= get_db_connection()
    conn.execute(
        f"""
        UPDATE ParkeringsBås
        SET Ledig = '{Agenda}'
        WHERE BLokationKode = '{i}'
        """
    )
    conn.commit() 
    conn.close()

with open("Main/BåsBestemmelse/PladsNRpixelsDict.json", "r") as f:
    PladsNrpixelsDict = json.load(f)
with open("Main/BåsBestemmelse/AsfaltOmrådepixelsDict.json", "r") as g:
    KontrolPladsDict = json.load(g)

Facitliste = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1]
with Image.open("Main/ParkeringspladsOriginal.jpg") as billede:
        billede = billede.convert("RGB")  # Sikrer at vi arbejder i RGB
        
        Pladsfarve = []
        for kontrolplads in KontrolPladsDict:
            PladsPixels = KontrolPladsDict[kontrolplads]
            for Pixel in PladsPixels:
                r, g, b = billede.getpixel((Pixel))

                PixelListeKontrolr = []
                PixelListeKontrolg = []
                PixelListeKontrolb = []
                PixelListeKontrolr.append(r)
                PixelListeKontrolg.append(g)
                PixelListeKontrolb.append(b)
            PixelListeKontrol = [mean(PixelListeKontrolr), mean(PixelListeKontrolg), mean(PixelListeKontrolb)]
            Pladsfarve.append(PixelListeKontrol)

def PladsBestemmelse(PrecisionFactor,GrænseProcent,Pladsfarve,billede):
    AgendaList = []
    
    for PladsID in PladsNrpixelsDict:
        FyldtPixel = 0
        PixelCount = 0
        for PixelPlacering in PladsNrpixelsDict[PladsID]:
            r, g, b = billede.getpixel((PixelPlacering))
            
            for Kontrol in Pladsfarve:
                rDiff = abs(r-Kontrol[0]) #Fjerner division da reletiv afvigelse er HELT forkert, da der regnes i absolut værdi
                gDiff = abs(g-Kontrol[1])
                bDiff = abs(b-Kontrol[2])
                SamletDiff = rDiff+gDiff+bDiff
                
                if (SamletDiff <= PrecisionFactor):
                    FyldtPixel -= 1
                    break
            FyldtPixel +=  1
            PixelCount +=  1
        Agenda = 1 if (FyldtPixel/PixelCount <= GrænseProcent) else 0
        AgendaList.append(Agenda)
        
        Change_db(PladsID,Agenda) #Det kommer på i den endelige version, men nu skal der optimeres, så det gør bare programmet langsommere
    return AgendaList
AgendaList = PladsBestemmelse(146,0.04,Pladsfarve,billede)
Score = 0
Total = 0
FejlListe = []
ForkertTom = 0
ForkertFyldt = 0
for x in (AgendaList):
    if AgendaList[Total] == Facitliste[Total]:
        Score +=1
    else:
        FejlListe.append(Total)
        if AgendaList[Total] < Facitliste[Total]:
            ForkertFyldt += 1
        else:
            ForkertTom += 1
    Total +=1
#print(f"{Score} ud af {Total}, Liste: {AgendaList} FejlListe: {FejlListe} Forkert Fyldt: {ForkertFyldt} Forkert Tom: {ForkertTom}")
print("Slut")


   

