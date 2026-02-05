import socket
import sqlite3

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8080))
s.listen(5)

def get_db_connection():
    conn = sqlite3.connect("Stefan/database.db")
    conn.row_factory = sqlite3.Row
    return conn

def send_notification(message, client_socket):    
     client_socket.send(bytes(message, "utf-8"))

def bestePladsOgBesked(brugerpreference, conn):
    if brugerpreference == "elbil":
        plads = conn.execute("SELECT * FROM parkerings_system WHERE plads_type = 'elbil' AND status = 'ledig' ORDER BY id LIMIT 1;").fetchone()["plads_code"]
        if plads != None:
            message = "Der er en ledig elbil plads på " + plads
            return message
        plads = conn.execute("SELECT * FROM parkerings_system WHERE plads_type = 'almindelig' AND status = 'ledig' ORDER BY id LIMIT 1;").fetchone()["plads_code"]
        if plads != None:
            message = "Der er ingen ledige elbil pladser pt. Den bedste alternative plads er " + plads
            return message
        return "Der er desværre igen ledige pladser."
    
    elif brugerpreference == "handicap":
        plads = conn.execute("SELECT * FROM parkerings_system WHERE plads_type = 'handicap' AND status = 'ledig' ORDER BY id LIMIT 1;").fetchone()["plads_code"]
        if plads != None:
            message = "Der er en ledig handicap plads på " + plads
            return message
        plads = conn.execute("SELECT * FROM parkerings_system WHERE plads_type = 'almindelig' AND status = 'ledig' ORDER BY id LIMIT 1;").fetchone()["plads_code"]
        if plads != None:
            message = "Der er ingen ledige handicap pladser pt. Den bedste alternative plads er " + plads
            return message
        return "Der er desværre igen ledige pladser."
    
    else:
        plads = conn.execute("SELECT * FROM parkerings_system WHERE plads_type = 'almindelig' AND status = 'ledig' ORDER BY id LIMIT 1;").fetchone()["plads_code"]
        if plads != None:
            message = "Der er en ledig plads på " + plads
            return message
        return "Der er desværre ingen ledige pladser."



# programmet skal afvente input fra brugeren på internettet
def main():
    while True:
        client_socket, addr = s.accept()
        print(f"Forbundet til {addr}")
        conn = get_db_connection()
        brugerpreference = client_socket.recv(1024).decode("utf-8")
        print(f"Brugerpræference: {brugerpreference}")
        message = bestePladsOgBesked(brugerpreference,conn)
        send_notification(message, client_socket)
        print(f"Sendt besked til {addr}: {message}")
        conn.close()
        client_socket.close()
        print(f"Afsluttet forbindelse til {addr}")
   
if __name__ == "__main__": 
    main()        
            