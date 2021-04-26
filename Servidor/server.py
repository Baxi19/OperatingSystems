from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import inspect

app = Flask(__name__)
CORS(app)

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()

lock = threading.Lock()

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
    return jsonify({"size":len(games) ,"array": games})


# /loadGames
def add_24(games_list):
    global games
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    print ("Inside %s()" % caller)
    print ("Acquiring lock")
    with lock:
        print ("Lock Acquired")
        games.extend(games_list)


# Load from 24 to 24 Games 
@app.route("/loadGames", methods=['POST'])
def loadGames():
    global games
    if request.method == 'POST':
        add = Thread(add_24(request.json['array']))
        return jsonify({"status": "ok", "size": len(games)})


# Delete all games
@app.route("/deleteAllGames", methods=['GET'])
def deleteAllGames():
    global games
    if request.method == 'GET':
        games = []
        return jsonify({"array": games, "size": len(games)})


# /updateAmazonGame
def updateAmazon(data):
    global games
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    print ("Inside %s()" % caller)
    print ("Acquiring lock")
    with lock:
        print ("Lock Acquired")
        for game in games:
            if game['name'] == data['name']:
                game['price'] = data['price']
                game['store'] = "Amazon"
        

# Update Amazon Game
@app.route("/updateAmazonGame", methods=['PUT'])
def updateAmazonGame():
    update = Thread(updateAmazon(request.json['games']))
    global games
    return jsonify({"status": "ok", "size": len(games)})

# /updateTimeGame
def updateTime(data):
    global games
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    print ("Inside %s()" % caller)
    print ("Acquiring lock")
    with lock:
        print ("Lock Acquired")
        for game in games:
            if game['name'] == data['name']:
                game['time'] = data['time']

# Update Time Game
@app.route("/updateTimeGame", methods=['PUT'])
def updateTimeGame():
    update = Thread(updateTime(request.json['games']))
    global games
    return jsonify({"status": "ok", "size": len(games)})


# /updateMetaDataGame
def updateMeta(data):
    global games
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    print ("Inside %s()" % caller)
    print ("Acquiring lock")
    with lock:
        print ("Lock Acquired")
        for game in games:
            if game['name'] == data['name']:
                game['meta'] = data['meta']

# Update MetaData Game
@app.route("/updateMetaDataGame", methods=['PUT'])
def updateMetaDataGame():
    update = Thread(updateMeta(request.json['games']))
    global games
    return jsonify({"status": "ok", "size": len(games)})


if __name__ == "__main__":
    # 'ipv4' o localhost
    app.debug = True
    app.run(host='localhost', port=8888)