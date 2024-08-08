
# Program to find the greatest of three numbers

def greatest(num1, num2, num3):
    # Using conditional statements to find the greatest number
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Calling the function to find the greatest number
greatest = greatest(num1, num2, num3)

# Result
print(f"The greatest number among {num1}, {num2}, and {num3} is: {greatest}")


"""* We define a function greatest that takes three numbers (num1, num2, num3) as parameters.
   * inside the function, conditional statements (if, elif, else) are used to determine which number is the greatest.
   * We call the greatest function with these input values to find the greatest number among them.
    * When you run this program, it will prompt you to enter three numbers, and then it will display which of those numbers is the greatest."""