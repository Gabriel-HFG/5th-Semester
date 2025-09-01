num = int(input("Enter a number here: "))

if num % 5 == 0 and num % 3 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print("Number is not divisable by 3 or 5")