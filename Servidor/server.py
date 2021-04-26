from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Games list
games = []

# Get Games


@app.route("/getGames", methods=['GET'])
def getGames():
    global games
    return jsonify(games)

# Load from 24 to 24 Games


@app.route("/loadGames", methods=['POST'])
def loadGames():
    global games
    if request.method == 'POST':
        games.extend(request.json['array'])
        print("SERVER>Quantity of games: " + str(len(games)))
        return jsonify({"status": "ok"})

# Insert 1 Game


@app.route("/insertGame", methods=['POST'])
def insertGames():
    global games
    if request.method == 'POST':
        games.append(request.json)
        return jsonify({"status": "ok"})

# Delete all games


@app.route("/deleteAllGames", methods=['GET'])
def deleteAllGames():
    global games
    if request.method == 'GET':
        games = []
        print("SERVER>Quantity of games: " + str(len(games)))
        return jsonify({"status": "ok"})

# Update Amazon Game


@app.route("/updateAmazonGame", methods=['PUT'])
def updateAmazonGame(name, newItem):
    global games
    for game in games:
        if game['name'] == name:
            game['price'] = newItem.price
            game['store'] = 'Amazon'
            return jsonify(games)

# Update Time Game


@app.route("/updateTimeGame", methods=['PUT'])
def updateTimeGame(name, time):
    global games
    for game in games:
        if game['name'] == name:
            game['time'] = time
            return jsonify(games)

# Update MetaData Game


@app.route("/updateMetaDataGame", methods=['PUT'])
def updateMetaDataGame(name, meta):
    global games
    for game in games:
        if game['name'] == request.json['name']:
            game['meta'] = request.json['meta']
            return jsonify(games)


if __name__ == "__main__":
    # 'ipv4' o localhost
    app.run(host='localhost', port=8888)
