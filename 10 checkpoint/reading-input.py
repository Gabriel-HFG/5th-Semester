def main():
  number = read_input("Please type in a number: ", 5, 10)
  print("You typed in:", number)


def read_input(prompt, min_value, max_value):
    while True:
        try:
            number = int(prompt)
            if number < min_value or number > max_value:
                print(f"Input must be between {min_value} and {max_value}.")   
                raise ValueError
            return number
        except ValueError:
            prompt = input(f"Please enter a number between {min_value} and {max_value}: ")
    
main()