num = int(input("Input a number: "))

for i in range(1, num + 1):
    for i2 in range(1, num + 1):
        print(f"{i} * {i2} = {i * i2}")
    print("")