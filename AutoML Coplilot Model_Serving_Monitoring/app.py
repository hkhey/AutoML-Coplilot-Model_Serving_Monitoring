import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Replace with your actual scoring URI and key
SCORING_URI = (
    "http://8555a98e-c394-4884-9938-262121f307b0.francecentral.azurecontainer.io/score"
)
# If the service is authenticated, set the key or token here
AUTH_KEY = "bexCz5TwmdBanpKAdRfTzvIIvUyiCqFN"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Receive data from the POST request
    data = request.form.to_dict()
    data = {
        "Inputs": {
            "data": [
                data,
            ]
        },
        "GlobalParameters": {"method": "predict"},
    }

    # Send the data to the external API
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + AUTH_KEY,
    }
    response = requests.post(SCORING_URI, json=data, headers=headers)

    # Return the response from the external API to the client
    return render_template("index.html", prediction_result=response.json())


if __name__ == "__main__":
    app.run(debug=True)
