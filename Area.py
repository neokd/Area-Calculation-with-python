# importing math module
import math


# Function to choose shape (rectangle, circle and square)
def area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    elif shape == "square":
        square_area()
    else:
        print("Enter the above only")


# Function to calculate the area of rectangle
def rectangle_area():
    l = float(input("Enter the length of the rectange : "))
    b = float(input("Enter the breadth of the rectangle : "))
    area = l * b
    print("The area of the rectangle is : ", area)


# Function to calculate the area of circle
def circle_area():
    r = float(input("Enter the radius of the circle : "))
    area = math.pi * r * r
    print("The area of the circle is : ", area)


# Function to calculate the area of square
def square_area():
    s = float(input("Enter the side of the square "))
    area = s * s
    print("the Area of the square is : ", area)


# Main Function
def main():
    shape = input("Enter the shape type : ")
    area(shape)


main()
