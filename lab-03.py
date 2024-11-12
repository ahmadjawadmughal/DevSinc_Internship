"""Task - 01"""


day = int(input("Enter the day in numeric (1-31): "))

month = int(input("Enter the month in numeric (1 - 12): "))

year = int(input("Enter the year in numeric (e.g: 23) : "))

if month * day == year:
    print("YOUR date is magic!")

else:
    print("Your date is not magic!")



"""Task - 02"""



length_rect1 = float(input("Enter the length of the rectangle 1: "))

width_rect1 = float(input("Enter the width of the rectangle 1: "))

length_rect2 = float(input("Enter the length of the rectangle 2: "))

width_rect_2 = float(input("Enter the width of the rectangle 2: "))

if True:
    area_rect1 = length_rect1 * width_rect1

    area_rect2 = length_rect2 * width_rect_2

    if area_rect1 > area_rect2:
        print("You area for rectangular 1 is: ",area_rect1, "greater than the area of rectangle 2: ",area_rect2)

    elif area_rect1 < area_rect2:
        print("You area for rectangular 2 is: ",area_rect2, "greater than the area of rectangle 1: ",area_rect1)

    else:
        print(f"Both areas of the rectangle are same: area_rectangle 1: {area_rect1} and the area_rectangle 2: {area_rect2}")



"""Task - 03"""


height = float(input("Enter the height of a person: ")) * 12  #converting into inches

weight = float(input("Enter the weight of a person: ")) * 2.20  #converting into feets

bmi = weight * (703/(height**2))


if bmi <= 18.5:
    print("This person is underweight!")

elif bmi >= 25:
    print("This person is overweight!")
        
else:
    print("Normal weight according to the height!")




"""Task - 04"""


object_mass = float(input("Enter an object mass: "))

obj_weight = object_mass * 9.8

print(f"The object's weight is {obj_weight:.2f} newtons.")

if obj_weight > 1000:
    print("Its too heavy!")

elif obj_weight < 1000:
    print("Its too light!")    

else:
    print("OBJECT weight is equal to 1000!")



"""Task - 05"""


num_seconds = float(input("Please enter the number of seconds: "))



if num_seconds >= 86400:

    days = num_seconds / 86400

    print(f"There is {days:.1f} days in {num_seconds}.") 

elif num_seconds >= 3600:

    hours = num_seconds / 3600

    print(f"There is {hours:.2f} hours in {num_seconds}.")

elif num_seconds >= 60:
    
    minutes = num_seconds / 60

    print(f"There is {minutes:.1f} minutes in {num_seconds}.")       

else:
    print("Your seconds is smaller than a minutes!")    



"""Task - 06"""    


account_balance = int(input("Please enter your account balance: "))

no_cheques = int(input("Please enter your number of cheques: "))

if account_balance < 15000 and account_balance > 0:
    if no_cheques >= 60:
        service_fee = (4* no_cheques) + 100 + 50

        print(f"Your bank service fee is Rs. {service_fee} because your account balance is smaller than Rs. 15000 number of cheques is {no_cheques}")

    elif no_cheques >= 40 and no_cheques <= 59:
        service_fee = (6 * no_cheques) + 100 + 50

        print(f"Your bank service fee is Rs. {service_fee} because your account balance is smaller than Rs. 15000 number of cheques is {no_cheques}")


    elif no_cheques >= 20 and no_cheques <= 39:
        service_fee = (8 * no_cheques) + 100 + 50

        print(f"Your bank service fee is Rs. {service_fee} because your account balance is smaller than Rs. 15000 number of cheques is {no_cheques}")

    elif no_cheques <= 20:
        service_fee = (10 * no_cheques) + 100 + 50

        print(f"Your bank service fee is Rs. {service_fee} because your account balance is smaller than Rs. 15000 number of cheques is {no_cheques}")

