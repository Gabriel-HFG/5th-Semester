# Read the words into a list
with open("words.txt", "r") as file:
    words = {word.lower() for word in file.read().splitlines()}

# Example variable
my_word = "nun"

# Check if it's in the list
if my_word.lower() in words:
    print(f"{my_word} is in the list!")
else:
    print(f"{my_word} is NOT in the list.")