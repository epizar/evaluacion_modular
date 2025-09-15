import requests

url = "http://127.0.0.1:5000/predict"
payload = {
    "features": [14.2, 20.0, 92.0, 640.0, 0.1, 0.15, 0.2, 0.08, 0.2, 0.06,
                 0.6, 1.0, 4.5, 50.0, 0.007, 0.025, 0.03, 0.01, 0.02, 0.004,
                 16.0, 27.0, 115.0, 800.0, 0.14, 0.3, 0.35, 0.12, 0.25, 0.08]
}
response = requests.post(url, json=payload)
print("Prediction:", response.json())
