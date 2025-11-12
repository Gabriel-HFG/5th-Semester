import requests
import json

bitcoins = input("Enter your bitcoins")
api_key = "ed052f6f72151ca6d7f2c4ce6b714002367226c1b34fbbe1a9aa6b836206feea"

URL = ("https://rest.coincap.io/v3/assets?search=BTC?apiKey="+api_key)
info = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey="+api_key).json()
print(info["data"]["priceUsd"])
price = float(info["data"]["priceUsd"])
print(f"Total cost of: {bitcoins} is {price * float(bitcoins)}")