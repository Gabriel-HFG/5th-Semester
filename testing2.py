alphabet = "abcdefghijklmnopqrstuvwxyz"

message = input("Enter a message: ")
cipher = ""
i = 0

while i < len(message):
    ch = message[i]

    if ch in alphabet:
        pos = alphabet.find(ch)
        cipher += alphabet[25 - pos]
    else:
        cipher += ch
    i += 1

print("Ciphered message: ", cipher)