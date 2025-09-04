input = input("do something: ").lower()
result = ""

for char in input:
    if char.isalpha():
        result += chr(ord("z") - (ord(char) - ord("a")))
    else:
        result += char
print(result)
