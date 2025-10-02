def number(number):
    return number.isnumeric()

number1 = eval(input("Input number\nInput: "))
while not number(number1):
    number1 = eval(input("Input valid number\nInput: "))

print()