elif account_balance >= 15000:
    if no_cheques >= 60:
        service_fee = (4 * no_cheques) + 50

        print(f"Your bank service fee is Rs. {service_fee} because your account balance is greater than Rs. 15000 number of cheques is {no_cheques}")

    elif no_cheques >= 40 and no_cheques <= 59:
        service_fee = (6 * no_cheques) + 50

        print(f"Your bank service fee is Rs. {service_fee} because your account balance is greater than Rs. 15000 number of cheques is {no_cheques}")


    elif no_cheques >= 20 and no_cheques <= 39:
        service_fee = (8 * no_cheques) + 50

        print(f"Your bank service fee is Rs. {service_fee} because your account balance is greater than Rs. 15000 number of cheques is {no_cheques}")

    elif no_cheques <= 20:
        service_fee = (10 * no_cheques) + 50

        print(f"Your bank service fee is Rs. {service_fee} because your account balance is greater than Rs. 15000 number of cheques is {no_cheques}")


else:
    print("Your account is overdrawn!")




"""Task - 07"""

package_weight = float(input("Please enter the package weight: "))

distance = float(input("Please enter the shipping distance in kilometer: "))


if package_weight < 0 or package_weight > 20 or distance < 10 or distance > 3000:
    
    print("Sorry! we can't provide you a logistic support!")

else:
    if package_weight > 10 and package_weight <= 20:
        
        shipping_charges = (distance/500) * 200

    elif package_weight > 6 and package_weight <= 10:

        shipping_charges = (distance/500) * 150

    elif package_weight > 2 and package_weight <= 6:

        shipping_charges = (distance/500) * 100

    elif package_weight <= 2 and package_weight >= 0:

        shipping_charges = (distance/500) * 50

    print(f"Your shipping charges are Rs. {shipping_charges:.2f} for a package weight of {package_weight} kg over a distance of {distance} km.")


"""Task - 08"""

no_calories = int(input("Please enter the calories in a food: "))
fat_grams = int(input("Please enter the fat grams in a food: "))

calories_from_fat = fat_grams * 9

calories_percentage = (calories_from_fat/no_calories) * 100

if no_calories < 0 or fat_grams < 0 or calories_from_fat > no_calories:

    print("Error: Either the calories or the fat grams were incorrectly entered")
else:
    if calories_percentage < 30:
        print(f"The percentage of calories from fat is {calories_percentage:.2f}%.")
        print("the food is low in fat!")


    else:
        print("the food is high in fat!")
        print(f"The percentage of calories from fat is {calories_percentage:.2f}%.")



"""Task - 09"""

first_salesperson_weekly_gross_sales = int(input("Please enter the first salesperson weekly gross sales: "))

second_salesperson_weekly_gross_sales = int(input("Please enter the second salesperson weekly gross sales: "))

third_salesperson_weekly_gross_sales = int(input("Please enter the third salesperson weekly gross sales: "))

if first_salesperson_weekly_gross_sales < 0 or second_salesperson_weekly_gross_sales < 0  or third_salesperson_weekly_gross_sales < 0:

    print("Invalid sales data!")

else:
    first_salesperson_earnings = 200 + ((9 / 100) * first_salesperson_weekly_gross_sales) 

    second_salesperson_earnings = 200 + ((9 / 100) * second_salesperson_weekly_gross_sales) 

    third_salesperson_earnings = 200 + ((9 / 100) * third_salesperson_weekly_gross_sales) 

    avg_sales = (first_salesperson_earnings +second_salesperson_earnings + third_salesperson_earnings)/3

    if first_salesperson_earnings > second_salesperson_earnings and first_salesperson_earnings > third_salesperson_earnings:

        max_sales = first_salesperson_earnings

    elif second_salesperson_earnings > first_salesperson_earnings and second_salesperson_earnings > third_salesperson_earnings:

        max_sales = second_salesperson_earnings   

    else:
        max_sales = third_salesperson_earnings    

    if first_salesperson_earnings < second_salesperson_earnings and first_salesperson_earnings < third_salesperson_earnings:

        min_sales = first_salesperson_earnings

    elif second_salesperson_earnings < first_salesperson_earnings and second_salesperson_earnings < third_salesperson_earnings:

        min_sales = second_salesperson_earnings

    else:
        min_sales = third_salesperson_earnings    

    print("---Sales Summary---")

    print(f"Average Sales: ${avg_sales:.2f}")   
    print(f"Max sale is: ${max_sales:.2f}")
    print(f"Min sale is: ${min_sales:.2f}")
 

"""Task - 10""" 


