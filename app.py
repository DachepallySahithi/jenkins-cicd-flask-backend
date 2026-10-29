from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Flask Backend is running!",
        "application": "Jenkins CI/CD Assignment",
        "status": "success"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/api/greet/<name>", methods=["GET"])
def greet(name):
    return jsonify({
        "message": f"Hello, {name}!",
        "service": "Flask Backend"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)