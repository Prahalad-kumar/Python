def area_of_triangle(base, height):
    area = 0.5 * base * height
    return area

# Taking input from the user
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculating the area of the triangle
area_of_triangle = area_of_triangle(base, height)

# the result
print(f"The area of the triangle with base {base} units and height {height} units is: {area_of_triangle:.2f} square units")

"""*We define a function calculate_area_of_triangle that takes the base and height of the triangle as parameters and computes the area.
  *We prompt the user to enter the base length and height of the triangle.
  *We call the area_of_triangle function with the user-provided base and height to compute the area.
  *Finally, we print the calculated area of the triangle, formatted to two decimal places for clarity.
"""