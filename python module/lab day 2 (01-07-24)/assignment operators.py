#Q.2 Write a program for assignment operators
# Assignment operators program

def assignment_operators():
    a = 10
    b = 5

    # Demonstrating assignment operators
    print("Initial values:")
    print("a =", a)
    print("b =", b)

    # Addition assignment
    a += b
    print("\nAfter 'a += b':")
    print("a =", a)

    # Subtraction assignment
    a -= b
    print("\nAfter 'a -= b':")
    print("a =", a)

    # Multiplication assignment
    a *= b
    print("\nAfter 'a *= b':")
    print("a =", a)

    # Division assignment
    a /= b
    print("\nAfter 'a /= b':")
    print("a =", a)

    # Modulus assignment
    a %= b
    print("\nAfter 'a %= b':")
    print("a =", a)

    # Floor division assignment
    a //= b
    print("\nAfter 'a //= b':")
    print("a =", a)

    # Exponentiation assignment
    a **= b
    print("\nAfter 'a **= b':")
    print("a =", a)

assignment_operators()


"""in this program 
*Initially, we initialize two variables a and b with values 10 and 5 respectively.
*Various assignment operators like +=, -=, *=, /=, %=, //=, and **= are applied to a with respect to b.
"""