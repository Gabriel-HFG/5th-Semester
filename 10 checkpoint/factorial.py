def main():
    while True:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Invalid input. Please enter a non-negative integer.")
            continue
        result = factorial(number)
        print(f"The factorial of {number} is {result}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    
main()