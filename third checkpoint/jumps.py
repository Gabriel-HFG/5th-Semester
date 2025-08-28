number = int(input("Input a number to start counting: "))
step_and_start = int(input("input the step size: "))

for i in range(step_and_start, number + 1, step_and_start):
    print(i)