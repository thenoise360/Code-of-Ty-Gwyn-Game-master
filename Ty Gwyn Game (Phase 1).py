def showInstructions():
    #print the  main menu and controls
    print("===========================================")
    print("Welcome to the Ty Gwyn night out adventure!")
    print("Commands:")
    print("'go [direction]'(north, south, east, west)")
    print("'get [item]'")
    print("MISSON: Leave in the taxi to go on a famous Ty Gwyn night out in Cardiff.")

def Player():
    #Ask the user their name to determine starting point
    print("But before we start, what is your name?")

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

showInstructions()

Player()
PlayerName=input().lower
if PlayerName == "jack":
    print("Oh so you are the famous " + PlayerName + "! Let's put you in your room!")
elif PlayerName == "tom":
    print("Oh so you are the famous " + PlayerName + "! Let's put you in your room!")
else: print("You are not cool enough to be included in this game")

#Define Starting Point
if PlayerName == "Jack":
    currentRoom = 1
elif PlayerName == "Tom":
    currentRoom = 2
else: currentRoom = 6

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


        

    
    

                  
