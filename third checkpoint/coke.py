def num_check(number1):
    return number1.isnumeric()

name = input("what is your name?: ")
money = 0

while True:
    coin = int(input(f"balance = {money}\nInput a coin (5, 10 or 25 cents only): "))
    if coin == 5 or 10 or 25:
        money = money + coin
        if money >= 50:
            break

print(f"Change = {money - 50}\nHere’s a Coke for {name}")