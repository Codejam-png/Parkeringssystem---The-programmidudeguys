from statistics import mean #Giver en nemmere måde at regne gennemsnittet af lister på.
from PIL import Image

A1Objekt = []
A2Objekt = []
A3Objekt = []
A4Objekt = []
A5Objekt = []
A6Objekt = []
count = 0
A1 = (0,0,0)
A2 = (1,0,0)
A3 = (2,0,0)
A4 = (3,0,0)
A5 = (4,0,0)
A6 = (255,255,0)    
Color = {
    A1 : "A1",
    A2 : "A2",
    A3 : "A3",
    A4 : "A4",
    A5 : "A5",
    A6 : "A6",
}
ObjektDict = {
    "A1" : A1Objekt,
    "A2" : A2Objekt,
    "A3" : A3Objekt,
    "A4" : A4Objekt,
    "A5" : A5Objekt,
    "A6" : A6Objekt,
}


with Image.open("William/Farlig parkeringspladsbillede.png") as billede:
    billede = billede.convert("RGB")
    bredde, højde = billede.size
    for y in range(højde):
        for x in range(bredde):
            Farve = billede.getpixel((x, y))
            if (Farve in Color):
                ObjektDict[Color[Farve]].append((x,y))
                count = count + 1
    print(len((A1Objekt)))
    print(len((A2Objekt)))
    print(len((A3Objekt)))
    print(len((A4Objekt)))