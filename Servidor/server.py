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

# Delete all
@app.route("/delete", methods=['GET'])
def delete():
    global games
    if request.method == 'GET':
        games = []
        return jsonify({"array": games, "size": len(games)})

# /games
def add(games_list):
    global games
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    print ("Inside %s()" % caller)
    print ("Acquiring lock")
    with lock:
        print ("Lock Acquired")
        games=games_list


# Load all Games 
@app.route("/games", methods=['POST'])
def games():
    global games
    if request.method == 'POST':
        req = Thread(add(request.json['array']))
        return jsonify({"status": "ok", "size": len(games)})


if __name__ == "__main__":
    # 'ipv4' o localhost
    app.debug = True
    app.run(host='localhost', port=8888)