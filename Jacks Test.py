#Raw input#
print ("Welcome to Ty Gwyn's Adventure!")
print ("\n[---------------------------------------------------------]")
print ("Let\'s start by getting your name.\n")
name = input("Type below here hit [Enter] \n-->").lower()
print ("Excellent!, It's nice to see you here again %s\n\n" % (name))

e1 = 1

room = int(input("What is your room number - 103, 108, or 104? \n-->"))
while (e1 == 1):
	if room == 104:
		e1 = e1 - 1
		break
	elif room == 108:
		e1 = e1 - 1
		break
	elif room == 103:
		e1 = e1 - 1
		break
	else:room = int(input("I\'m sorry, that room doesnt exist! Please try again -->"))

print ("\n[---------------------------------------------------------]\n")

print ("Ok, so you are %s and you are staying in room number %s.\n" % (name, room.upper))
begin = input("So, now we are all set up are you ready to go? \n-->").lower()

e2 = 1
while (e2 == 1):
	if begin == "yes":
		e2 = e2 - 1
		break
	elif begin == "no":
		e2 = e2 - 1
		break
	else:begin = input("I\'m sorry, that isn't the right answer! Please try again -->").lower()

print ("\n[---------------------------------------------------------] \n\n Then let us begin... \n\n[---------------------------------------------------------]")

#End of introduction#