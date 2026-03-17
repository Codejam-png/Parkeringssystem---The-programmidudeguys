import socket
import sqlite3


#DETTE ER SERVEREREN

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8080))
s.listen(5)

def get_db_connection():
    conn = sqlite3.connect("ParkeringsDatabase.db")
    conn.row_factory = sqlite3.Row
    return conn

def send_notification(message, client_socket):    
     client_socket.send(bytes(message, "utf-8"))

def bedstePladsOgBesked(brugerpreference, conn):    

    if brugerpreference == "None":
        if conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'almindelig' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone() != None: #Henter data fra databasen og ser om der findes noget på den prefererede plads som sql-sætningen definerer. Hvis der gør det så fortsæt, hvis ikke så sig "ingen plads" (i return sætningen)
            plads = conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'almindelig' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone()[0]
            message = f"Du har ikke indtastet en preference, du faar derfor givet den tilgaengelige almindelige plads der er taettest paa skolens indgang:{plads}"
            return message
        elif conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'almindelig' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone() == None:
            message = "Der er desvaerre ingen ledige pladser af nogen type."
            return message

    #almindelig
    if brugerpreference == "Almindelig":
        if conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'almindelig' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone() != None: #Henter data fra databasen og ser om der findes noget på den prefererede plads som sql-sætningen definerer. Hvis der gør det så fortsæt, hvis ikke så sig "ingen plads" (i return sætningen)
            plads = conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'almindelig' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone()[0]
            message = f"Der er en ledig plads paa {plads}"
            return message
        elif conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'almindelig' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone() == None:
            message = "Der er desvaerre ingen ledige pladser af nogen type."
            return message

    #elbil
    elif brugerpreference == "Elbil":
        if conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'elbil' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone() != None:
            plads = conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'elbil' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone()[0] #Vi henter dataen ud fra select sætningen. Grunden til [0] er for at vi kun vælger "sqlite3.Row object"(tror vi) og dataen vises korrekt, syntaksen er fundet her: https://stackoverflow.com/questions/76354183/database-returns-sqlite3-row-object-at-0x0000019494a725f0-instead-of-data
            
            message = f"Der er en ledig elbilplads paa {plads}"
            return message
        
        if conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'elbil' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone() == None: #Henter data fra databasen og ser om der findes noget på den prefererede plads som sql-sætningen definerer. Hvis der ikke gør det (==None) så søger den istedet i almindelig og giver den tilgængelige almindelige plads
            plads = conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'almindelig' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone()[0]
            message = f"Der er desværre ingen ledige elbilpladser pt. Den bedste alternative plads er {plads}"
            return message
        elif conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'almindelig' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone() == None:
            message = "Der er desvaerre ingen ledige pladser af nogen type."
            return message
    #handicap
    elif brugerpreference == "Handicap":
        if conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'handicap' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone() != None: #Henter data fra databasen og tjekker om der findes noget på den prefererede plads som sql-sætningen definerer. Hvis der gør det så fortsæt, hvis ikke så gå ned i elif som søger almindelige.
            plads = conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'handicap' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone()[0] #Vi henter dataen ud fra select sætningen. Grunden til [0] er for at vi kun vælger "sqlite3.Row object"(tror vi) og dataen vises korrekt, syntaksen er fundet her: https://stackoverflow.com/questions/76354183/database-returns-sqlite3-row-object-at-0x0000019494a725f0-instead-of-data
            message = f"Der er en ledig handicapplads paa {plads}"
            return message
        
        elif conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'handicap' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone() == None: #Henter data fra databasen og ser om der findes noget på den prefererede plads som sql-sætningen definerer. Hvis der ikke gør det (==None) så søger den istedet i almindelig og giver den tilgængelige almindelige plads
            plads = conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'almindelig' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone()[0]
            message = f"Der er desvaerre ingen ledige handicappladser pt. Den bedste alternative plads er {plads}"
            return message
        elif conn.execute("SELECT BLokationKode FROM ParkeringsBås WHERE Type = 'almindelig' AND Ledig = 1 ORDER BY AfstandFI LIMIT 1;").fetchone() == None:
            message = "Der er desvaerre ingen ledige pladser af nogen type."
            return message
    


# programmet skal afvente input fra brugeren på internettet
def main():
    while True:
        client_socket, addr = s.accept()
        print(f"Forbundet til {addr}")
        conn = get_db_connection()
        brugerpreference = client_socket.recv(1024).decode("utf-8")
        print(f"Brugerpræference: {brugerpreference}")
        message = bedstePladsOgBesked(brugerpreference,conn)
        send_notification(message, client_socket)
        print(f"Sendt besked til {addr}: {message}")
        conn.close()
        client_socket.close()
        print(f"Afsluttet forbindelse til {addr}")
if __name__ == "__main__": 
    main()        
            