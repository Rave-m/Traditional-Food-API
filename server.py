from flask import Flask, request, jsonify
from flask_cors import CORS

import time
import dotenv

import os

dotenv.load_dotenv()

app = Flask(__name__)
CORS = CORS(app, origins="*")

@app.route("/")
def index():
    return "Alamakk, wes running to?"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))