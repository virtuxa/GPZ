from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("yaMap.html")

@app.route('/getCoords', methods=['GET', 'POST'])
def getCoords():
    global coord
    # POST request
    if request.method == 'POST':
        print('Incoming..')
        coords = request.get_json()  # parse as JSON
        coord = coords['coords']
        coord = str(round(coord[0],4))+"  "+str(round(coord[1],4))
        return 'OK', 200

if __name__ == '__main__':
    app.run()