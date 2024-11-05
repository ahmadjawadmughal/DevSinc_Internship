"""Task 01"""


# Storing initials using double quotes

first_double = "A"

middle_double = "J"

last_double = "M"

# Storing initials using single quotes

first = 'A'

middle = 'J'

last = 'M'

print(f"Storing initials using double quotes: {first_double}{middle_double}{last_double}.")

print(f"Storing initials using single quotes: {first}{middle}{last}.")



"""Task 02"""

age = 10
weight = 65.0

print(f"My age is {age} and weight is {weight} pounds.")


"""Task 03"""

speed = 20 
time = 10

distance = speed * time

print("Distance: ", distance)

"""Task 04"""

force = 172.5 
area = 27.5

pressure =  force / area

print("Pressure: ", pressure)


"""Task 05"""

sales = 680       # Rs. 680 millions

south_punjab_sales_percent = 62/100

south_punjab_this_year_sales = sales * south_punjab_sales_percent

print("Sales predicted for the South Punjab division:")
print(f"Rs. {south_punjab_this_year_sales} Millions")


"""Task 06"""

meal_cost = 4450 

tip_rate = 15 / 100

tax_rate = 6.75 / 100

tax_amount = meal_cost * tax_rate

tip_amount = (meal_cost + tax_amount) * tip_rate

total_bill = meal_cost + tax_amount + tip_amount

print("Meal charge: ",meal_cost)
print("Tax amount: ", tax_amount)
print("Tip amount: ", tip_amount)
print("Total bill", total_bill)


"""Task 07"""

payAmount = 5700

payPeriods = 26

annualPay = payAmount * payPeriods

print(annualPay)


"""Task 08"""

ocean_level_rising = 1.5          # 1.5 mm per year

ocean_level_rising_after_five_year = 5 * 1.5


ocean_level_rising_after_seven_year = 7 * 1.5


ocean_level_rising_after_ten_year = 10 * 1.5


print(f"Ocean level would be rise {ocean_level_rising_after_five_year} mm after 5 years.")
print(f"Ocean level would be rise {ocean_level_rising_after_seven_year} mm after 7 years.")
print(f"Ocean level would be rise {ocean_level_rising_after_ten_year} mm after 10 years.")


"""Task 09"""


one_acre_land = 43_560       #43560 sq. feet 

tract_of_land = 389_767       # 389767 sq. feet


no_of_acre_in_tract_of_land = tract_of_land / one_acre_land

print("no_of_acre_in_the_tract_of_land: ", no_of_acre_in_tract_of_land)


"""Task 10"""

no_of_shares = 600

per_share_price = 21.77     #Rs. 21.77 

commission_rate = 2 / 100

stock_amount_paid_without_commission = no_of_shares * per_share_price

commission_amount = stock_amount_paid_without_commission * commission_rate

total_amount_paid = stock_amount_paid_without_commission + commission_amount


print("stock_amount_paid_without_commission: ", stock_amount_paid_without_commission)
print("commission_amount: ", commission_amount)
print("total_amount_paid: ", total_amount_paid)


"""Task 11"""

surveyed_customers = 12_467     

customers_percent_purchased_one_or_more_per_week =  14 / 100 

percent_customer_love_citrus_flavor = 64 / 100

customers_purchased_one_or_more_per_week =  surveyed_customers * customers_percent_purchased_one_or_more_per_week

customers_prefer_citrus_flavor = customers_purchased_one_or_more_per_week * percent_customer_love_citrus_flavor

print("customers_purchased_one_or_more_per_week: ", customers_purchased_one_or_more_per_week)
print("no_of_customers_prefer_citrus_flavor: ", customers_prefer_citrus_flavor)