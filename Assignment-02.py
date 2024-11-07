"""Q - 01"""

# Correct Answer is: (A) 


"""Q - 02"""

x = 20


if x == 20:
    y = 0

price = 600

if price > 500:    
    discountRate = 0.2

hours = 45
payRate = 0

if hours > 40:
    payRate *= 1.5



"""Q - 03"""

"""
if interestRate > 0.7:
    print("This account earns a $10 bonus.")
    balance += 10.0
"""


"""Q - 04"""

sales = 60000

if sales > 50000:
    commissionRate = 0.25
    bonus = 250


"""Q - 05"""



if sales >= 50000:
    commissionRate = 0.20

else:
    commissionRate = 0.10



"""Q - 06"""

number = int(input("Please enter the number: "))

if number > 0:
    print("zero")

    if number > 10:
        print("Ten")

        if number > 20:
            print("Twenty")

# if user enters 5 :  zero would display on the screen
# if user enters 15 :  both Zero and Ten would display on the screen
# if user enters 30 : Zero, Ten, and Twenty all of them would display on the screen
# if user enters -1 : nothing would be display on the screen             


"""Q - 07"""

funny = 7
serious = 15

funny = serious % 2

if funny != 1:

    funny = 0
    serious = 0

elif funny == 2:

    funny = 10
    serious = 10

else: 
    funny = 1
    serious = 1


print(funny," ," ,serious)    # both of them display as a 1 , 1



"""Q - 08"""

numCoupons = 0

numBooks = int(input("How many books are being purchased? "))


if numBooks < 1:
    numCoupons = 0

elif numBooks < 3:
    numCoupons = 1

elif numBooks < 5:
    numCoupons = 2

else:
    numCoupons = 3

print(f"The number of coupons to given is : {numCoupons}")    

# user purchased 1 book: One coupon customer get
# user purchased 3 books: TWO coupons customer get
# user purchased 4 books: TWO coupons customer get
# user purchased 5 books: Three coupons customer get
# user purchased 7 books: Three coupons customer get
# user purchased 10 books: Three coupons customer get


"""Q - 09"""

print('"Bill" == "BILL":', "Bill" == "BILL") # false
print('"Bill" < "BILL":', "Bill" < "BILL")   # false
print('"Bill" < "Bob":', "Bill" < "Bob")     #True
print('"189" > "23":', "189" > "23")         #false
print('"189" > "Bill":', "189" > "Bill")     #false
print('"Mary" < "MaryEllen":', "Mary" < "MaryEllen") #True
print('"MaryEllen" < "Mary Ellen":', "MaryEllen" < "Mary Ellen") #false


"""Q - 10"""

"""
A) z = 1 if x > y else 20

B) population = base * 10 if temp > 45 else base * 2

C) wages = wages * 1.5 if hours > 40 else wages * 1

D) result = "The result is positive" if result >= 0 else "The result is negative"

"""




"""Q - 11"""
"""
A) 

if k > 90:
    j = 57
else:
    j = 12

B)

if x >= 10:
    factor = y * 22

else: 
    factor = y * 35


C)

if count == 1:
    total += sales

else:
    total += count * sales    


D) 

if (num % 2 == 0):
    print("Even")
else:
    print("Odd")
"""



"""Q - 12"""

UPPER = 8
LOWER = 2

num1 = num2 = num3 = 12

num4 = 3

num1 = UPPER if num3 < num4 else LOWER
num2 = num3 if num4 > UPPER else LOWER

print(num1, "  " ,num2) # answer would be 2  2



"""Q - 13"""

temperature = int(input("Please enter the temperature: "))

if temperature >= -50 and temperature <= 150:
    print("The number is valid")

else:
    print("The number is invalid")


"""Q - 14"""


# 1 - C
# 2 - A
# 3 - B





"""Q - 15 (error detection)"""

"""
// This program averages 3 test scores.
// It uses the variable perfectScore as a flag.
#include <iostream>
using namespace std;

int main()
{
    cout << "Enter your 3 test scores and I will ";
    cout << "average them:\n";
    int score1, score2, score3;
    cin >> score1 >> score2 >> score3;

    double average;
    average = (score1 + score2 + score3) / 3.0;

    bool perfectScore = false; // Declare the flag variable
    if (average == 100) // Remove the incorrect semicolon here
        perfectScore = true;  // Set the flag variable

    cout << "Your average is " << average << endl;

    if (perfectScore)
    {
        cout << "Congratulations!\n";
        cout << "That's a perfect score.\n";
        cout << "You deserve a pat on the back!\n";
    }
    
    return 0;
}
"""



"""Q - 16(error detection)"""


"""
// This program divides a user-supplied number by another
// user-supplied number. It checks for division by zero.
#include <iostream>
using namespace std;

int main()
{
    double num1, num2, quotient;

    cout << "Enter a number: ";
    cin >> num1;
    cout << "Enter another number: ";
    cin >> num2;  // Corrected error: replaced `cout >> num2` with `cin >> num2`

    if (num2 == 0)
    {
        cout << "Division by zero is not possible.\n";
        cout << "Please run the program again ";
        cout << "and enter a number besides zero.\n";
    }
    else
    {
        quotient = num1 / num2;
        cout << "The quotient of " << num1 <<
                " divided by " << num2 << " is ";
        cout << quotient << endl;
    }
    return 0;
}


"""



"""Q - 17"""

"""
if count >= 0 and count <= 100: 

"""

"""Q - 18"""

"""

if count < 0 or count > 100:

"""