import random 
print("Welcome to the goblin game")
print("The best game ever")
player_name = input("What is your name\nInput: ")
print("|_|"*5)
goblin_position = random.randint(1, 5)
guess_position = int(input("Can you guess where the goblin is?: "))

while not guess_position == goblin_position:
    print("no")
    guess_position = int(input("Can you guess where the goblin is?: "))
print("good, you find the goblin")
