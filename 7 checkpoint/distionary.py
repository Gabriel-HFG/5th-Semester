# capitals = {
#     "Germany": "Berlin",
#     "Canada": "Ottawa",
#     "England": "London"
#     }

# capitals["Italy"] = "Rome" #way to add new capitals
# del capitals["England"] #way to delete capitals
# capitals.pop("Canada") # second way to delete capitals

# capitals.clear() #way to clear the dictionary

# print(capitals)

# houses = {
#     "Harry": "Gryffindor",
#     "Hermione": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
#     }

# for house in houses: print(f"Name: {house}, House: {houses[house]}")

# students = {
#     "Name": ["Hermione", "Ron", "Draco", "Harry"],
#     "Houses": ["Gryffindor", "Gryffindor", "Slytherin", "Gryffindor"],
#     "Patronus": ["Otter", "Jack Russell Terrier", "None", "Stag"],
#     }

# for i in range(len(students["Name"])):
#     print(f"Name: {students['Name'][i]}, House: {students['Houses'][i]}, Patronus: {students['Patronus'][i]}")

students = [{
    "name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}
]

for student in students:
    print(f"Name: {student['name']}, House: {student['house']}, Patronus: {student['patronus']}")
    print()