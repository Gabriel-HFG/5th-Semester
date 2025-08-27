def main():
    while True:
        something = input("Say hi\nInput: ")

        if something.lower() == "hello":
            print("$100")
            break

        something_test = something.lower().replace("h","")
        if not something == something_test:
            print("$20")

        else:
            print("$0")

main()