#Brogan Mutarelli
#Dec 5th, 2017
#Raspi's Cave Adventure
#A text based adventure game
def cls():
    print ('\n' * 60)

cls()

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

print ("You walk into a cave and you start to walk in. You get 30 feet in and the cave splits in 2. You can go to the right or to the left.")
cave_choice = input ("Ener L to go left and R to gor right: ")
cave_choice = "no"
while cave_choice not in ["L", "R", "LEFT", "RIGHT"]:
    cave_choice = input ("Ener L to go left and R to go right: ").upper()

if cave_choice in ["L", "LEFT"]:
    print ("You walk into the left tunnel")
    print ("You come across a river and see a boat")
    river-choice = input ("Do you want to walk (W) along the river, ride the boat (B) across the river or swim (S) to the other side of the river: ")



    
else:
    print ("You walk into the right tunnel")
    print ("The tunnel you are walking in suddenly starts to slope downward")
