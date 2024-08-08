def check_number(num):

    if num > 0:
        print(f"{num} is positive.")
    elif num < 0:
        print(f"{num} is negative.")
    else:
        print("The number is zero.")

# Taking input
num = float(input("Enter a number: "))  # Using float to handle decimal inputs as well

# Calling the function
check_number(num)
