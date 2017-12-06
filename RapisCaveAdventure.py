#Brogan Mutarelli
#Dec 5th, 2017
#Raspi's Cave Adventure
#A text based adventure game
import time

def cls():
    print ('\n' * 60)

cls()

def wrong():
    print ("Please enter a diffrent answer")
    time.sleep (1)

def left_cave():
    print ("You walk into the left tunnel")
    print ("You come across a river and see a boat")
    river_choice = input ("Do you want to walk (W) along the river, ride the boat (B) across the river or swim (S) to the other side of the river: ").upper()
    while river_choice not in ["S", "SWIM", "B", "BOAT", "W", "WALK"]:
        wrong()
        river_choice = input ("Do you want to walk (W) along the river, ride the boat (B) across the river or swim (S) to the other side of the river: ").upper()
    return river_choice

def right_cave():
    print ("You walk into the right tunnel")
    print ("You see a hole in the ground with a rope going down and a torch off in the distance")
    rope_choice = input ("Do you want to go down the rope (R) or get the torch and keep walking (T): ").upper()
    while river_choice not in ["T", "TORCH", "R", "ROPE"]:
        wrong()
        rope_choice = input ("Do you want to walk (W) along the river, ride the boat (B) across the river or swim (S) to the other side of the river: ").upper()
    return rope_choice



print ("<oo>" * 20)
print ('\n' * 2)
print("""
██████╗  █████╗ ███████╗██████╗ ██╗███████╗                                  
██╔══██╗██╔══██╗██╔════╝██╔══██╗██║██╔════╝                                  
██████╔╝███████║███████╗██████╔╝██║███████╗                                  
██╔══██╗██╔══██║╚════██║██╔═══╝ ██║╚════██║                                  
██║  ██║██║  ██║███████║██║     ██║███████║                                  
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝                                  
                                                                             
 ██████╗ █████╗ ██╗   ██╗███████╗                                            
██╔════╝██╔══██╗██║   ██║██╔════╝                                            
██║     ███████║██║   ██║█████╗                                              
██║     ██╔══██║╚██╗ ██╔╝██╔══╝                                              
╚██████╗██║  ██║ ╚████╔╝ ███████╗                                            
 ╚═════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝                                            
                                                                             
 █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  
██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  
██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║███████╗
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                             
""")

#First choice

print ("""As you are collecting firewood you see a cave. You want to go in the cave but in might be dangerous, so you turn away.
As you turn away you suddenly remember an old folktale that was told when the town came together, once a year, to eat. It was called Ramenday.
The story goes there is a cave high up in the mountains and in that cave there a glorious treasures. You decide to go into the cave to try and find the riches.
You know you could die but if you did succeed your family could buy anything thay want and bathe in gold, diamonds, and jewels.
You walk into a cave. You get 30 feet in and the cave splits in 2. You can go to the right or to the left.""")

time.sleep (4)
print ('\n' * 2)
cave_choice = "CS is the best"
cave_choice = "no"
while cave_choice not in ["L", "R", "LEFT", "RIGHT"]:
    cave_choice = input ("Ener L to go left and R to go right: ").upper()

if cave_choice in ["L", "LEFT"]:
    choice = left_cave()
    
    if choice == "B" or choice == "BOAT":
        #Boat choice
        print ("You climb into a wooden boat and push off")
        time.sleep (1)
        print ("""You have been rowing along and just now you have noticed there is a leak in your boat. You start moving around and making a lot of noise, disturbing the bats.
One of them swoops down and bites you with its mouth witch happens to be full of rabies germs""")
    elif choice == "S" or choice == "SWIM":
        #Swim
        print ("You take a deep breath and jump into the freezing cold river")
        time.sleep (1)
        print ("You foot gets stuck on caveweed but you are able to escape")
    else:
        #Walk
        print ("You walk along the narrow edge of the river")
        time.sleep (1)
        print ("As you are walking you trip, fall, and skewer yourself on a stalagmite")
else: # Right Cave
    choice = right_cave()
        if choice == "T" or choice == "TORCH":
        #Torch choice
        print ("You climb into a wooden boat and push off")
        time.sleep (1)
        print ("""You have been rowing along and just now you have noticed there is a leak in your boat. You start moving around and making a lot of noise, disturbing the bats.
One of them swoops down and bites you with its mouth witch happens to be full of rabies germs""")
    elif choice == "R" or choice == "ROPE":
        #Rope
        print ("You climb down the rope")
        

    
