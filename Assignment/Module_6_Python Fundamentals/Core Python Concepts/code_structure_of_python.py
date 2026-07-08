# Import statement
import math

# Function definition
def calculate_area(radius):
    return math.pi * radius * radius

# Main program
radius = 5

if radius > 0:
    area = calculate_area(radius)
    print("Area of circle:", area)
else:
    print("Invalid radius")
