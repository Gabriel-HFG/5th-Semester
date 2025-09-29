birthdays = {
    "Gabriel": "2008-07-28",
    "Hyrum": "2008-02-14",
    "Joseph": "2008-02-14",
}

while True:
    name = input("\ntype Quit to exit.\nDictionary to create a new dictionary\nEnter a name: ").capitalize()
    if name == "Quit":
        break
    if name == "Dictionary":
        new_birthdays = {}
        while True:
            person = input("Enter a name (or type 'done' to finish): ").capitalize()
            if person == "Done":
                break
            date = input(f"Enter {person}'s birthday (YYYY-MM-DD): ")
            new_birthdays[person] = date

        with open("birthdays.txt", "w") as file:
            for person, date in new_birthdays.items():
                file.write(f'{person}: {date},\n')
        print("Dictionary saved to birthdays.txt")

        with open("birthdays.txt", "r") as file:
            content = file.read()
            print("Contents of birthdays.txt:\n")
            print(content)
        continue

    birthday = birthdays.get(name)
    if birthday:
        print(f"{name}'s birthday is {birthday}")
    else:
        print(f"Sorry, we don't have birthday information for {name}")
        birthdate = input("What is their birthday? ")
        birthdays[name] = birthdate
