
def convert(argument):
    argument = argument .replace(":)", "☺️").replace(":(", "🙁")
    return argument

def main():
    something = input("Type something\nInput: ")
    something = convert(something)
    print(something)

main()