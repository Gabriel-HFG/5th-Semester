def random_13_letters():
    import random
    letters = []
    Alphabet = ["A","A","A","A","A","A","A","A","A",
                "B","B",
                "C","C",
                "D","D","D","D",
                "E","E","E","E","E","E","E","E","E","E","E","E",
                "F","F",
                "G","G","G",
                "H","H",
                "I","I","I","I","I","I","I","I","I",
                "J",
                "K",
                "L","L","L","L",
                "M","M",
                "N","N","N","N","N","N",
                "O","O","O","O","O","O","O","O",
                "P","P",
                "Q",
                "R","R","R","R","R","R",
                "S","S","S","S",
                "T","T","T","T","T","T",
                "U","U","U","U",
                "V","V",
                "W","W",
                "X",
                "Y","Y",
                "Z"]

    for i in range(0,13):
        i = random.choice(Alphabet)
        letters.append(i)
    return " ".join(letters), letters

def scrabble_score(word):
    score_chart = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }
    
    score = 0
    word = word.upper()
    
    for letter in word:
        for points, letters in score_chart.items():
            if letter in letters:
                score += points
                break            
    return score

def main():
    while True: 
        random_letters, random_letters_list = random_13_letters()
        print(f"Random 13 letters: {random_letters}")

        user_word = input("Type enter to end program\nEnter a word to calculate its Scrabble score: ")

        if user_word == "":
            break

        valid = True
        cheating_letters = []
        for letter in user_word:
            if letter.upper() in random_letters_list:
                random_letters_list.remove(letter.upper())
            else:
                cheating_letters.append(letter.upper())
                valid = False
        
        if not valid:
            print(f"\nYou do not have the letter or letters: {" ".join(cheating_letters)}\n")
            continue
        
        with open("words.txt", "r") as file:
            words = {word.lower() for word in file.read().splitlines()}
        
        if user_word.lower() not in words:
            print("Not a valid word\n")
            continue

        total_score = scrabble_score(user_word)
        print(f"The Scrabble score for '{user_word.upper()}' is: {total_score}\n")

main()
