def area_of_square(side):
    area = side * side
    return area

# Taking input from the user
side = float(input("Enter the side length of the square: "))

# Calculating the area of the square
area_of_square = area_of_square(side)

#  the result
print(f"The area of the square with side length {side} units is: {area_of_square:.2f} square units")

"""* We define a function calculate_area_of_square that takes the side length of the square as a parameter and computes the area using the formula side×side.
   * We prompt the user to enter the side length of the square.
   * We call the area_of_square function with the user-provided side length to compute the area.
   * Finally, we print the calculated area of the square, formatted to two decimal places for clarity."""