import requests
import json

api_key = "ed052f6f72151ca6d7f2c4ce6b714002367226c1b34fbbe1a9aa6b836206feea"
api_key_2 = "a5fcdf69b876e95906642d1ecb78f650"

cryptocurrency = input("Enter the cryptocurrency (bitcoin,etherium,tether,dogecoin): ").lower().strip()
bitcoins = input(f"Enter {cryptocurrency}:")
URL = (f"https://rest.coincap.io/v3/assets/{str(cryptocurrency)}?apiKey="+api_key)
# print(URL)
info = requests.get(URL).json()
# print(info)
price = float(info["data"]["priceUsd"])

# URL = ("https://rest.coincap.io/v3/assets?search=BTC?apiKey="+api_key)
# info = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey="+api_key).json()
# price = float(info["data"]["priceUsd"])

print(f"Total cost of {cryptocurrency} coin is {price}\nYou have: {bitcoins} coins\nTotal USD value: ${(price * float(bitcoins)):,.2f}")