acc_num = int(input("Enter your account number: "))
acc_balance = int(input("Enter your account balance: "))
total_all_items_charged = int(input("Enter the total of all items charged by this customer this month: "))
total_all_credits = int(input("Enter the total of all credits applied to this customer's account this month: "))
allowed_credit_limit = int(input("Enter the credit limit: "))


new_balance = (acc_balance + total_all_items_charged) - total_all_credits

if new_balance > allowed_credit_limit:
    print(f"Customer's account number: {acc_num}")
    print(f"Customer's allowed credit limit: {allowed_credit_limit}")
    print(f"Customer's new balance: {new_balance}")
    print("Credit limit exceeded!")

else:
    print("Your credit limit is not exceeded!")



"""Task - 11"""


check_pallindrome = int(input("Please enter the five-digits integer: "))

first_digit = (check_pallindrome // 10000)
second_digit = (check_pallindrome // 1000) % 10
third_digit = (check_pallindrome // 100) % 10
fourth_digit = (check_pallindrome // 10) % 10
fifth_digit = (check_pallindrome % 10)


if first_digit == fifth_digit and second_digit == fourth_digit:
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome.")




"""Task - 12"""


binary_digits = int(input("Please enter the binary digits (0s and 1s only): "))

decimal_value = 0
position = 0

while binary_digits > 0:

    bit = binary_digits % 10
    
    decimal_value += bit * (2 ** position)
    
    binary_digits //= 10
    
    position += 1

print("The decimal equivalent is:", decimal_value)



"""Task - 13"""

PI = 3.14159

while True:

    user_request = input(
        "Please select one of the options:\n"
        "1. Calculate the area of a Circle\n"
        "2. Calculate the area of a Rectangle\n"
        "3. Calculate the area of a Triangle\n"
        "4. Calculate the area of a Cylinder\n"
        "5. Calculate the area of a Trapezoid\n"
        "6. Quit\n"
        "Enter your choice (1-6): "
    )

    if user_request == "1":

        circle_radius = float(input("Enter the radius of the circle: "))
        if circle_radius >= 0:
            area = PI * (circle_radius ** 2)
            print(f"Area of the circle is: {area}")
        else:
            print("Please enter a positive radius.")

    elif user_request == "2":

        rect_length = float(input("Enter the length of the rectangle: "))
        rect_width = float(input("Enter the width of the rectangle: "))
        if rect_length >= 0 and rect_width >= 0:
            rect_area = rect_length * rect_width
            print(f"Area of the rectangle is: {rect_area}")
        else:
            print("Please enter positive values for length and width.")

    elif user_request == "3":

        triangle_base = float(input("Enter the length of the triangle base: "))
        triangle_height = float(input("Enter the height of the triangle: "))
        if triangle_base >= 0 and triangle_height >= 0:
            triangle_area = triangle_base * triangle_height * 0.5
            print(f"Area of the triangle is: {triangle_area}")
        else:
            print("Please enter positive values for base and height.")

    elif user_request == "4":

        cylinder_radius = float(input("Enter the radius of the cylinder: "))
        cylinder_height = float(input("Enter the height of the cylinder: "))
        if cylinder_radius >= 0 and cylinder_height >= 0:
            cylinder_area = (2 * (PI * (cylinder_radius ** 2))) + (cylinder_height * (2 * PI * cylinder_radius))
            print(f"Area of the cylinder is: {cylinder_area}")
        else:
            print("Please enter positive values for radius and height.")

    elif user_request == "5":

        trapezoid_base_a = float(input("Enter base a of the trapezoid: "))
        trapezoid_base_b = float(input("Enter base b of the trapezoid: "))
        trapezoid_height = float(input("Enter the height of the trapezoid: "))
        if trapezoid_base_a >= 0 and trapezoid_base_b >= 0 and trapezoid_height >= 0:
            trapezoid_area = trapezoid_height * ((trapezoid_base_a + trapezoid_base_b) / 2)
            print(f"Area of the trapezoid is: {trapezoid_area}")
        else:
            print("Please enter positive values for bases and height.")

    elif user_request == "6":
        print("Exiting the program.")
        break

    else:
        print("Please select a valid option (1-6).")
