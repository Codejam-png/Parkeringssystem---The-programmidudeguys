import socket
import sqlite3

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8080))
s.listen(5)

def get_db_connection():
    conn = sqlite3.connect("parkerings_system.db")
    conn.row_factory = sqlite3.Row
    return conn

def send_notification(message, client_socket):    
     client_socket.send(bytes(message, "utf-8"))

def bestePladsOgBesked(brugerpreference, conn):
    if brugerpreference == "elbil":
        plads = conn.execute(
            "SELECT * FROM parkerings_system WHERE plads_type = 'elbil' AND status = 'ledig' ORDER BY id LIMIT 1;"
        )
        if plads.fetchone() != None:
            message = "Der er en ledig elbil plads på " + str( plads.fetchone()["plads_code"])
            return message
        plads = conn.execute(
                "SELECT * FROM parkerings_system WHERE plads_type = 'almindelig' AND status = 'ledig' ORDER BY id LIMIT 1;"
            )
        if plads.fetchone() != None:
            message = "Der er ingen ledige elbil pladser pt. Den bedste alternative plads er " + plads.fetchone()["plads_code"]
            return message
        return "Der er desværre igen ledige pladser."
    
    elif brugerpreference == "handicap":
        plads = conn.execute(
            "SELECT * FROM parkerings_system WHERE plads_type = 'handicap' AND status = 'ledig' ORDER BY id LIMIT 1;"
        )
        if plads.fetchone() != None:
            message = "Der er en ledig handicap plads på " + plads.fetchone()["plads_code"]
            return message
        plads = conn.execute(
                "SELECT * FROM parkerings_system WHERE plads_type = 'almindelig' AND status = 'ledig' ORDER BY id LIMIT 1;"
            )
        if plads.fetchone() != None:
            message = "Der er ingen ledige handicap pladser pt. Den bedste alternative plads er " + plads.fetchone()["plads_code"]
            return message
        return "Der er desværre igen ledige pladser."
    
    else:
        plads = conn.execute(
            "SELECT * FROM parkerings_system WHERE plads_type = 'almindelig' AND status = 'ledig' ORDER BY id LIMIT 1;"
        )
        if plads.fetchone() != None:
            message = "Der er en ledig plads på " + plads.fetchone()["plads_code"]
            return message
        return "Der er desværre ingen ledige pladser."

def init_db():
    conn= get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS parkerings_system (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        plads_code TEXT NOT NULL,
        status TEXT NOT NULL,
        plads_type TEXT NOT NULL
        );
        """
    )
    conn.commit()
    if conn.execute("SELECT COUNT(*) FROM parkerings_system").fetchall()[0][0] == 0:
        for i in range(1,8):
            conn.execute(
                """
                INSERT INTO parkerings_system (plads_code, status, plads_type)
                VALUES
                ('A"""+str(i)+"""', 'ledig', 'almindelig'),
                ('B"""+str(i)+"""', 'ledig', 'handicap'),
                ('C"""+str(i)+"""', 'ledig', 'elbil');
                """
            )
            conn.commit() 
    conn.close()

# programmet skal afvente input fra brugeren på internettet
def main():
    while True:
        client_socket, addr = s.accept()
        print(f"Forbundet til {addr}")
        conn = get_db_connection()
        brugerpreference = client_socket.recv(1024).decode("utf-8")
        message = bestePladsOgBesked(brugerpreference,conn)
        send_notification(message, client_socket)
        conn.close()
        client_socket.close()
   
if __name__ == "__main__": 
    init_db()
    main()        
            