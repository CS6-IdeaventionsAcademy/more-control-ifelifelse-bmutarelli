#Brogan Mutarelli
#Behind the door game show
#CS

import random
import time
door1 = "Iphone X"
door2 = "Egostia"
door3 = "Freshly Used Toilet (Unflushed)"
door4 = "$1000"

def cls():
    print ('\n' * 60)

cls()

door = random.randint (1,4)

play_again = "yes"

again = ["yes", "Yes", "Y", "y", "yep", "Yep"]

answers = ["1", "2", "3", "4"]

print ("You are on the last question!!!!")
time.sleep(1)
print ("You have made it to the last stage!!!!")

while play_again in again:

    user_door = input ("Pick your door (1-4): ")
    
    while user_door not in answers:
        print ("THAT IS INVALID")
        user_door = input ("Pick your door (1-4): ")
        

    if user_door == "1":
        print ("You got a brand new " + door1)
        time.sleep (1)
    elif user_door == "2":
        print ("You got a brand new " + door2)
        time.sleep (1)
    elif user_door == "3":
        print ("You got a brand new " + door3)
        time.sleep (1)
    elif user_door == "4":
        print ("You got a brand new " + door4)
        time.sleep (1)

    play_again = input ("Do you want to play again (Y/N)?  ")

print ("Thank you for playing ","Behind the Door",".")


