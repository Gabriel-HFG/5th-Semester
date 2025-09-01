
def convert(argument):
    return argument.replace(":)", "☺️").replace(":(", "🙁")

def main():
    something = convert(input("Type something\nInput: "))
    print(something)

main()