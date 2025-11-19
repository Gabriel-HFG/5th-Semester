import requests

def main():

    while True:
        get_joke = input("Would you like to hear a dad joke? (yes/no): ").strip().lower()
        while get_joke not in ["yes", "no"]:
            get_joke = input("Would you like to hear a dad joke? (yes/no): ").strip().lower()
            if get_joke == "no":
                print("Alright, no more jokes for now!")
                break
        if get_joke == "no":
            
            break
        if get_joke == "yes":
            joke = random_joke()
            print(joke)
    
def random_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {
        "Accept": "application/json",
        "User-Agent": "yomero (yomero@example.com)"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data["joke"]

main()