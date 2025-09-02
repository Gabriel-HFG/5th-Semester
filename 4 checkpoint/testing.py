input = input("do something: ").lower()

def main(input):
    result = ""
    for char in input:
        if char.isalpha():
            result += chr(ord("z") - (ord(char) - ord("a")))
        else:
            result += char
    print(result)

main(input)