alphabet = "abcdefghijklmnopqrstuvwxyz" #The alphabet

message = input("Enter a message: ").lower() #The message to be ciphered
cipher = "" #The ciphered message list
i = 0 #Index counter for the message

while i < len(message): #Loop through each character in the message. 
    ch = message[i] #Get the character at the current index

    if ch in alphabet: #If the character is in the alphabet continue
        pos = alphabet.find(ch) #Find the position of the character in the alphabet
        cipher += alphabet[25 - pos] #Get the character at the opposite position in the alphabet and add it to the ciphered message
    else: #If the character is not in the alphabet (space, punctuation, number) just add it to the ciphered message
        cipher += ch #Add the character to the ciphered message
    i += 1 #Increment the index counter

print("Ciphered message: ", cipher) #Print the ciphered message