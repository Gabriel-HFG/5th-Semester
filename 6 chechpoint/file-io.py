# names = []

# for i in range(3):
#     names.append(input("what is your name? "))

# print(names)

# for name in sorted(names):
#     print(f"hello {name}")


# name = input("what is your name? ")
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()


# write to a file

# with open("names.txt", "a") as file:
#     file.write(f"{input("what is your name? ")}\n") 


# read from a file

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in sorted(lines):
    print(f"hello {line.rstrip()}")