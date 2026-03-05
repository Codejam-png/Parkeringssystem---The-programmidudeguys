import sqlite3

båsliste = [

    {"AfstandFI": 34.7, "BLokationKode": "A1", "Ledig": 1, "Type": "handicap"},
    {"AfstandFI": 128.4, "BLokationKode": "A2", "Ledig": 0, "Type": "handicap"},
    {"AfstandFI": 276.9, "BLokationKode": "A3", "Ledig": 1, "Type": "handicap"},
    {"AfstandFI": 412.3, "BLokationKode": "A4", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 59.8, "BLokationKode": "A5", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 487.6, "BLokationKode": "A6", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 93.5, "BLokationKode": "A7", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 301.2, "BLokationKode": "A8", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 215.7, "BLokationKode": "A9", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 378.4, "BLokationKode": "A10", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 142.6, "BLokationKode": "A11", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 498.1, "BLokationKode": "A12", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 67.3, "BLokationKode": "A13", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 254.8, "BLokationKode": "A14", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 19.5, "BLokationKode": "A15", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 333.9, "BLokationKode": "A16", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 451.7, "BLokationKode": "A17", "Ledig": 1, "Type": "almindelig"},

    {"AfstandFI": 82.4, "BLokationKode": "B1", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 167.9, "BLokationKode": "B2", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 289.6, "BLokationKode": "B3", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 354.1, "BLokationKode": "B4", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 44.2, "BLokationKode": "B5", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 472.5, "BLokationKode": "B6", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 199.3, "BLokationKode": "B7", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 310.8, "BLokationKode": "B8", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 123.7, "BLokationKode": "B9", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 265.4, "BLokationKode": "B10", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 390.2, "BLokationKode": "B11", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 58.6, "BLokationKode": "B12", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 441.9, "BLokationKode": "B13", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 218.5, "BLokationKode": "B14", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 347.6, "BLokationKode": "B15", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 76.3, "BLokationKode": "B16", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 498.7, "BLokationKode": "B17", "Ledig": 0, "Type": "almindelig"},

    {"AfstandFI": 135.8, "BLokationKode": "C1", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 268.4, "BLokationKode": "C2", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 92.7, "BLokationKode": "C3", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 412.6, "BLokationKode": "C4", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 38.9, "BLokationKode": "C5", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 489.4, "BLokationKode": "C6", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 177.5, "BLokationKode": "C7", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 356.2, "BLokationKode": "C8", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 209.8, "BLokationKode": "C9", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 74.6, "BLokationKode": "C10", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 300.3, "BLokationKode": "C11", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 450.5, "BLokationKode": "C12", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 119.4, "BLokationKode": "C13", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 247.1, "BLokationKode": "C14", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 16.8, "BLokationKode": "C15", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 388.9, "BLokationKode": "C16", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 421.3, "BLokationKode": "C17", "Ledig": 1, "Type": "almindelig"},

    {"AfstandFI": 55.6, "BLokationKode": "D1", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 180.2, "BLokationKode": "D2", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 295.7, "BLokationKode": "D3", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 401.8, "BLokationKode": "D4", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 63.9, "BLokationKode": "D5", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 472.1, "BLokationKode": "D6", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 222.4, "BLokationKode": "D7", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 349.5, "BLokationKode": "D8", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 108.3, "BLokationKode": "D9", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 267.6, "BLokationKode": "D10", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 390.4, "BLokationKode": "D11", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 145.9, "BLokationKode": "D12", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 498.9, "BLokationKode": "D13", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 87.1, "BLokationKode": "D14", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 312.5, "BLokationKode": "D15", "Ledig": 0, "Type": "almindelig"},
    {"AfstandFI": 44.8, "BLokationKode": "D16", "Ledig": 1, "Type": "almindelig"},
    {"AfstandFI": 433.2, "BLokationKode": "D17", "Ledig": 0, "Type": "almindelig"}
]


def get_db_connection():
    conn = sqlite3.connect("ParkeringsDatabase.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn= get_db_connection()
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS "ParkeringsBås" (
        "BLokationKode" TEXT NOT NULL UNIQUE,
        "AfstandFI" REAL NOT NULL,
        "Ledig" INTEGER NOT NULL,
        "Type" TEXT NOT NULL,
        PRIMARY KEY("BLokationKode")
        );
        '''
    )
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS "ParkeringsPlads"(
        "PLokation" BLOB NOT NULL UNIQUE,
        "Ejer" TEXT NOT NULL,
        PRIMARY KEY("PLokation")
        );
        '''
    )
    conn.execute(
        '''
        INSERT INTO "ParkeringsPlads" (PLokation,Ejer)
        VALUES ("Lillelundvej 21 Herning","Herningsholm Erhvervsskole og Gymnasier");
        '''
        )
    
    conn.commit()
    if conn.execute("SELECT COUNT(*) FROM ParkeringsBås").fetchall()[0][0] == 0:
        for bås in båsliste:
            conn.execute(
                f'''
                INSERT INTO "ParkeringsBås" (BLokationKode, AfstandFI, Ledig, Type) 
                VAlUES ("{bås['BLokationKode']}",{bås['AfstandFI']},{bås['Ledig']},"{bås['Type']}");
                '''
            )
            conn.commit() 

    conn.close()
init_db()
