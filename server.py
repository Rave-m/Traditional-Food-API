from flask import Flask, request, jsonify
from flask_cors import CORS

import time
import dotenv

import os

from helper.functions import get_food_information

dotenv.load_dotenv()

app = Flask(__name__)
CORS = CORS(app, origins="*")

@app.route("/")
def index():
    return "Alamakk, wes running to?"

@app.route("/api/food-classification", methods=["POST"])
def food_detection():
    """
    Parameters:
        - image : image path

    Returns:
        - Detected objects
    """
    data = request.json
    image = data.get('image')

    if image is None:
        return jsonify({"error": "The 'image' field must be provided"}), 400

    try:
        # outputs = load_yolo_model("./model/food_classification/model.pt", image)
        outputs = ["nasi lemak", "roti canai", "teh tarik", "roti bakar", "kopi o"] # TODO: Implement food classification model

        response = {
            "objects": outputs
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/food-information", methods=["POST"])
def food_information():
    """
    Parameters:
        - food : food name

    Returns:
        - Food Name
        - 
    """
    data = request.json
    food_name = data.get('food')

    if food_name is None:
        return jsonify({"error": "The 'food' field must be provided"}), 400

    try:
        informations = get_food_information(food_name)

        response = {
            "informations": informations
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))