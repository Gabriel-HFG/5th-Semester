import random

number = random.randint(1, 5)
guess = input("Guess a random number Input: ")
if int(number) == int(guess): print("Correct guess the number was: ", guess)
else: print("Incorrect guess number the number was: ", number)