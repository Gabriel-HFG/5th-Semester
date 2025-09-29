dictionary = {
    "color": "black",
    "age": 29,
}

print(dictionary.values())
for v in dictionary.values():
    print(v)

print(dictionary.keys())
for k in dictionary.keys():
    print(k)

print(dictionary.items())
for item in dictionary.items():
    print(item)

for k, v in dictionary.items():
    print(f"{k} -> {v}")

#get
picnic_items = {"apples": 5,"cups": 2,}
print(f"Im bringing {picnic_items.get("cups")} cups")
print(f"Im bringing {picnic_items.get("eggs", 0)} eggs")

#setting default values
pet_info = {"name": "Puka", "age": 5}
pet_info.setdefault("color", "black")
print(pet_info)