def tyGwyndo(action):
    #This is to determine the 'Variable Mob' (vmob) which is to have the
	#person who's not playing as the final mob option.
	#This will need to be more complex in future when the players are more
	#than just Tom or Jack
	if playername == 'jack':
   		vmob="Tom"
	elif playername == 'tom':
   		vmob="Jack"

	#Dictionary of Ty Gwyners (TGs)
	TGs = {
       	1: "Zaz",
       	2: "Matt",
       	3: "Ross",
       	4: "Charlie",
       	5: "Chris",
       	6: "Bron",
       	7: "Sara",
       	8: "Liv",
       	9: "Em",
       	10: "Ben",
       	11: vmob}

	# Random allocation of a number to the mob which coincides with the
	#dictionary above
	MOB = random.randint(1,11)

	#Setting the health stats for the game (will need to be more complex later)
	playerHealth = 6
	mobHealth = 6

	#Starting the narrative
	print ('You are approached by ', TGs[MOB], ' to play a game of Ty Gwyndo.')
	print ('You excitedly accept.')
	print ('You need to throw the ball into all 6 of ',TGs[MOB], ' cups.')
	print ('The first person to lose all 6 cups is the loser.')
	print ('If you land a normal shot, you can remove 1 cup. If you land a trick shot you can remove 2 cups.')
	coinFlip = random.randint(1,2)
	if coinFlip == 1:
    	print ('You flip a coin for first play.\nIt lands on heads so it looks like you are going first.\nEither throw a normal shot (1) or a trick shot (2).\n\n|<===========================================>|\n\n')
		playerInput(action,mobhealth,playerHealth)
	else:
		print ('You flip a coin for first play.\nIt lands on tails so it looks like ' TGs[MOB]' is going first.\n\n|<===========================================>|\n\n')
		mobInput(action,mobhealth,playerHealth)

def playerTurn(action,mobHealth,playerHealth):
	if playerHealth > 0:
		playerInput = input('Take your shot\n-->')
		randomInput= random.randint(1,3)
		if playerInput == 1|2:
   			if playerInput>randomInput:
       			mobHealth=mobHealth-1
       			print ('You throw the ball and get it into one of ', TGs[MOB], ' cups.')
				mobHealth = mobHealth - playerInput
       			print (TGs[MOB], 'has ',mobHealth, ' cups left.')
				print ('You get another turn\n\n|<===========================================>|\n\n')
   			else playerInput != randomInput:
       			print ('You missed!')
       			print (TGs[MOB], 'still has',mobHealth, 'cups left.')
				mobTurn(action,mobHealth,playerHealth)
		else:
			print ('Everyone is waiting for you to throw!')
       		print ('Enter 1 for a steady shot, or 2 for a trick shot.')
	else:
		print ('You have lost all of your cups.')
		print ('YOU LOSE!')
		print ('Would you like to try again?')
		retry input('-->').lower
		if retry == 'yes'|'y':
			tyGwyndo(action)
		else:
			kitchen(action)

def mobTurn(action,mobHealth,playerHealth):
   	if mobHealth > 0:
       	print (TGs[MOB], ' lines up a shot and throws...')
       	mobInput = random.randint(1,2)
       	mRandomInput = random.randint(1,3)
       	if mobInput > mRandomInput:
           	print (TGs[MOB], ' gets the shot in one of your cups!')
           	playerHealth = playerHealth - mRandomInput
           	print ('You have ',playerHealth, ' cups left.')
			print (TGs[mob],' gets another turn!\n\n|<===========================================>|\n\n')
			mobTurn(action,mobHealth,playerHealth)
       	elif mobInput!= mRandomInput:
           	print (TGs[MOB], ' missed!')
           	print ('You still have ',playerHealth, ' cups left.')
			print ('Now it is your turn.\n\n|<===========================================>|\n\n')
			playerTurn(action,playerHealth,mobHealth)
	else:
		print (TGs[MOB], 'has lost all of their cups.')
    	print ('YOU WIN!')
		print ('Would you like to try again?')
		retry input('-->').lower
		if retry == 'yes'|'y':
			tyGwyndo(action)
		else:
			drunk(action)
