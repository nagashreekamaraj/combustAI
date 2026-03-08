from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np

app = Flask(__name__)
CORS(app)

model = tf.keras.models.load_model("combustion_model.keras")

latest_result = {}

@app.route("/predict", methods=["POST"])
def predict():

    global latest_result

    data = request.json

    features = np.array([
        data["AT"],
        data["AP"],
        data["AH"],
        data["AFDP"],
        data["GTEP"],
        data["TIT"],
        data["TAT"],
        data["TEY"],
        data["CDP"],
        data["CO"],
        data["NOX"]
    ]).reshape(1, -1)

    prediction = model.predict(features)

    if prediction[0][0] > 0.5:
        result = "Complete Combustion"
    else:
        result = "Incomplete Combustion"

    latest_result = {
        "sensor_data": data,
        "result": result
    }

    return jsonify({"result": result})


@app.route("/latest", methods=["GET"])
def latest():

    return jsonify(latest_result)


if __name__ == "__main__":
    app.run(debug=True)