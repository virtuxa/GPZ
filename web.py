from flask import Flask, render_template, request

import app as MainApp
from app import *

app = Flask(__name__)
global numRound
numRound = 6 # Кол-во знаков после запятой в координатах

@app.route("/")
def index():
    return render_template("yaMap.html")

@app.route('/getCoords', methods=['GET', 'POST'])
def getCoords():
    global coordStart
    global coordEnd

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        coords = request.get_json()  # Получаем JSON
        if MainApp.flag == 0:
            coordStart = coords['coords']
            coordStart = str(round(coordStart[0],numRound))+"  "+str(round(coordStart[1],numRound))
            MainApp.flag = 1
        elif MainApp.flag == 1:
            coordEnd = coords['coords']
            coordEnd = str(round(coordEnd[0],numRound))+"  "+str(round(coordEnd[1],numRound))
            MainApp.flag = 2

        return 'OK', 200

if __name__ == '__main__':
    app.run()