import requests
import json

song = input("What song are you looking for?: ")
requested = requests.get("https://itunes.apple.com/search", params={"entity": "song", "limit": 1, "term": song})
# requested = requests.get(f"http://www.apple.com/search?entity=song&limit=1&term="+song)
# print(json.dumps(requested.json(), indent=2))
search = requested.json()
for result in search["results"]:
    print(f"{result['trackName']} by {result['artistName']}")