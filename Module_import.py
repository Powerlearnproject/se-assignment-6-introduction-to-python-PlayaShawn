import math

def calculate_circle_area(radius): #Calculate the area of a circle given its radius.
  
    return math.pi * radius ** 2

def calculate_hypotenuse(a, b): #Calculate the hypotenuse of a right-angled triangle given the lengths of the other two sides.

    
    return math.sqrt(a**2 + b**2)

# Example usage
radius = 63
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is {area}")

side_a = 7
side_b = 2
hypotenuse = calculate_hypotenuse(side_a, side_b)
print(f"The hypotenuse of a right-angled triangle with sides {side_a} and {side_b} is {hypotenuse}")
