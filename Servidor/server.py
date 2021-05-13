from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
CORS(app)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'usuario@gmail.com', #TODO: Change by your gmail
    "MAIL_PASSWORD": 'password123' #TODO: Change by your password
}
app.config.update(mail_settings)
mail = Mail(app)

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

# Sent email 
@app.route("/email", methods=['POST'])
def subscribed_email():
    if request.method == 'POST':
        try:
            data = request.json #[email, game]
            send_email('You are Subscribed!',[data[0]], "Game: " + data[1]['name'] + "\nPrice: " + data[1]['price'])
            return jsonify({"status": "ok", "email":"sended"})
        except:
            print("Error email method")


def send_email(subject,recipients,body):
    with app.app_context():
        msg = Message(subject=subject,
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=recipients,
                      body=body)
        mail.send(msg)

if __name__ == "__main__":
    # 'ipv4' o localhost
    app.debug = True
    app.run(host='localhost', port=8888)