def lenght(list):
    lenght_list = len(list)
    return lenght_list

def mean(list):
    mean = sum(list) / len(list)
    return mean

def range_of_list(list):
    range = (f"{min(list)} - {max(list)} Difference: {min(list) -max(list)}")
    return range

def main():
    list = []

    while True:
        num = int(input("Input a number: "))
        if num == 0:
            break
        list.append(num)
        print(list)
        print(sorted(list))

    print(f"list lenght {lenght(list)}")
    print(f"List mean {mean(list)}")
    print(f"List range {range_of_list(list)}")

main()