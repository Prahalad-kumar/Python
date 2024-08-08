4#Q.3Write a program for Bitwise operators
def bitwise_operators(a, b):
    # Bitwise AND
    print(f"{a} & {b} =", a & b)

    # Bitwise OR
    print(f"{a} | {b} =", a | b)

    # Bitwise XOR
    print(f"{a} ^ {b} =", a ^ b)

    # Bitwise NOT (Complement)
    print(f"~{a} =", ~a)
    print(f"~{b} =", ~b)

    # Bitwise Left Shift
    print(f"{a} << 2 =", a << 2)

    # Bitwise Right Shift
    print(f"{a} >> 2 =", a >> 2)
# Taking input from user
num1 =int  (input("Enter first number: "))
num2 = int (input("Enter second number: "))

# Calling the function with example values
bitwise_operators(num1, num2)

"""* We define a function bitwise_operators that takes two integers a and b as parameters.
   * Inside the function, various bitwise operators such as & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), and >> (right shift) are demonstrated."""