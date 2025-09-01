

def main():
    while True:
        something = input("Say hi\nInput: ")
        if something.lower() == "hello":
            print("$0")

        if something.startswith("h"):
            print("$20")

        else:
            print("$100")
            break

main()