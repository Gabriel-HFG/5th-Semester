import requests
import json

universities = {
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
}


data_link = "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json"
uni = (requests.get(data_link)).json()

def search_universities_by_name(uni):
    results = []
    for unii in uni:
        if name in unii['name'].lower():
            results.append(unii)
        return results

while True:
        name = str(input("\nEnter a name or 'exit': ").strip().lower())
        if name == 'exit':
            break

        results = search_universities_by_name(uni)

        if not results:
            print("No universities found.")
        else:
            print(f"\nFound {len(results)} matches:\n")
            for uni in results[:10]:  # show first 10 results
                print(f" - {uni['name']} ({uni['country']})")
                print(f"   Domain(s): {', '.join(uni['domains'])}")
                print(f"   Website(s): {', '.join(uni['web_pages'])}\n")

univercity = input("Type a university name: ")

if univercity in universities:
    print(f"{univercity} has {universities[univercity]['majors']} majors.")
    print(f"Average semester cost: {universities[univercity]['average_semester_cost']}")
    print(f"Closest campus: {universities[univercity]['closest_campus']}")
    print(f"Distance (km): {universities[univercity]['distance_km']}")
else:
    print("University not found.")