message = input("Enter a message: ")

char_count = {}
for char in message:
    counter = char_count.get(char,0) + 1
    char_count[char] = counter

print(char_count)
print(f"There are: {len(message)} characters in your message.")

repeated = max(char_count, key=char_count.get)
print(f"The most repeated character is '{repeated}' which appears {char_count[repeated]} times.")