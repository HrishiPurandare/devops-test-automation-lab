from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return "<!doctype html><title>Lab App</title><h1>Test Automation Lab</h1>"


@app.get("/api/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
