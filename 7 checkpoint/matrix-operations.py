def matrix_print(matrix):
    print(f"  {" ". join(f"{i:4}" for i in range(1,5))}")
    print("-" * 25)
    i = 0
    for row in matrix: 
        i += 1
        print(f"{i}.{" ".join(f"{num:4}" for num in row)}")

def sum_matrix(matrix, row):
    return sum(matrix[row])

def sum_matrix_col(matrix, col):
    return sum((row[col]) for row in matrix)

def change_value(matrix,row,col,number):
     matrix[row][col] = number
     return matrix

def main():

    matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
    while True:
        what = input("what to do\n1. Sum row\n2. Sum col\n3. Change val\n4. Print Matrix\n5. Exit\nInput: ")
        if what == "1":
            row = int(input("Which row sum would you like to print?: "))
            print(sum_matrix(matrix,row - 1))
        if what == "2":
            col = int(input("Which col would you like to sum: "))
            print(sum_matrix_col(matrix,col - 1))
        if what == "3":
            row = int(input("Row in which number to change is located: "))
            col = int(input("Col in which number to change is located: "))
            number = int(input("number which is replacing the number: "))
            change_value(matrix,row - 1,col - 1,number)
        if what == "4":
            matrix_print(matrix)
        if what == "5":
            exit()

main()