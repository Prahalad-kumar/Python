def area_of_rectangle(length, width):
    area = length * width
    return area

# Taking input from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculating the area of the rectangle
area_of_rectangle = area_of_rectangle(length, width)

#  the result
print(f"The area of the rectangle with length {length} units and width {width} units is: {area_of_rectangle:.2f} square units")

"""* We define a function calculate_area_of_rectangle that takes the length and width of the rectangle as parameters and computes the area using the formula length×width.
   * We prompt the user to enter the length and width of the rectangle.
   * We call the area_of_rectangle function with the user-provided length and width to compute the area.
   * Finally, we print the calculated area of the rectangle, formatted to two decimal places for clarity."""