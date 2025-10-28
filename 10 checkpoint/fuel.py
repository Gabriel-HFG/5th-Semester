while True:
    fraccion = input("Enter a fraction (numerator/denominator) or enter to end the program: ")
    if fraccion == "":
        break
    try:
        rounded_value = round(eval(fraccion) * 100)
        if rounded_value <= 1 and rounded_value >= 0:
            print("E")
        if rounded_value >= 99 and rounded_value <= 100:
            print("F")
        if rounded_value > 1 and rounded_value < 99:
            print(f"{rounded_value}%")
        if rounded_value > 100:
            print("Invalid input. Please enter a valid fraction.")
    except:
        print("Invalid input. Please enter a valid fraction.")