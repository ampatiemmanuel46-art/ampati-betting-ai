from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "name": "AMPATI BETTING AI",
        "status": "Running",
        "features": [
            "Football match analysis",
            "Correct score predictions",
            "BTTS analysis",
            "Odds analysis",
            "Live match analysis"
        ],
        "message": "Welcome to AMPATI BETTING AI!"
    })

@app.route("/health")
def health():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
