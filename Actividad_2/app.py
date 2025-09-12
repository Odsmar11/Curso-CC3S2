from flask import Flask, jsonify
import os
import sys

app = Flask(__name__)

PORT = int(os.getenv("PORT", "8080"))
MESSAGE = os.getenv("MESSAGE", "Hola a todos")
RELEASE = os.getenv("RELEASE", "v0")

@app.route("/", methods=["GET"])
def root():
    return jsonify({
        "message": MESSAGE,
        "release": RELEASE
    })

if __name__ == "__main__":
    print(f"[INFO] Starting app on port {PORT}", file=sys.stdout)
    app.run(host="0.0.0.0", port=PORT)
