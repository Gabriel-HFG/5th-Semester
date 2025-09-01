mass = input("Enter a mass in kilograms to calculate the energy\nInput: ")
while not mass.isnumeric(): mass = input("Input valid number\nInput: ")

print(f"the energy of {int(mass)} is {int(mass) * (300000000 ** 2)}")