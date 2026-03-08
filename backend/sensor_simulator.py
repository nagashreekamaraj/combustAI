import requests
import random
import time

url = "http://127.0.0.1:5000/predict"

while True:

    data = {
        "AT": random.uniform(3,6),
        "AP": 1018,
        "AH": 83,
        "AFDP": 3.5,
        "GTEP": 23,
        "TIT": 1086,
        "TAT": 549,
        "TEY": 134,
        "CDP": 11,
        "CO": random.uniform(0.2,1.0),
        "NOX": 80
    }

    response = requests.post(url, json=data)

    print("Sensor Data:", data)
    print("AI Prediction:", response.json())

    time.sleep(5)