def main():
  number = read_input("Please type in a number: ", 5, 10)
  print("You typed in:", number)


def read_input(prompt, min_value, max_value):
    while True:
        if prompt.isdigit() and min_value <= int(prompt) <= max_value:
            return int(prompt)
        else:
            prompt = input(f"Please enter a number between {min_value} and {max_value}: ")
    
main()