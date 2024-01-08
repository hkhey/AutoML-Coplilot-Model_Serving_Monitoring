import json

import pandas as pd
import requests

data = pd.read_csv("sample_inference_data.csv")
data = data.drop(columns=["Timestamp", "Location", "Future_weather_condition"]).to_dict(
    orient="records"
)
# data = data.drop(columns=['Future_weather_condition'])
url = (
    "http://8555a98e-c394-4884-9938-262121f307b0.francecentral.azurecontainer.io/score"
)
headers = {
    "Content-Type": "application/json",
    "Authorization": ("Bearer " + "bexCz5TwmdBanpKAdRfTzvIIvUyiCqFN"),
}


for i, record in enumerate(data):
    inference_data = {
        "Inputs": {
            "data": [
                record,
            ]
        },
        "GlobalParameters": {"method": "predict"},
    }
    inference_data = json.dumps(inference_data)
    r = requests.post(url, data=inference_data, headers=headers)
    print(str(i) + ":" + str(record) + "\n" + str(r.json()) + "\n")
