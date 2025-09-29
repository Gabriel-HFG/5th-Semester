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

