def num_check(number1):
    return number1.isnumeric()
    

def main():
    number = input("Input a number to start counting: ")
    while not num_check(number):
        number = input("Enter digit: ")

    while True:
        step_and_start = input("input the step size: ")
        while not num_check(step_and_start):
            step_and_start = input("input the step size: ")
        if int(step_and_start) == 0:
            print("number must not be 0")
        else:
            break

    step_and_start = int(step_and_start)
    number = int(number)

    for i in range(step_and_start, number + 1, step_and_start):
        print(i)

main()