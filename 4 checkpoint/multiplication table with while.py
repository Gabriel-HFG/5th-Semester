def num_check(number1):
    return number1.isnumeric()
    

num = input("Input a number: ")
while not num_check(num):
    num = input("Input a number: ")


num = int(num)
i = 1
while i <= num:
    i2 = 1
    while i2 <= num:
        print(f"{i} * {i2} = {i * i2}")
        i2 += 1
    print("")
    i += 1