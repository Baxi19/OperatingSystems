from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Games list
games = []

# Index
@app.route('/')
def index():
  return "<h1>Welcome to SO Server</h1>"

# Get Games
@app.route("/getGames", methods=['GET'])
def getGames():
    global games
    return jsonify({ "array": games })

# Load from 24 to 24 Games 
@app.route("/loadGames", methods=['POST'])
def loadGames():
    global games
    if request.method == 'POST':
        games.extend(request.json['array'])
        return jsonify({"status": "ok"})

# Delete all games
@app.route("/deleteAllGames", methods=['GET'])
def deleteAllGames():
    global games
    if request.method == 'GET':
        games = []
        return jsonify({"array": games})

# Update Amazon Game
@app.route("/updateAmazonGame", methods=['PUT'])
def updateAmazonGame():
    global games
    data = request.json['games']
    for game in games:
        if game['name'] == data['name']:
            game['price'] = data['price']
            game['store'] = "Amazon"
            return jsonify({"array": games})

# Update Time Game
@app.route("/updateTimeGame", methods=['PUT'])
def updateTimeGame():
    global games
    data = request.json['games']
    for game in games:
        if game['name'] == data['name']:
            game['time'] = data['time']
            return jsonify({"array": games})

# Update MetaData Game
@app.route("/updateMetaDataGame", methods=['PUT'])
def updateMetaDataGame():
    global games
    data = request.json['games']
    for game in games:
        if game['name'] == data['name']:
            game['meta'] = data['meta']
            return jsonify({"array": games})


if __name__ == "__main__":
    # 'ipv4' o localhost
    app.debug = True
    app.run(host='localhost', port=8888)