#NOTES:
#Consider using 'in' function:
#e.g. if bed in action:
#should work in the same way as a "Contains" function - test when using python proper.

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>

#HEADER - Defining functions

import random

showInstructions = ("|<===========================================>|\n\nWelcome to the Ty Gwyn night out adventure\nCommands:\n Type \"Go To\" and one of the objects in the room = (e.g. desk, wardrobe, bed, sink, shelf, door)\nget [item]\n\nMISSON: Leave in the taxi to go on a famous Ty Gwyn night out in Cardiff.\n\n|<===========================================>|\n")

# COMPLETE STATUS BLOCK

deskStatus = "incomplete"
bedStatus = "incomplete"
sinkStatus = "incomplete"
wardrobeStatus = "incomplete"
deskItemLocation = random.randint(1,4)
bedItemLocation = random.randint(1,4)
sinkItemLocation = random.radint(1,3)
wardrobeLocation = random.radint(1,4)

#STARTING BLOCK

def bedStart(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation):
	print ("You are in your room ready to go on a night out.\nYou are sat on your bed and look around your room.\nIn front of you, you can see your desk. It has 2 draws.\nThere is a book shelf with books in and an empty beer bottle.\nYou look towards your left and you can see that the window is closed.\nTo your right is you wardrobe which is closed, and that your sink is empty.\nOn the other side of the wardrobe is the door out to the communal hallway.\n")
	action = input("\nWhere would you like to go next?\n-->").lower()
	
	#This refers to "Exit Bed" = eb. I will use this format for all of the exit codes (as its a little easier to use)

	eb = 1
	while (eb ==1 ):
		if action == "go to desk":
			desk(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to bed":
			bed(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to start":
			bedStart(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to sink":
			sink(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to shelf":
			shelf(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to wardrobe":
			wardrobe(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to door":
			door(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "help":
			print (showInstructions)
			action = input("When you have read the instructions, keep looking! \n-->").lower()
		elif action == "hint":
			print ("Here you want to pick one of the locations listed in the original dialogue.\nYou can see it here:\n\nYou are in your room ready to go on a night out.\nYou are sat on your bed and look around your room.\nIn front of you, you can see your desk. It has 2 draws.\nThere is a book shelf with books in and an empty beer bottle.\nYou look towards your left and you can see that the window is closed.\nTo your right is you wardrobe which is closed, and that your sink is empty.\nOn the other side of the wardrobe is the door out to the communal hallway.\n")
			action = input("When you have decided where to go, type below and hit [enter]\n-->").lower()
		else: action = input("That isn\'t a location in the room, try again!\n-->").lower()

#DESK BLOCK

def desk(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation):
	deskStatus = deskStatus
	action = action
	if deskStatus == "complete":
		print ("It looks like you already have the items you need from this area.\ntry looking in another area.")
		completeNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
	
	else :
		print ("You are standing at the desk.\nYou remember leaving your phone here but it doesn't appear to be on the surface top.\nIt must be in the area but you'll have to look.")
		deskNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)

def completeNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation):
	action = input("\nWhere would you like to go to next?\n-->").lower()
	edEndComplete = 1
	while (edEndComplete == 1):
		if action == "help":
			print (showInstructions)
			action = input("When you have read the instructions, keep looking! \n-->").lower()
		elif action == "go back":
			bedStart(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to desk":	
			desk(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to bed":
			bed(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to start":
			bedStart(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to sink":
			sink(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to shelf":
			shelf(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to wardrobe":
			wardrobe(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to door":
			door(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		else: action=input("That isn't a location in this room. Type \'help\' if you get stuck! \n-->").lower()

def deskNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation):
	action = input("\nWhere would you like to look first?\n-->").lower()
		#This refers to "Exit Desk" = ed. I will use this format for all of the exit codes (as its a little easier to use)
	ed = 1
	while (ed == 1):
		if action == "top drawer":
			if deskItemLocation == 1:
				ed = ed - 1
				print ("You found your phone in the top drawer.\nIt is added to your inventory\n\n|<===========================================>|\n")
				deskStatus = "complete"
				desk(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			else:
				action = input("You look into the top drawer and it appears empty.\nYou will need to continue searching!\n-->").lower()
		elif action == "bottom drawer":
			if deskItemLocation == 2:
				ed = ed - 1
				print ("You found your phone in the bottom drawer.\nIt is added to your inventory\n\n|<===========================================>|\n")
				deskStatus = "complete"
				desk(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			else:
				action = input("You look into the bottom drawer and it appears empty.\nYou will need to continue searching!\n-->").lower()
		elif action == "under the desk":
			if deskItemLocation == 3:
				ed = ed - 1
				print ("It appears your phone must have fallen on the floor.\nIt is added to your 	inventory\n\n|<===========================================>|\n")
				deskStatus = "complete"
				desk(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)		
				break			
			else:
				action = input("You look under the desk and there is nothing there.\nYou will need to continue searching!\n-->").lower()
		elif action == "behind the desk":
			if deskItemLocation == 4:
				ed = ed - 1
				print ("It appears your phone must have fallen behind the desk.\nIt is added to your inventory\n\n|<===========================================>|\n")
				deskStatus = "complete"
				desk(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)		
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
			bedStart(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to desk":
			desk(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to bed":
			bed(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to start":
			bedStart(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break	 
		elif action == "go to sink":
			sink(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to shelf":
			shelf(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to wardrobe":
			wardrobe(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to door":
			door(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		else: action=input("It doesn't seem like you are looking in the right places, something else, or type \'hint\' if you get stuck! \n-->").lower()

#BED BLOCK

def bed(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation):
  bedStatus = bedStatus
  action = action
  if bedStatus == "complete":
    print ("It looks like you already have the items you need from this area.\nTry looking in another area.")
    completeNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
  
  else :
    print ("You are standing by your bed. Your bed is untidy but you also can't be arsed to make it.\nYou remember you had your watch in bed but you look to your wrist but it isnt there.\nIt must be in the area but you'll have to look...")
    bedNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation) 

def bedNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation):
  action = input("\nWhere would you want to look first?\n-->").lower()
	ebEndComplete = 1
	while (ebEndComplete == 1):
		if action == "under the bed":
            if bedItemLocation == 1:
                eb = eb + 1
                print ("Your watch must have fallen on the floor during your pre night out power nap.\nYou collect it and put it on your wrist\n\n|<===========================================>|\n")
				bedStatus = "complete"
                bed(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
            else:
                action = input("\nYou look under the bed but all you see is old socks and shit you can't be bothered to tidy up. You will need to continue looking.\n-->")
        elif action == "behind the bed":
            if bedItemLocation == 2:
                eb = eb + 1
                print ("Your watch must have fallen behind your bed during your pre night out power nap.\nYou collect it and put it on your wrist\n\n|<===========================================>|\n")
                bedStatus = "complete"
				bed(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
            else:
                action = input("\nYou look behind the bed but all you see is dubious looking tissues. You will need to continue looking.\n-->")
        elif action == "in the duvet":
            if bedItemLocation == 3:
                eb = eb +1
                print ("Your watch must have fallen off in the duvet during your pre night out power nap.\nYou collect it and put it on your wrist\n\n|<===========================================>|\n")
                bedStatus = "complete"
				bed(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
            else:
                action = input("\nYou look in the duvet but you can't see your watch. You dump the duvet back on the bed in a heap and continue searching.\n-->")
        elif action == "under your pillow"
            if bedItemLocation == 4:
            	eb = eb + 1
               	print("\nYou look under your pillow and you see a pair of old boxers (which should probably go in the wash) and your watch which you collect and place on your wrist\n\n|<===========================================>|\n")
                bedStatus = "complete"
				bed(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
            else:
                action = input("You look under your pillow and all you see is a crusty pair of boxers. You hide them again with the pillow and continue looking.\n-->")
   		elif action == "help":
    		print (showInstructions)
			action = input("When you have read the instructions, keep looking! \n-->").lower()
		elif action == "hint":
			print ("You should probably look behind and under your bed, under your pillow and under your duvet as thats where it is likely to be")
			action	= input("When you are ready to keep looking, try typing in one of the instructions shown! \n-->").lower()
		elif action == "go back":
			bedStart(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to desk":
			desk(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to bed":
			bed(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to start":
			bedStart(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break	 
		elif action == "go to sink":
			sink(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to shelf":
			shelf(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to wardrobe":
			wardrobe(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to door":
			door(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		else: action=input("It doesn't seem like you are looking in the right places, something else, or type \'hint\' if you get stuck! \n-->").lower()	
  
#SINK BLOCK

def sink(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation):
      sinkStatus = sinkStatus
  action = action
  if sinkStatus == "complete":
    print ("It looks like you already have the items you need from this area.\nTry looking in another area.")
    completeNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
  
  else :
    print ("You look into the sink. You see white rings running from the top to the bottom.\nThis must have been from when you decided to wash in the sink when the showers were full.\nYou see a your murkey reflection in front of you.\n You should clean the mirror. There is a noticable cluster of finger prints to the right of the mirror.\nIt appears to have been moved many times\nYou remember seeing your wallet there last time you were shaving - although it was some time ago.\nIt must be in the area but you'll have to look...")
    sinkNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation) 

def sinkNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation):
  action = input("\nWhere would you want to look first?\n-->").lower()
	esEndComplete = 1
	while (esEndComplete == 1):
		if action == "in the sink":
            if sinkItemLocation == 1:
                eb = eb + 1
                print ("It was right in front of you all along. Are you losing your sight?.\nYou collect it and put it in your pocket\n\n|<===========================================>|\n")
                sinkStatus = "complete"
				sink(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
            else:
                action = input("\nAll you see is those white rings and dispare fills you up.\nYou really should clean the sink but you would be late for the night out...\nYou will need to continue looking.\n-->")
        elif action == "behind the mirror":
			if sinkItemLocation == 2:
    			eb = eb + 1
                print ("You grab the right and side of the mirror and pull it forward.\nYou revel a set of shelves where you see you toilitaries, painkillers and your wallet.\nYou collect it and put itin your pocket\n\n|<===========================================>|\n")
                sinkStatus = "complete"
				sink(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
            else:
    			action = input("\nYou grab the right and side of the mirror and pull it forward.\nYou revel a set of shelves where you see you toilitaries, painkillers, but no wallet. You will need to continue looking.\n-->")
        elif action == "on the floor":
            if sinkItemLocation == 3:
    			eb = eb + 1 
				print ("You look to the floor and see your wallet\nThere's no cash in it (of course) and an old out of date condom.\nYou collect it and put it on your wrist\n\n|<===========================================>|\n")
				sinkStatus = "complete"
				sink(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
            else:
                action = input("If it was on the floor you probably would have stepped on it.\nYou continue searching...\n-->")
   		elif action == "help":
    			print (showInstructions)
			action = input("When you have read the instructions, keep looking! \n-->").lower()
		elif action == "hint":
			print ("You should probably look in the sink or on the floor. Now you mention it, that mirror looks like there could be something behind it...")
			action	= input("When you are ready to keep looking, try typing in one of the instructions shown! \n-->").lower()
		elif action == "go back":
			bedStart(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to desk":
			desk(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to bed":
			bed(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to start":
			bedStart(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break	 
		elif action == "go to sink":
			sink(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to shelf":
			shelf(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to wardrobe":
			wardrobe(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			breask
		elif action == "go to door":
			door(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		else: action=input("It doesn't seem like you are looking in the right places, something else, or type \'hint\' if you get stuck! \n-->").lower()	

#SHELF BLOCK

def shelf(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation):
	print ("Shelf")

#WARDROBE BLOCK

def wardrobe(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation):
  wardrobeStatus = wardrobeStatus
  action = action
  if wardrobeStatus == "complete":
    print ("It looks like you already have the items you need from this area.\nTry looking in another area.")
    completeNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
  
  else :
    print ("You realise that you need to get ready.\nYou go to your wardrobe to find your night out shirt.\nYou were pretty sure you \"ironed it\" and \"hung it up\" but you can't be sure.\nYou wore it only recently and you think it is here somewhere?\nYou open the wardrobe and look around.\nThere is a shelf of T-Shirts, a hanging rail, and a wash basket.\nIt must be in the area but you'll have to look...")
    wardrobeNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation) 

def wardrobeNest(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation):
    	action = input("\nWhere would you like to look first?\n-->").lower()
		#This refers to "Exit Wardrobe" = ew. I will use this format for all of the exit codes (as its a little easier to use)
	ew = 1
	while (ew == 1):
		if action == "on the shelf":
			if wardrobeItemLocation == 1:
				ew = ew - 1
				print ("It appears you actually folder your shirt up and put it away - ITS A MIRACLE!!!\nYou put it on and look closer to being ready for a night out.\n\n|<===========================================>|\n")
				wardrobeStatus = "complete"
				wardrobe(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			else:
				action = input("You look at the shelg and can\'t see your shirt.\nYou will need to continue searching!\n-->").lower()
		elif action == "on the floor":
			if wardrobeItemLocation == 2:
				ew = ew - 1
				print ("Of course! Where else would it be\nYou attempt to straighten out the crumpled McCoys crisp of a shirt and put it on.\n\n|<===========================================>|\n")
				wardobeStatus = "complete"
				wardrobe(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			else:
				action = input("Hmmm. that suprising! For once it isn't on the floor.\nYou will need to continue searching!\n-->").lower()
		elif action == "hung up":
			if wardrobeItemLocation == 3:
				ew = ew - 1
				print ("For once in your life it appears that you hung up your shirt.\nIt is only mildly creased from its last wear - the benefits of using a hanger!\nYou put it on and it doesn\'t smell all that bad. \n\n|<===========================================>|\n")
				wardrobeStatus = "complete"
				wardrobe(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)		
				break			
			else:
				action = input("Nope! No suprises that you didn\'t hang it up.\nYou will need to continue searching!\n-->").lower()
		elif action == "in the wash basket":
			if wardrobeItemLocation == 4:
				ew = ew - 1
				print ("You see it in your wash basket. You know you shouldn't bit it IS your night out shirt.\nYou pick it out of the basket, brush it off, shake it out, and give it a smell.\nA quick spray of lynx africa will sort that right out!.\nAfter a good 3 seconds of lynx you pop it on ready for your night out\n\n|<===========================================>|\n")
				wardrobeStatus = "complete"
				wardrobe(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)		
				break
			else:
				action = input("it\'s not in the basket so must be \"clean\". I suppose you should keep looking\n-->").lower()
		elif action == "help":
			print (showInstructions)
			action = input("When you have read the instructions, keep looking! \n-->").lower()
		elif action == "hint":
			print ("It\'s not a big cupboard to be fair. Its unlikely you hung it up or put it on the shelf, most likely it\'s in the wash basket or on the floor...")
			action	= input("When you are ready to keep looking, try typing in one of the instructions shown! \n-->").lower()
		elif action == "go back":
			bedStart(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to desk":
			desk(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to bed":
			bed(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to start":
			bedStart(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break	 
		elif action == "go to sink":
			sink(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to shelf":
			shelf(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to wardrobe":
			wardrobe(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		elif action == "go to door":
			door(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)
			break
		else: action=input("It doesn't seem like you are looking in the right places, something else, or type \'hint\' if you get stuck! \n-->").lower()

#DOOR BLOCK

def door(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation):
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

bedStart(deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation)

print ("\:\: END OF CODE \:\:")

#CURRENT FUNCIONAL POINT ---------------------------------------------------------------------#

#Looping logic of game:
while True:
	showStatus()

	#get the player's next move
	#.split(action,deskStatus,deskItemLocation,bedStatus,bedItemLocation,sinkStatus,sinkItemLocation,wardrobeStatus,wardrobeLocation) breaks it up into a list array
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
