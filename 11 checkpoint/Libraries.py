# import random

# for i in range(10):
#     coin = random.choice(['Heads', 'Tails'])
#     print(coin)

# random_number = random.randint(1, 100)
# print(f'Random number between 1 and 100: {random_number}\n')

# cards = ["Jack", "Queen", "King", "Ace"]
# random.shuffle(cards)
# for card in cards: print(card)

import statistics

# print(statistics.mean([1, 2, 3, 4, 5]))

import sys
import cowsay
cowsay.cow("Hello, World!")
# print("hello my name is", sys.argv[1])
# print(statistics.mean([float(sys.argv[1]), float(sys.argv[2])]))
try:
    print("Hello my name is", sys.argv[1])
except IndexError:
    print("No name provided as command line argument.")
    sys.exit(1)
