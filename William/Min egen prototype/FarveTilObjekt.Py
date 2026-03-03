from statistics import mean #Giver en nemmere måde at regne gennemsnittet af lister på.
from PIL import Image

A1Objekt = []
A2Objekt = []
A3Objekt = []
A4Objekt = []
A5Objekt = []

A1 = [0,255,204]
A2 = [0,0,0]
A3 = [255,0,0]
A4 = [0,255,0]
A5 = [0,0,255]
A6 = [255,255,0]
AvereagevalueDict = {
    mean(A1) : "A1",
    mean(A2) : "A2",
    mean(A3) : "A3",
    mean(A4) : "A4",
    mean(A5) : "A5",
    mean(A6) : "A6",
}
ObjektFarveDict = {
    "A1" : A1,
    "A2" : A2,
    "A3" : A3,
    "A4" : A4,
    "A5" : A5,
    
}
ObjektDict = {
    "A1" : A1Objekt,
    "A2" : A2Objekt,


}


with Image.open("William/Min egen prototype/ImageForRoconizion.png") as billede:
    billede = billede.convert("RGB")
    bredde, højde = billede.size
    PixelListe = []
    for y in range(højde):
        for x in range(bredde):
            r, g, b = billede.getpixel((x, y))
            Avereagevalue = (r+g+b)/3
            
            if (AvereagevalueDict(Avereagevalue)):
                ObjektID = AvereagevalueDict(Avereagevalue)
                rObjekt,gObjekt,bObjekt = ObjektFarveDict(ObjektID)[0,1,2]
                if (rObjekt == r and gObjekt == g and bObjekt == b):
                    ObjektDict[ObjektID].append((x,y))

            


                    



