from multiprocessing import Pool
from PIL import Image
import Farvegenkendelse
import time

# Global variables for workers
image_path = "William/ParkeringspladsOriginal.jpg"
billede = None  # will be set in initializer
Pladsfarve = Farvegenkendelse.Pladsfarve
FacitListe = Farvegenkendelse.Facitliste
func = Farvegenkendelse.PladsBestemmelse

# Initializer for each worker
def initialiserArbejder():
    global billede
    with Image.open(image_path) as img: #Hver Worker har nu billedet gemt, og "global billede" vil overskride "billede" i funktionen.
        billede = img.convert("RGB")

# Worker function
def Funktionen(parametre):
    global billede
    PrecisionFactor, ErrorMargin = parametre
    ErrorMargin /= 100
    
    
    AgendaList = func(PrecisionFactor, ErrorMargin, Pladsfarve, billede)
    points=0
    for g in range(len(AgendaList)):
        if FacitListe[g] == AgendaList[g]:
            points +=1
    return (PrecisionFactor, ErrorMargin, points)

if __name__ == "__main__":
    PrecisionsVærdiListe = range(0, 255*3+1, 5)
    ErrorVærdiListe = range(0, 100, 1)
    Parametre = []
    for værdiP in PrecisionsVærdiListe:
        for værdiE in ErrorVærdiListe:
            kombinationsTuple = (værdiP,værdiE)
            Parametre.append(kombinationsTuple)

    startTime = time.time()
    with Pool(initializer=initialiserArbejder) as pool: #Antal arbejdere = antal kerner
        Resultater = pool.map(Funktionen, Parametre)
    PointListe = 0
    HøjestePoint = 0
    BedsteResultat = ()
    for res in Resultater:
        Point = res[2]
        if Point > HøjestePoint:
            HøjestePoint = Point
            BedsteResultat = res 
    TidBrugt = time.time() - startTime
    print(f"Den bedste ErrorMargin: {BedsteResultat[1]} \n Den bedste PrecisionFactor: {BedsteResultat[2]} \n Det tog i alt {TidBrugt}")

