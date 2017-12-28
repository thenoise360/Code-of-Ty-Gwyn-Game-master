#HEADER - Defining functions

import random

showInstructions = ("|<===========================================>|\n\nWelcome to the Ty Gwyn night out adventure\nCommands:\n Type \"Go To\" and one of the objects in the room = (e.g. desk, wardrobe, bed, sink, shelf, door)\nget [item]\n\nMISSON: Leave in the taxi to go on a famous Ty Gwyn night out in Cardiff.\n\n|<===========================================>|\n")

# COMPLETE STATUS BLOCK

deskStatus = "incomplete"
deskItemLocation = random.randint(1,4)
print (deskItemLocation)

#STARTING BLOCK

def bedStart(deskStatus):
	print ("You are in your room ready to go on a night out.\nYou are sat on your bed and look around your room.\nIn front of you, you can see your desk. It has 2 draws.\nThere is a book shelf with books in and an empty beer bottle.\nYou look towards your left and you can see that the window is closed.\nTo your right is you wardrobe which is closed, and that your sink is empty.\nOn the other side of the wardrobe is the door out to the communal hallway.\n")
	action = input("\nWhere would you like to go next?\n-->").lower()
	
	#This refers to "Exit Bed" = eb. I will use this format for all of the exit codes (as its a little easier to use)

	eb = 1
	while (eb ==1 ):
		if action == "go to desk":
			desk(action, deskStatus,deskItemLocation)
			break
		elif action == "go to bed":
			bed(action, deskStatus,deskItemLocation)
			break
		elif action == "go to start":
			bedStart(action, deskStatus,deskItemLocation)
			break
		elif action == "go to sink":
			sink(action, deskStatus,deskItemLocation)
			break
		elif action == "go to shelf":
			shelf(action, deskStatus,deskItemLocation)
			break
		elif action == "go to wardrobe":
			wardrobe(action, deskStatus,deskItemLocation)
			break
		elif action == "go to door":
			door(action, deskStatus,deskItemLocation)
			break
		elif action == "help":
			print (showInstructions)
			action = input("When you have read the instructions, keep looking! \n-->").lower()
		elif action == "hint":
			print ("Here you want to pick one of the locations listed in the original dialogue.\nYou can see it here:\n\nYou are in your room ready to go on a night out.\nYou are sat on your bed and look around your room.\nIn front of you, you can see your desk. It has 2 draws.\nThere is a book shelf with books in and an empty beer bottle.\nYou look towards your left and you can see that the window is closed.\nTo your right is you wardrobe which is closed, and that your sink is empty.\nOn the other side of the wardrobe is the door out to the communal hallway.\n")
			action = input("When you have decided where to go, type below and hit [enter]\n-->").lower()
		else: action = input("That isn\'t a location in the room, try again!\n-->").lower()

#DESK BLOCK

def desk(action, deskStatus, deskItemLocation):
	deskStatus = deskStatus
	action = action
	if deskStatus == "complete":
		print ("It looks like you already have the items you need from this area.\ntry looking in another area.")
		deskNest1(action, deskStatus,deskItemLocation)
	
	else :
		print ("You are standing at the desk. On the desk you can see your wallet.\nYou remember leaving your phone here but it doesn't appear to be on the surface top.\nIt must be in the area but you'll have to look.")
		deskNest2(action, deskStatus,deskItemLocation)

def deskNest1(action, deskStatus,deskItemLocation):
	action = input("\nWhere would you like to go to next?\n-->").lower()
	edEndComplete = 1
	while (edEndComplete == 1):
		if action == "help":
			print (showInstructions)
			action = input("When you have read the instructions, keep looking! \n-->").lower()
		elif action == "go back":
			bedStart(action, deskStatus,deskItemLocation)
			break
		elif action == "go to desk":	
			desk(action, deskStatus,deskItemLocation)
			break
		elif action == "go to bed":
			bed(action, deskStatus,deskItemLocation)
			break
		elif action == "go to start":
			bedStart(action, deskStatus,deskItemLocation)
			break
		elif action == "go to sink":
			sink(action, deskStatus,deskItemLocation)
			break
		elif action == "go to shelf":
			shelf(action, deskStatus,deskItemLocation)
			break
		elif action == "go to wardrobe":
			wardrobe(action, deskStatus,deskItemLocation)
			break
		elif action == "go to door":
			door(action, deskStatus,deskItemLocation)
			break
		else: action=input("That isn't a location in this room. Type \'help\' if you get stuck! \n-->").lower()

