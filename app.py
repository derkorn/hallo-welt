from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379)

@app.route("/")
def hallo():
    besuche = redis.incr("besuche")
    return f"Hallo Welt! Diese Seite wurde {besuche} Mal aufgerufen."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)