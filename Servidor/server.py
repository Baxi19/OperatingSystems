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
    return jsonify({"size":len(games) ,"array": games})

# Delete all
@app.route("/delete", methods=['GET'])
def delete():
    global games
    if request.method == 'GET':
        games = []
        return jsonify({"array": games, "size": len(games)})

# Load all Games 
@app.route("/games", methods=['POST'])
def games():
    global games
    if request.method == 'POST':
        games = request.json['array']
        return jsonify({"status": "ok", "size": len(games)})

if __name__ == "__main__":
    # 'ipv4' o localhost
    app.debug = True
    app.run(host='localhost', port=8888)