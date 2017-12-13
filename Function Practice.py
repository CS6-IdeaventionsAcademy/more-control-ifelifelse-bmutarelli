#Brogan M
#Dec 12, 17'
#Function Practice

import time
import math
import random
##def cheese():
##    """Makes a screen full of I Like Cheeses"""
##    print("I Like Cheese" * 100)
##
##
##
##def temp_C(temp_F):
##    """Converts a tempature in fahrenhight to Celcius"""
##    #(F - 32) * 5/2
##    answer = (temp_F - 32) * (5/9)
##    return answer
##
##def volume_sphere(radius):
##    """Calculate the volume of a sphere"""
##    #4/3 pi r cubed
##    volume = (4/3)*math.pi*r**3
##    print ("Calculating")
##    time.sleep (1)
##    return volume

def ran_num(UE, LE):
    r_n = random.randint(LE, UE)
    return r_n
#cheese()

##t_in_F = input ("Please enter a tempature in Fahrenheit: ")
##t_in_F = float(t_in_F)
##t_in_C = temp_C(t_in_F)
##print ("Celsuis: ", t_in_C)
##
##
##r = input ("Please enter a radius of a sphere: ")
##r = float(r)
##v_sphere = volume_sphere(r)
##print ("Sphere Volume: ", v_sphere)


LE = input ("What is your lowest number (Whole Number): ")
UE = input ("What is your highest number (Whole Number): ")
UE = int(UE)
LE = int(LE)
ran_num(UE, LE)
print (r_n)
