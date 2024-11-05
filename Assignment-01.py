"""Question - 01"""

x = 10
y = 2
z = 4

x = x * y

y = y * z

y = x + z

print("The value of y is:", y)


"""Question - 02"""

room_width = int(input("What is Room's width: "))

room_length = int(input("What is Room's length: "))

room_area = room_length * room_width

print("The area of the room is:", room_area)


"""Question - 03"""

# 'A': This is a character literal. It is enclosed in single quotes, indicating that it represents a single character.


"""Question - 04"""

# Sizes of data types in bytes
size_char = 1  
size_int = 4   
size_double = 8 

# Number of variables
num_ints = 3   # x, y, z
num_chars = 2  # a, b
num_doubles = 2 # j, k

# Calculate total memory required
total_memory = (num_ints * size_int) + (num_chars * size_char) + (num_doubles * size_double)

# Display the total memory required in bytes
print("Total memory required in bytes:", total_memory)


"""Question - 05 """

x, y, z = 7, 20, 28

print("x:", x)
print("y:", y)
print("z:", z)


"""Question - 06 """

# Unary operators are operators that operate on a single operand.

x = True
print(not x)

# Binary operators are operators that operate on two operands.

x = 2

y = 2

z = x + y

print(z)

# Ternary operators are operators that operate on three operands.


a = 2
b = 4

res = a if a > b else "a is not greater than b!"

print(res)


"""Question - 07 """

# Python uses indentation (typically 4 spaces or a tab) to group statements as a block. There are no braces { } or other symbols used to define a block.

"""
if condition:
    # Start of block
    statement1
    statement2
    # End of block
"""



"""Question - 08 """

w = 5
x = 4
y = 8
z = 2

result1 = x + y

result2 = z * 2

result3 = y / x

result4 = y - z

result5 = w % 2


print(result1)
print(result2)
print(result3)
print(result4)
print(result5)


"""Question - 09 """

x = 5
b = 3
c = 4
z = 2


y = 6 * x

a = 2 * b + 4 * c

y1 = x ** 2

g = (x + 2) / (z ** 2)

y2 = (x ** 2) / (z ** 2)


print("y = 6x:", y)
print("a = 2b + 4c:", a)
print("y = x^2:", y1)
print("g = (x + 2) / z^2:", g)
print("y = x^2 / z^2:", y2)


"""Question - 10 """

#Algorithm
"""
1- Input length
2- Input width
3- Calculate Perimeter = 2 * (length + width)
4- Calculate Area = length * width
5- Display Perimeter
6- Display Area
"""

width = int(input("Enter the width of rectangle: "))

length = int(input("Enter the length of rectangle: "))


perimeter = 2 * (length + width)

area = length * width

print("Perimeter of a rectangle: ", perimeter)
print("Area of a rectangle: ", area)


"""Question - 11"""

# Algorithm of this problem
"""
1 - Input the cost of the item.
2 - Define the tax rates:
        State's sales tax rate = 4% (or 0.04)
        City's sales tax rate = 1.5% (or 0.015)
        Luxury tax rate = 10% (or 0.10), applicable only if the cost > 50000
3 - Calculate the basic sales tax:
        Basic sales tax = (State's tax rate + City's tax rate) * cost of the item
4 - Determine if the luxury tax applies:
        If the cost of the item is greater than 50000, calculate the luxury tax as:
    
        Luxury_tax=luxury_tax_rate x cost_of_item
        Otherwise, set luxury tax = 0
5 - Calculate the total tax:
        Total tax = Basic sales tax + Luxury tax
6 - Calculate the total price:
        Total price = Cost of item + Total tax
7 - Output the following:
    Basic sales tax
    Luxury tax (if applicable)
    Total tax
    Total price

"""

cost_of_item = float(input("Enter the cost of an item: "))

state_sale_tax_rate = 4/100

city_sale_tax_rate = 1.5/100

luxury_tax_rate = 10/100

basic_sale_tax = (state_sale_tax_rate + city_sale_tax_rate) * cost_of_item

if cost_of_item > 50_000:
    luxury_tax = luxury_tax_rate * cost_of_item

else:
    luxury_tax = 0


total_tax = basic_sale_tax + luxury_tax


total_price = cost_of_item + total_tax


print("Basic sales tax", basic_sale_tax)
print("Luxury tax: ", luxury_tax)
print("Total tax: ", total_tax)
print("Total price: ", total_price)


"""Question - 12 """

# Algorithm
"""
1 - input from user about radius and price of pizza

2 - find the area of a pizza by using formula: area = pi * (radius ** 2)

3 - calculate the price per square inch of pizza by dividing price/area

4 - display the price_per_sq_inch_pizza

"""
import cmath

radius = float(input("Enter the radius of pizza: "))
price = float(input("Enter the price of pizza: "))

area = cmath.pi * (radius ** 2)

price_per_sq_inch = price / area


print("price_per_sq_inch_of_pizza: ", price_per_sq_inch)

"""Question - 13 """

a = 28
b = 32
c = 37
d = 24
e = 33

sum = a + b + c + d + e

average = sum / 5

print("Average: ", average)



"""Question - 14 """

# Error:

# incorrect assignment: number1 + number2 = sum


"""Question - 15 """

# Error:

# Incorrect Type casting : quotient = float<static_cast>(numberl) / number2;


"""Question - 16 """

"""

A) True

B) True

C) False

D) True

E) True

F) False

G) True

"""

