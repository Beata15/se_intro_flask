from flask import Flask
app = Flask(__name__)

moje_imie = 'Beata'

@app.route('/')
def hello_world():
    return 'Hello, World ' + moje_imie + ' !'

@app.route('/kto')
def kto():
    return moje_imie


@app.route('/wiadomosc')
def wiadomosc():
    return 'Hello, World!'

@app.route('/miasto')
def miasto():
    return 'Wroclaw'
