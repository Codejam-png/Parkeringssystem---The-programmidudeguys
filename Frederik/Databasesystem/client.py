import socket
import flask

#DETTE ER KLIENTEN

## to run in cmd write: py client.py

# når klientens gps kommer tæt på parkeringspladsen skal den connecte til serveren
#https://www.youtube.com/watch?v=ZVfeIWk6974&t=578s


#klienten connecter til serveren, sender preference og modtager den bedste plads.
app = flask.Flask(__name__)

@app.route('/')
def askforlocation():
    return flask.render_template('askforlocation.html')

@app.route('/locationdata',methods=['POST'])
def locationdata():
    #pladspreference = flask.request.form['pladspreference']
    latitude = flask.request.form['latitude']
    longitude = flask.request.form['longitude']
    print(f"location er latitude: {latitude} og longitude: {longitude}")
    if vedParkeringPladsen(latitude, longitude):
        message =connect_and_receive()
        return flask.render_template('notification.html', message=message)
    else:
        return flask.render_template('askforlocation.html')

def vedParkeringPladsen(latitude, longitude):
    return True #sammenlign latitude og longitude med parkeringspladsens koordinater

def connect_and_receive():
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 8080))
    pladspreference = "elbil"
    s.send(bytes(pladspreference, "utf-8"))
    full_msg = ''
    while True:
        msg = s.recv(8)
        if not msg:
            break
        full_msg += msg.decode("utf-8")
    print(full_msg)
    return full_msg
    s.close()

app.run(debug=True)
