import socket
import flask

#DETTE ER KLIENTEN

## to run in cmd write: py client.py

# når klientens gps kommer tæt på parkeringspladsen skal den connecte til serveren
#https://www.youtube.com/watch?v=ZVfeIWk6974&t=578s

#klienten connecter til serveren, sender preference og modtager den bedste plads.

app = flask.Flask(__name__)


@app.route('/', methods=['POST','GET'])
def askforlocation():
    global pladspreference
    pladspreference = str(flask.request.form.get('pladspref'))
    return flask.render_template('askforlocation.html', pladsprefHTML = pladspreference)


@app.route('/locationdata', methods=['POST'])
def locationdata():
    #pladspreference = flask.request.form['pladspreference']
    latitude = flask.request.form.get('latitude')
    longitude = flask.request.form.get('longitude')
    print(f"location er latitude: {latitude} og longitude: {longitude}")
    if vedParkeringPladsen(latitude, longitude):
        message = connect_and_receive()
        return flask.render_template('notification.html', message=message)
    else:
        return flask.render_template('askforlocation.html', LOCmessage = "Du er udenfor rækkevidde")


def vedParkeringPladsen(latitude, longitude):#sammenlign latitude og longitude med parkeringspladsens koordinater
    if float(latitude) <= 56.148 and float(latitude) >= 56.145 and float(longitude) >= 8.990488 and float(longitude) <= 8.996228: #er kommet hertil
        return True
    else:
        return True

def connect_and_receive():
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 8080))
    global pladspreference #referer til den preference som er sat i app route /.
    s.send(bytes(pladspreference, "utf-8"))
    full_msg = ''
    while True:
        msg = s.recv(8)
        if not msg:
            break
        full_msg += msg.decode("utf-8")
    print(full_msg)
    s.close()
    return full_msg

app.run(debug=True)
