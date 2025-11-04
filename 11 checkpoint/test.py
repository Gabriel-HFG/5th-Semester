# ...existing code...
# import random
#
# for i in range(10):
#     coin = random.choice(['Heads', 'Tails'])
#     print(coin)
#
# random_number = random.randint(1, 100)
# print(f'Random number between 1 and 100: {random_number}\n')
#
# cards = ["Jack", "Queen", "King", "Ace"]
# random.shuffle(cards)
# for card in cards: print(card)

import statistics

# print(statistics.mean([1, 2, 3, 4, 5]))

import sys
import cowsay

def main():
    if len(sys.argv) < 2:
        print("Usage: python Libraries.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    cowsay.cow(f"Hello, my name is {name}")

if __name__ == "__main__":
    main()
# ...existing code...