# This function 'username' takes one argument 'name' and prints it as the student's name
def username(name):
    # Printing the student's name
    print("Student Name:", name)

# Calling the 'username' function with different names as arguments
username("ali")  # Output: Student Name: ali
username("usman")  # Output: Student Name: usman

# This function 'add' takes two arguments 'a' and 'b', and prints their sum
def add(a, b):
    # Printing the sum of the two numbers
    print(a + b)

# Calling the 'add' function with different pairs of numbers
add(1, 22)  # Output: 23
add(112, 22)  # Output: 134
add(133, 22)  # Output: 155
add(1456, 22)  # Output: 1478


def square(number):
    return number * number

# Test the function
print(square(5))  # Output: 25
print(square(10))  # Output: 100


def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
print(is_even_or_odd(4))  # Output: Even
print(is_even_or_odd(7))  # Output: Odd


def find_max(a, b):
    if a > b:
        return a
    else:
        return b

# Test the function
print(find_max(10, 20))  # Output: 20
print(find_max(50, 30))  # Output: 50


def area_of_rectangle(length, width):
    return length * width

# Test the function
print(area_of_rectangle(5, 3))  # Output: 15
