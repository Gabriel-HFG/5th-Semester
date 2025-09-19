def write_numbers(filename):
    the_list = input("Enter a list of numbers seperated with commas: ")
    the_list = list(the_list)
    with open(filename, "w") as file:
        for number in the_list:
            file.write(number + "\n")

def read_numbers(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        print("".join(lines))

def find_largest(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        print((f"Largest number: {max(lines)}"))


def main():
    while True:
        options = input("1. to write in file\n2.to display file stuff\n3.Exit\nInput: ")
        if options == "1":
            write_numbers("Largest.txt")
            find_largest("Largest.txt")

        if options == "2":
            file_name = str(input("Enter list name: "))
            file_name = file_name + ".txt"
            read_numbers(file_name)
            find_largest(file_name)

        if options == "3":
            break

main()