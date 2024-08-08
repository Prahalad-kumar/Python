# Determine if the number is even or odd
def check_num(number):
    Num= number % 2
    if(Num==1):
        print(f"The {number} is odd no")
    else:
        print(f"The {number} is even no")
    return 0
#Taking input from user.
num=int(input("Type the number="))
print(check_num(num))