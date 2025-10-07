def random_13_letters():
    import random
    alphabet = ["A","A","A","A","A","A","A","A","A",
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
    letters_13 = []

    for i in range(0,13):
        i = random.choice(alphabet)
        letters_13.append(i)
    
    return " ".join(letters_13), letters_13

def score(word):
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
    for i in word:
        for point, letters in score_chart.items():
            if i in letters:
                score += point
    return score

while True: 
    letters, list_letters = random_13_letters()
    print(letters)
    word = input("type your word: ").upper()
    wrong_characters = []

    valid = True
    for i in word:
        if i in list_letters:
            list_letters.remove(i)
        else:
            wrong_characters.append(i)
            valid = False

    if not valid:
        print(f"Invalid input you do not have: {wrong_characters}")
        continue

    with open("words.txt", "r") as file:
        words = {word.lower() for word in file.read().splitlines()}

    if word.lower() not in words:
        print("Not a valid word")
        continue

    if word.lower() in words:
        print(f"your score is {score(word)}")