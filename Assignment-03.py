import time
import os

keypad = {
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z']
}

delay = 2.5
last_num = 0
press_count = 0
text = []

current_time = time.time()



#for first press

user_input = input("enter the number: ")

if user_input.isdigit() and user_input in keypad:
    end_time = time.time()

    if user_input == last_num and end_time - current_time <= delay: 

        press_count += 1

    else:
        press_count = 1    

    letter = keypad[user_input][(press_count - 1) % len(keypad[user_input])]

    if press_count > 1 and len(text) > 0 and text[-1] != letter:    

        text[-1] = letter  

    else:
        press_count == 1
        text.append(letter)    


    last_num = user_input

    end_time = current_time

    os.system("cls")
    print(f"My text: {" ".join(text)}")

else:

    print("Please enter a valid digit (2 - 9)!")        



# second press

user_input = input("enter the number: ")

if user_input.isdigit() and user_input in keypad:
    end_time = time.time()

    if user_input == last_num and end_time - current_time <= delay: 

        press_count += 1

    else:
        press_count = 1    

    letter = keypad[user_input][(press_count - 1) % len(keypad[user_input])]

    if press_count > 1 and len(text) > 0 and text[-1] != letter:    

        text[-1] = letter  

    else:
        press_count == 1
        text.append(letter)    


    last_num = user_input

    end_time = current_time

    os.system("cls")
    print(f"My text: {" ".join(text)}")

else:

    print("Please enter a valid digit (2 - 9)!")        



# third press

user_input = input("enter the number: ")

if user_input.isdigit() and user_input in keypad:
    end_time = time.time()

    if user_input == last_num and end_time - current_time <= delay: 

        press_count += 1

    else:
        press_count = 1    

    letter = keypad[user_input][(press_count - 1) % len(keypad[user_input])]

    if press_count > 1 and len(text) > 0 and text[-1] != letter:    

        text[-1] = letter  

    else:
        press_count == 1
        text.append(letter)    


    last_num = user_input

    end_time = current_time

    os.system("cls")
    print(f"My text: {" ".join(text)}")

else:

    print("Please enter a valid digit (2 - 9)!")        



# fourth press

user_input = input("enter the number: ")

if user_input.isdigit() and user_input in keypad:
    end_time = time.time()

    if user_input == last_num and end_time - current_time <= delay: 

        press_count += 1

    else:
        press_count = 1    

    letter = keypad[user_input][(press_count - 1) % len(keypad[user_input])]

    if press_count > 1 and len(text) > 0 and text[-1] != letter:    

        text[-1] = letter  

    else:
        press_count == 1
        text.append(letter)    


    last_num = user_input

    end_time = current_time

    os.system("cls")
    print(f"My text: {" ".join(text)}")

else:

    print("Please enter a valid digit (2 - 9)!")        



# fifth press

user_input = input("enter the number: ")

if user_input.isdigit() and user_input in keypad:
    end_time = time.time()

    if user_input == last_num and end_time - current_time <= delay: 

        press_count += 1

    else:
        press_count = 1    

    letter = keypad[user_input][(press_count - 1) % len(keypad[user_input])]

    if press_count > 1 and len(text) > 0 and text[-1] != letter:    

        text[-1] = letter  

    else:
        press_count == 1
        text.append(letter)    


    last_num = user_input

    end_time = current_time

    os.system("cls")
    print(f"My text: {" ".join(text)}")

else:

    print("Please enter a valid digit (2 - 9)!")        



# sixth press

user_input = input("enter the number: ")

if user_input.isdigit() and user_input in keypad:
    end_time = time.time()

    if user_input == last_num and end_time - current_time <= delay: 

        press_count += 1

    else:
        press_count = 1    

    letter = keypad[user_input][(press_count - 1) % len(keypad[user_input])]

    if press_count > 1 and len(text) > 0 and text[-1] != letter:    

        text[-1] = letter  

    else:
        press_count == 1
        text.append(letter)    


    last_num = user_input

    end_time = current_time

    os.system("cls")
    print(f"My text: {" ".join(text)}")

else:

    print("Please enter a valid digit (2 - 9)!")        





# seventh press

user_input = input("enter the number: ")

if user_input.isdigit() and user_input in keypad:
    end_time = time.time()

    if user_input == last_num and end_time - current_time <= delay: 

        press_count += 1

    else:
        press_count = 1    

    letter = keypad[user_input][(press_count - 1) % len(keypad[user_input])]

    if press_count > 1 and len(text) > 0 and text[-1] != letter:    

        text[-1] = letter  

    else:
        press_count == 1
        text.append(letter)    


    last_num = user_input

    end_time = current_time

    os.system("cls")
    print(f"My text: {" ".join(text)}")

else:

    print("Please enter a valid digit (2 - 9)!")        



# eight-th press


user_input = input("enter the number: ")

if user_input.isdigit() and user_input in keypad:
    end_time = time.time()

    if user_input == last_num and end_time - current_time <= delay: 

        press_count += 1

    else:
        press_count = 1    

    letter = keypad[user_input][(press_count - 1) % len(keypad[user_input])]

    if press_count > 1 and len(text) > 0 and text[-1] != letter:    

        text[-1] = letter  

    else:
        press_count == 1
        text.append(letter)    


    last_num = user_input

    end_time = current_time

    os.system("cls")
    print(f"My text: {" ".join(text)}")

else:

    print("Please enter a valid digit (2 - 9)!")        



# ninth press

user_input = input("enter the number: ")

if user_input.isdigit() and user_input in keypad:
    end_time = time.time()

    if user_input == last_num and end_time - current_time <= delay: 

        press_count += 1

    else:
        press_count = 1    

    letter = keypad[user_input][(press_count - 1) % len(keypad[user_input])]

    if press_count > 1 and len(text) > 0 and text[-1] != letter:    

        text[-1] = letter  

    else:
        press_count == 1
        text.append(letter)    


    last_num = user_input

    end_time = current_time

    os.system("cls")
    print(f"My text: {" ".join(text)}")

else:

    print("Please enter a valid digit (2 - 9)!")        

