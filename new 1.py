#Raw input#
print ("Welcome to Ty Gwyn's Adventure!")
print ("[---------------------------------------------------------]")
print ("Let\'s start by getting your name.")
name = input("Type below here hit [Enter] -->").lower()
print ("Excellent!, It's nice to see you here again %s" % (name))

e1 = 1

room = input("What is your room number - 103, 108, or 104? -->")

while (e1 == 1):
	if room == 104:
		e1 = e1 - 1
	elif room == 108:
		e1 = e1 - 1
	elif room == 103:
		e1 = e1 - 1
	else:room = int(input("I\'m sorry, that room doesnt exist! Please try again -->"))
	
print ("Ok, so you are %s and you are staying in room number %s." % (name, room))
begin = input("So, now we are all set up are you ready to go? -->").lower()

e2 = 1
while (e2 == 1):
	if begin == "yes":
		e2 = e2 - 1
		break
	elif begin == "no":
		e2 = e2 - 1
		break
	else:begin = input("I\'m sorry, that isn't the right answer! Please try again -->").lower()