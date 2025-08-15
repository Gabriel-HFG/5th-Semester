def number(number):
    return number.isnumeric()

while True:
    determiner = input("\nWelcome to calculator\nPick calculation:\n1. Addition\n2. Subtraction\n3. Divicion\n4. Multiplication\nInput: ")
    while determiner not in {"1","2","3","4"}:
        determiner = input("Input between 1,2,3,4\nInput: ")

    number1 = input("Input number\nInput: ")
    while not number(number1):
        number1 = input("Input valid number\nInput: ")

    number2 = input("Input number\nInput: ")
    while not number(number2):
        number2 = input("Input valid number\nInput: ")

    number1 = int(number1)
    number2 = int(number2)

    if determiner == "1":
        print(f"\n{number1} + {number2} = {number1 + number2}\n")
    if determiner == "2":
        print(f"\n{number1} - {number2} = {number1 - number2}\n")
    if determiner == "3":
        print(f"\n{number1} / {number2} = {number1 / number2}\n")
    if determiner == "4":
        print(f"\n{number1} * {number2} = {number1 * number2}\n")

    determiner2 = input("Would you like to perform another calculation? (1. Yes, 2. no)\nInput: ")
    while determiner2 not in ("1","2"):
        determiner2 = input("Please perform a valid input... (1. Yes, 2. no)\nInput: ")
    if determiner2 == "1":
        continue
    else:
        print("\nThanks for using")
        exit()