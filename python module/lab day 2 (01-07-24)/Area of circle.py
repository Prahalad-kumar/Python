#he programm is for calculate area of circle
def area(radius):
    #Here we take the value of pi is 3.14

    area=3.14*(radius**2)

    return area
#Taking input from user
radius=float(input("Type the radius of circle="))

#Calling the area function

area=area(radius)
#Result
print("The area of circle is =",area,"square units")

""" * We define a function area that takes the radius of the circle as a parameter and computes the area using the formula (πxrxr).
    *We prompt the user to enter the radius of the circle.
    *We call the area function with the user-provided radius to compute the area.
    *Finally, we print the calculated area, formatted to two decimal places for clarity.
    
 ."""