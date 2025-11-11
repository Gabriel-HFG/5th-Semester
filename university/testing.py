import requests
import json

DATA_URL = "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json"

def load_universities():
    response = (requests.get(DATA_URL)).json()
    return response

def search_universities(universities, name):
    results = []
    for uni in universities:
        if name in uni['name'].lower():
            results.append(uni)

    return results

def main():

    search = input("Search local or web data? (l/w): ").strip().lower()
    while search not in ['l', 'w']:
        search = input("Please enter 'l' for local or 'w' for web: ").strip().lower()

    if search == 'l':
        universities_list = {
        "Tecmilenio": {
            "majors": 24,
            "average_semester_cost": 25000,
            "closest_campus": "Ciudad Juarez",
            "distance_km": 280,
        },
        "UACJ": {
            "majors": 37,
            "average_semester_cost": 5000,
            "closest_campus": "Ciudad Juarez",
            "distance_km": 280,
        },
        "upn": {
            "majors": 64,
            "average_semester_cost": 0,
            "closest_campus": "Chihuahua",
            "distance_km": 326,
        },
        "urn": {
            "majors": 29,
            "average_semester_cost": 10000,
            "closest_campus": "Juarez",
            "distance_km": 290,
        },
        "Tec de Monterrey": {
            "majors": 44,
            "average_semester_cost": 160000,
            "closest_campus": "Monterrey",
            "distance_km": 920,
        },
        "BYU_Pathway": {
            "majors": 30,
            "credit_cost": 3000,
            "closest_campus": "Online",
            "distance_km": 0,
        },
        "EAC": {
            "majors": 140,
            "average_semester_cost": 0,
            "closest_campus": "Thatcher",
            "distance_km": 466,
        },
        "tec_casas_grandes": {
            "majors": 8,
            "average_semester_cost": 3000,
            "closest_campus": "Casas Grandes",
            "distance_km": 27,
        },
        "La Salle": {
            "majors": 37,
            "average_semester_cost": 20000,
            "closest_campus": "Chihuahua",
            "distance_km": 280,
        },
        "IASG": {
            "majors": 1,
            "average_semester_cost": 145150,
            "closest_campus": "Chihuahua",
            "distance_km": 280,
        },
    }

        while True:
            univercityy = input("Type a university name or 'exit': ")
            if univercityy.lower() == 'exit':
                break

            if univercityy in universities_list:
                print(f"{univercityy} has {universities[univercityy]['majors']} majors.")
                print(f"Average semester cost: {universities[univercityy]['average_semester_cost']}")
                print(f"Closest campus: {universities[univercityy]['closest_campus']}")
                print(f"Distance (km): {universities[univercityy]['distance_km']}")
            else:
                print("University not found.")

    if search == 'w':
        universities = load_universities()
        while True:
            name = input("\nEnter a name or 'exit': ").strip().lower()
            if name == 'exit':
                break
            results = search_universities(universities, name)
            if not results:
                print("No universities found.")
            else:
                print(f"\nFound {len(results)} matches:\n")
                for uni in results[:10]:
                    print(f" - {uni['name']} ({uni['country']})")
                    print(f"   Domain(s): {', '.join(uni['domains'])}")
                    print(f"   Website(s): {', '.join(uni['web_pages'])}\n")

main()