e1 = 1

print ("\nWelcome to the Ty Gwyn night out adventure!\n\nIf you ever get stuck, just type \'help\' to get a list of instructions, or \'hint\' to get a small hint on the puzzle in front of you.\n\nEnjoy!\n\n - Jack and Tom\n\n|<===========================================>|\n")

showInstructions = ("|<===========================================>|\n\nWelcome to the Ty Gwyn night out adventure\nCommands:\ngo [direction] = (north, south, east, west)\nget [item]\n\nMISSON: Leave in the taxi to go on a famous Ty Gwyn night out in Cardiff.\n\n|<===========================================>|\n")

def Player():
    #Ask the user their name to determine starting point
    print("But before we start, what is your name?\n-->")

def showStatus():
    #print the player's current status
    print("===========================================")
    print("You are in " + rooms[currentRoom]["name"])
    print("Inventory : " + str(inventory))
    if "item" in rooms[currentRoom]:
        print("There is a " + rooms[currentRoom]["item"])
    print("===========================================")

#The player's starting Inventory
inventory = []

#Dictionary of rooms (map of game)
rooms = {
            1 : { "name"    :   "Jack's Room",
                  "east"    :   3 } ,
            2 : { "name"    :   "Tom's Room",
                  "west"    :   3 } ,
            3 : { "name"    :   "the Hall",
                  "east"    :   2,
                  "west"    :   1,
                  "south"   :   4,
                  "north"   :   5} ,
            4 : { "name"    :   "the Kitchen",
                  "north"   :   3,
                  "item"    :   "bottle of vodka"} ,
            5 : { "name"    :   "the Car Park",
                  "south"   :   3},
            6 : { "name"    : "The Great Abyss. You are not welcome to play this game!"}
        }

Player()
playerName=input().lower()

while (e1 == 1):
	if playerName == "jack":
		e1 = e1 - 1
		break
	elif playerName == "help":
		print (showInstructions)
		playerName=input("When you have read the instructions, try typing in your name again! \n-->").lower()
	elif playerName == "tom":
		e1 = e1 - 1
		break
	else: playerName=input("\nSorry, I don't recognise that name! please try again \n-->").lower()

print("\nOh so you are the famous %s! Let's put you in your room!\n\n|<===========================================>|\n\n"	% (playerName))
	
#Define Starting Point
if playerName == "jack":
    currentRoom = 1
elif playerName == "tom":
    currentRoom = 2
else: currentRoom = 6


print ("You are in your room ready to go on a night out.\nYou are sat on your bed and look around your room.\nIn front of you, you can see your phone and wallet on the desk.\nThere is a book shelf with books in and an empty beer bottle.\nYou look towards your left and you can see that the window is closed.\nTo your right is you wardrobe which is closed, and that your sink is empty.\nOn the other side of the wardrobe is the door out to the communal hallway.\n")

action = input("\nWhere would you like to go next?\n-->").lower()

end




#CURRENT FUNCIONAL POINT ---------------------------------------------------------------------#

#Looping logic of game:
while True:
    showStatus()

    #get the player's next move
    #.split() breaks it up into a list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = input(">").lower().split()
    if move[0] == "go":
        #check that the move is legal
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            #there is no door to the next room
        else:
            print("You can't go that way!")
    #if they type 'get' first
    if move[0] == "get" :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            #add the item to the inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + " got!")
            #delete item from room
            del rooms[currentRoom]["item"]
        #otherwise if the item isn't there
        else:
          #tell them they can't have it
            print("Can't get " + move[1] + "!")

    #END SCENARIOS
    if currentRoom == 5 and "bottle" not in inventory:
        print("You cannot leave in the taxi until you are pissed!")
        #VICTORY
    elif currentRoom == 5 and "bottle" in inventory:
        print("You down the bottle of vodka and enter the taxi.")
        print("YOU WIN")
        break
        #GAME OVER
    elif currentRoom == 6 and "bottle" not in inventory:
        print("You cannot go anywhere or do anything but lose.")
        print("Try to have a cooler name next time.")
        print("GAME OVER")
        break