def deskNest2(action, deskStatus,deskItemLocation):
	action = input("\nWhere would you like to search for your phone?\n-->").lower()
		#This refers to "Exit Desk" = ed. I will use this format for all of the exit codes (as its a little easier to use)
	ed = 1
	while (ed == 1):
		if action == "top drawer":
			if deskItemLocation == 1:
				ed = ed - 1
				print ("You found your phone in the top drawer.\nIt is added to your inventory\n\n|<===========================================>|\n")
				deskStatus = "complete"
				desk(action, deskStatus,deskItemLocation)
			else:
				action = input("You look into the top drawer and it appears empty.\nYou will need to continue searching!\n-->").lower()
		elif action == "bottom drawer":
			if deskItemLocation == 2:
				ed = ed - 1
				print ("You found your phone in the bottom drawer.\nIt is added to your inventory\n\n|<===========================================>|\n")
				deskStatus = "complete"
				desk(action, deskStatus,deskItemLocation)
			else:
				action = input("You look into the bottom drawer and it appears empty.\nYou will need to continue searching!\n-->").lower()
		elif action == "under the desk":
			if deskItemLocation == 3:
				ed = ed - 1
				print ("It appears your phone must have fallen on the floor.\nIt is added to your 	inventory\n\n|<===========================================>|\n")
				deskStatus = "complete"
				desk(action, deskStatus,deskItemLocation)		
				break			
			else:
				action = input("You look under the desk and there is nothing there.\nYou will need to continue searching!\n-->").lower()
		elif action == "behind the desk":
			if deskItemLocation == 4:
				ed = ed - 1
				print ("It appears your phone must have fallen behind the desk.\nIt is added to your inventory\n\n|<===========================================>|\n")
				deskStatus = "complete"
				desk(action, deskStatus,deskItemLocation)		
				break
			else:
				action = input("You look behind the desk and don\'t see your phone.\nYou will need to continue searching!\n-->").lower()
		elif action == "help":
			print (showInstructions)
			action = input("When you have read the instructions, keep looking! \n-->").lower()
		elif action == "hint":
			print ("Here you will need to look under the desk, behind the desk, and in the top and bottom drawer to find what you are looking for.")
			action	= input("When you are ready to keep looking, try typing in one of the instructions shown! \n-->").lower()
		elif action == "go back":
			bedStart(action, deskStatus,deskItemLocation)
			break
		elif action == "go to desk":
			desk(action, deskStatus,deskItemLocation)
			break
		elif action == "go to bed":
			bed(action, deskStatus,deskItemLocation)
			break
		elif action == "go to start":
			bedStart(action, deskStatus,deskItemLocation)
			break	 
		elif action == "go to sink":
			sink(action, deskStatus,deskItemLocation)
			break
		elif action == "go to shelf":
			shelf(action, deskStatus,deskItemLocation)
			break
		elif action == "go to wardrobe":
			wardrobe(action, deskStatus,deskItemLocation)
			break
		elif action == "go to door":
			door(action, deskStatus,deskItemLocation)
			break
		else: action=input("It doesn't seem like you are looking in the right places, something else, or type \'hint\' if you get stuck! \n-->").lower()

#BED BLOCK

def bed(action, deskStatus,deskItemLocation):
	print ("Bed")

#SINK BLOCK

def sink(action, deskStatus,deskItemLocation):
	print ("Sink")

#SHELF BLOCK

def shelf(action, deskStatus,deskItemLocation):
	print ("Shelf")

#WARDROBE BLOCK

def wardrobe(action, deskStatus,deskItemLocation):
	print ("Wardrobe")

#DOOR BLOCK

def door(action, deskStatus,deskItemLocation):
	print ("Door")
				
		
#End of Header ---------------------------------------------------------------------------->

e1 = 1

print ("\nWelcome to the Ty Gwyn night out adventure!\n\nIf you ever get stuck, just type \'help\' to get a list of instructions, or \'hint\' to get a small hint on the puzzle in front of you.\n\nEnjoy!\n\n - Jack and Tom\n\n|<===========================================>|\n")

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
			1 : { "name"	:	 "Jack's Room",
					"east"	:	 3 } ,
			2 : { "name"	:	 "Tom's Room",
					"west"	:	 3 } ,
			3 : { "name"	:	 "the Hall",
					"east"	:	 2,
					"west"	:	 1,
					"south"	 :	 4,
					"north"	 :	 5} ,
			4 : { "name"	:	 "the Kitchen",
					"north"	 :	 3,
					"item"	:	 "bottle of vodka"} ,
			5 : { "name"	:	 "the Car Park",
					"south"	 :	 3},
			6 : { "name"	: "The Great Abyss. You are not welcome to play this game!"}
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

bedStart(deskStatus)

print ("\:\: END OF CODE \:\:")

#CURRENT FUNCIONAL POINT ---------------------------------------------------------------------#

#Looping logic of game:
while True:
	showStatus()

	#get the player's next move
	#.split(action, deskStatus,deskItemLocation) breaks it up into a list array
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
