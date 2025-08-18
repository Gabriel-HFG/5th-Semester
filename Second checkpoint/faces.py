
def convert(argument):
    argument = argument .replace(":)", "☺️").replace(":(", "🙁")
    return argument

def main():
    something = convert(input("Type something\nInput: "))
    print(something)

main()