print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You arrive at a two ways magical tunnel going underground. \nThe left side is dark and have the most hunted sounds, \nthe right side is blooming with light and have a herd of what sounds like heavenly angels singing. \nWhich way wounld you go?")
Adventurer_direction = input("Type \"left\" to go left and \"right\" to go right? :")
print(Adventurer_direction)

if Adventurer_direction == "left" or Adventurer_direction == "Left" or Adventurer_direction == "LEFT":
    print("Congratulations! You passed the first level")
else:
    print("Game Over!!")
    print("You fell into the trap of scheming two face demons and you get tortured for eternity")

print("Now you find yourself at a huge enchanted lake, \nwith a glowing island in the middle of the lake. \nYou have two options, to swim or wait for a boat that is magically moving on its own.")
Adventurer_choice = input("Type \"swim\" to swim  or \"wait\" to wait for the enchanted boat :")
if Adventurer_choice == "wait" or Adventurer_choice == "Wait" or Adventurer_choice == "WAIT":
    print("Congratulations! You passed the second level")
else:
    print("Game Over!!")
    print("You get attacked by three legendary, magical and mysterious water creatures from the enchanted lake.")

print("Finally, you have crossed the Enchanted lake and reached a magical castle. \nWhere you are faced with three doors of different colors. \nThe three colors are red, yellow, blue. \nAnd the door you choose determines your final destination. \nWhich door would you choose?")
Adventurer_final_decision = input("Type \"red\", \"yellow\", or \"blue\" to choose a door :")
if Adventurer_final_decision == "red" or Adventurer_final_decision == "Red" or Adventurer_final_decision == "RED":
    print("Game Over!!")
    print("You get melted by a dungeon full of lava.")
elif Adventurer_final_decision == "blue" or Adventurer_final_decision == "Blue" or Adventurer_final_decision == "BLUE":
    print("Game Over!!")
    print("You want in to a dimension full of monsters and get devoured.")
elif Adventurer_final_decision == "yellow" or Adventurer_final_decision == "Yellow" or Adventurer_final_decision == "YELLOW":
    print("Congratulations! You found the treasure. You win!!")