"""Task - 01"""

import math

# Initialize variables
value1 = float(input("Enter the number: "))

# Perform calculations
value2 = 2 * math.pow(value1, 2.0)
value3 = 3 + value2 / 2 - 1

# Output result
print(value3)

# if user enter "2", then output would be: 6.0
# if user enter "5", then output would be: 27.0
# if user enter "4.3", then output would be: 20.49
# if user enter "6", then output would be: 38.0


"""Task - 02"""

# 1 - input from users regarding amount of credit got and the amount of credit used

# 2 - find  the available credit using formula : available credit = maximum credit - credit used

# 3 - display the available/ remaining credit

customers_credit_amount =  int(input("Enter your maximum credit amount: "))

credit_used = int(input("Enter the amount of credit you used: "))

remaining_credit = customers_credit_amount - credit_used

print("Remaining credit:", remaining_credit)


"""Task - 03"""

# 1 - take an input from users regardig the golfer's score for three games of golf

# 2 - apply formula of  an average for getting an average of among three games 

# 3 - display the average of three scores

game1_score = int(input("Enter the golfer's score of 1st game: "))

game2_score = int(input("Enter the golfer's score of 2nd game: "))

game3_score = int(input("Enter the golfer's score of 3rd game: "))


average = (game1_score + game2_score + game3_score)/3

print("The average score for the three games is:", average)


"""Task - 04"""

test = 32767


print(test)

test += 1

print("After adding one to test: ", test)

test -= 1

print("After subtracting one from test: ", test)


"""Task 05"""

import math

angle1 = float(input("Enter the value of angle1 in radian: "))

angle2 = float(input("Enter the value of angle2 in radian: "))


x = math.sin(angle1) + math.cos(angle2)

print("The result of sin(angle1) + cos(angle2) is:", x)


"""Task - 06"""

a = 120

y = 1/math.sin(a)

print("The result of cosecant of angle a:", y)



"""Task - 07"""


amount = int(input("Enter the amount: "))

note_500 = 0
note_100 = 0
note_50 = 0
note_20 = 0
note_10 = 0
note_5 = 0
note_1 = 0


if amount >= 500:
    note_500 = amount // 500
    amount = amount % 500
    
if amount >= 100:
    note_100 = amount // 100
    amount = amount % 100

if amount >= 50:
    note_50 = amount // 50
    amount = amount % 50

if amount >= 20:
    note_20 = amount // 20
    amount = amount % 20

if amount >= 10:
    note_10 = amount // 10
    amount = amount % 10

if amount >= 5:
    note_5 = amount // 5
    amount = amount % 5

if amount >= 1:
    note_1 = amount // 1
    amount = amount % 1


print("500:", note_500)
print("100:", note_100)
print("50:", note_50)
print("20:", note_20)
print("10:", note_10)
print("5:", note_5)
print("1:", note_1)


"""Task - 08"""

classA_cost = 2000

classB_cost = 1000

classC_cost = 500

ticket_sold_classA = int(input("Enter the tickets sold of class A: ")) 

ticket_sold_classB = int(input("Enter the tickets sold of class B: "))

ticket_sold_classC = int(input("Enter the tickets sold of class C: ")) 



if ticket_sold_classA < 0:
    print("Error: Number of tickets sold for Class A cannot be negative.")
if ticket_sold_classB < 0:
    print("Error: Number of tickets sold for Class B cannot be negative.")
if ticket_sold_classC < 0:
    print("Error: Number of tickets sold for Class C cannot be negative.")
else:
    
    income_generated = (ticket_sold_classA * classA_cost) + \
                       (ticket_sold_classB * classB_cost) + \
                       (ticket_sold_classC * classC_cost)

    print("Total income generated from the sale of tickets: ", income_generated)


"""Task - 09"""

first_month = input("Enter the first month: ")
amount_of_rain_first = float(input(f"Please enter the amount of rain of {first_month} in mm: "))

second_month = input("Enter the second month: ")
amount_of_rain_second = float(input(f"Please enter the amount of rain of {second_month} in mm: "))

third_month = input("Enter the third month: ")
amount_of_rain_third = float(input(f"Please enter the amount of rain of {third_month} in mm: "))

calculate_rainfall = (amount_of_rain_first + amount_of_rain_second + amount_of_rain_third) / 3 

print(f"The average rain for {first_month}, {second_month} & {third_month} is {calculate_rainfall:.2f} millimeter.")


"""Task - 10"""

movie_name = input("Please enter the movie name: ")
adult_tickets_sold = int(input("Enter the number of adult tickets sold: "))
child_tickets_sold = int(input("Enter the number of child tickets sold: "))
adults_above_60 = int(input("Enter the number of adults above 60: "))

adult_ticket_price = 500
child_ticket_price = 250
adult_discount = 10 / 100  # 10% discount

adult_revenue = adult_tickets_sold * adult_ticket_price
adult_discount_amount = adults_above_60 * adult_ticket_price * adult_discount
adult_revenue_after_discount = adult_revenue - adult_discount_amount

