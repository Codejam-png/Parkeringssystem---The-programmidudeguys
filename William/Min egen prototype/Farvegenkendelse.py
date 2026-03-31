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
    conn = sqlite3.connect("Stefan/ParkeringsDatabase.db")
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

with open("William/Min egen prototype/PladsNRpixelsDict.json", "r") as f:
    PladsNrpixelsDict = json.load(f)
with open("William/Min egen prototype/AsfaltOmrådepixelsDict.json", "r") as g:
    KontrolPladsDict = json.load(g)

Facitliste = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,1]
with Image.open("William/ParkeringspladsOriginal.jpg") as billede:
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

def PladsBestemmelse(PrecisionFactor,ErrorMargin,Pladsfarve,billede):
    AgendaList = []
    
    for PladsID in PladsNrpixelsDict:
        ErrorCount = 0
        PixelCount = 0
        for PixelPlacering in PladsNrpixelsDict[PladsID]:
            r, g, b = billede.getpixel((PixelPlacering))
            
            for Kontrol in Pladsfarve:
                rScore = abs(r-Kontrol[0]) #Fjerner division da reletiv afvigelse er HELT forkert, da der regnes i absolut værdi
                gScore = abs(g-Kontrol[1])
                bScore = abs(b-Kontrol[2])
                FinalScore = rScore+gScore+bScore

                if (FinalScore <= PrecisionFactor):
                    ErrorCount -= 1
                    break
            ErrorCount +=  1
            PixelCount +=  1
        Agenda = 1 if (ErrorCount/PixelCount <= ErrorMargin) else 0
        AgendaList.append(Agenda)
        
        #Change_db(i,Agenda) Det kommer på i den endelige version, men nu skal der optimeres, så det gør bare programmet langsommere
    return AgendaList
AgendaList = PladsBestemmelse(0.04,146,Pladsfarve,billede)
Score = 0
Total = 0
for x in (AgendaList):
    if AgendaList[Total] == Facitliste[Total]:
        Score +=1
    Total +=1
print(f"{Score} ud af {Total}")
    


   

