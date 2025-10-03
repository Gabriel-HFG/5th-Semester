def random_13_letters():
    import random
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V", "W", "X", "Y", "Z"]
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


letters, list_letters = random_13_letters()
print(letters)
word = input("type your word: ").upper()
wrong_characters = []


valid = False
for i in word:
    if i in list_letters:
        list_letters.remove(i)
    else:
        wrong_characters.append(i)
        valid == True

if valid:
    print(f"Invalid input you do not have: {wrong_characters}")

if not valid:
    print(score(word))