child_revenue = child_tickets_sold * child_ticket_price

gross_box_office_profit = adult_revenue_after_discount + child_revenue

theater_profit = gross_box_office_profit * 0.20

distributor_payment = gross_box_office_profit * 0.80


print("\n--- Box Office Report ---")
print(f"Movie Name: {movie_name}")
print(f"Adult Tickets Sold: {adult_tickets_sold}")
print(f"Child Tickets Sold: {child_tickets_sold}")
print(f"Adults Above 60: {adults_above_60}")
print(f"Gross Box Office Profit: Rs. {gross_box_office_profit}")
print(f"Net Box Office Profit (Theater's Profit): Rs. {theater_profit}")
print(f"Amount Paid to Distributor: Rs. {distributor_payment}")



"""Task - 11"""

cookie = int(input("Please enter how many cookies you ate: "))

calories = 300 / (40/10)
total_calories_consumed = cookie * calories #75 calories per cookie

print("Total calories consumed: ",total_calories_consumed)


"""Task - 12"""

actual_value_property = int(input("Enter the actual value of the piece of property: "))

current_tax_rate = float(input("Please enter the current tax rate: "))

exemption = 5000

tax_applicable_amount = actual_value_property - exemption

each_100_USD = tax_applicable_amount / 100

annual_property_tax = current_tax_rate * each_100_USD

quarterly_tax = annual_property_tax/4

print(f"Annual property tax: ${annual_property_tax:.2f}")
print(f"Quarterly property tax: ${quarterly_tax:.2f}")


"""Task - 13"""

principal = int(input("Enter your principal amount: "))

interest_rate = int(input("Enter the interest rate: ")) / 100

times_of_interest_compounded = int(input("Enter the interest compounded times: "))

amount = principal * ((1 + interest_rate/times_of_interest_compounded)**times_of_interest_compounded)

interest = amount - principal

print("---Report---")
print(f"Interest Rate: {interest_rate * 100:.2f} %")
print("Time Compounded: ", times_of_interest_compounded)
print(f"Principal:  Rs. {principal}")
print(f"Interest: Rs. {interest:.2f}")
print(f"Amounts in Savings:  Rs. {amount:.2f}")


"""Task - 14"""

number_of_payments = int(input("Enter the number of payments: "))
amount_of_loan = int(input("Please enter the amount of loan: "))

monthly_interest_rate = int(input("Enter the monthly interest rate: ")) / 100

monthly_payment = monthly_interest_rate * ((1 + monthly_interest_rate)**number_of_payments)/(((1 + monthly_interest_rate)**number_of_payments) -1) * amount_of_loan

amount_paid_back = number_of_payments * monthly_payment

interest_paid = amount_paid_back - amount_of_loan

print("--Report--")
print(f"Loan Amount: Rs. {amount_of_loan}")
print(f"Monthly Interest Rate: {monthly_interest_rate * 100:.2f}%")
print(f"Number of Payments Rs. {number_of_payments}")
print(f"Monthly Payments: Rs. {monthly_payment:.2f}")
print(f"Amount Paid Back: Rs. {amount_paid_back:.2f}")
print(f"Interest Paid: Rs. {interest_paid:.2f}")


"""Task - 15"""

import math

diameter_of_pizza = float(input("Enter the diameter of a pizza in inches: "))

radius_of_pizza = diameter_of_pizza / 2

area_of_pizza = math.pi * radius_of_pizza * radius_of_pizza

number_of_slices = area_of_pizza / 14.125

print(f"Should {number_of_slices:.1f} number of slices for {diameter_of_pizza} inches pizza!")


"""Task - 16"""

number_of_people = int(input("Please enter the number of people who'll attend the party: "))

pizza_diameter = float(input("Enter the diameter of the pizza in inches: "))

pizza_radius = pizza_diameter / 2

pizza_area = math.pi * pizza_radius * pizza_radius

pizza_slices = pizza_area / 14.125

slices_needed = number_of_people * 4

pizzas_needed = math.ceil(slices_needed / pizza_slices) #ceil is used for round up 

print(f"You should purchase {pizzas_needed} pizzas for {number_of_people} people.")




"""Task - 17"""

no_shares = 1000
purchase_share_price = 32.87

selling_share_price = 33.92

amount_paid = no_shares * purchase_share_price

commission_paid = (2/100) * amount_paid

stock_sold_amount = no_shares * selling_share_price

sold_commission_paid = (2/100) * stock_sold_amount

profit = (stock_sold_amount - amount_paid) - (sold_commission_paid + commission_paid)

print(f"Amount of money Kathryn paid for the stock: Rs. {amount_paid:.2f}")
print(f"The amount of commission she paid her broker when buying the stock: Rs. {commission_paid:.2f}")
print(f"The amount that Kathryn sold the stock for: Rs. {stock_sold_amount:.2f}")
print(f"The amount of commission Kathryn paid her broker when selling the stock: Rs. {sold_commission_paid:.2f}")
print(f"The amount of profit she made after selling her stocks: Rs. {profit:.2f}")

