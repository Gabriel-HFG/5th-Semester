from sympy import isprime
    
num = int(input("Enter a number here: "))
output = ["Nothing"]

if isprime(num):
    output.append("Prime")
if num % 5 == 0:
    output.append("Buzz")
if num % 3 == 0:
    output.append("Fizz")

result = " ".join(output[1:]).replace(" ", "")
print(result)