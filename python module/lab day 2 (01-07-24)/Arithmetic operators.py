
#Q.1 Write a program for arithmatic operators
def arithmetic_operations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Modulus:", a % b)
    print("Exponentiation:", a ** b)
    print("Floor Division:", a // b)

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calling the function with user input
arithmetic_operations(num1, num2)

"""*Inside the function, various arithmetic operations like addition, subtraction, multiplication, division, modulus, 
exponentiation, and floor division are performed and printed.
*We take user input for two numbers (num1 and num2) and call the arithmetic_operations function with these inputs."""