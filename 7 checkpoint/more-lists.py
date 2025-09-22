# List with strings

# names = ["Bob","Alex","Kevin"]
# names.append("Joseph")

# for name in sorted(names):
#     print(f"{name}")

# List with floats

# measurements = [-2.5,1.1,7.5,14.61,21.05,3.14]
# mean = sum(measurements)/len(measurements)
# print(f"Mean is: {mean}")

# List within list
# super_list = [[5,2,3],[4,1],[2,2,5,1]]
# print(super_list[1][0]) 

# grades = [["Shakira",8,"D"],["Bad bunny",0, "F"],["Gabriel",10,"C"]]
# for student in grades:
#     name = student[0]
#     grade = student[1]
#     letter = student[2]
#     print(f"{name} has a grade of {grade} which in group: {letter}")

# matrices 

matrix = [[1,2,3],[4,5,6],[7,8,9]]
new_matrix = []
final_matrix = []
i = 0

while i < 3:
    new_matrix = []
    for row in matrix:
        new_matrix.append(row[i])
    i += 1
    print(new_matrix)

