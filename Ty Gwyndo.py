#########The Ty Gwyndo Mini Game Code

#You need to import the random functions:
import random


#----------------Only needed when standalone (not in full game)--------#
print("What is your name?")
playername = input().lower()

#----------------------------------------------------------------------#

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
#//<-----Jack Notes----->\\#
# Worth making it 6 / 8?
playerhealth = 3
mobhealth = 3

#Starting the narrative
print('You are approached by', TGs[MOB], 'to play a game of Ty Gwyndo.')
print('You excitedly accept.')
print('You need to throw the ball into all 3 of',TGs[MOB], 'cups.')
print('The first person to lose all 3 cups is the loser.')

#Creating the while loop of logic so that when the playerhealth isn't 0
#it asks them to input a shot option
while (playerhealth != 0):
    
    print ('You can either throw a steady shot(1) or a trick shot (2)')
    playerinput=input()
#Creating a nested while that only allows for 1's and 2's to be entered

#//<-----Jack Notes----->\\#
#Could create a loop based on - while (playerinput == 1|2) - This will only loop if one or two
#Currently it looks like it will only loop if 2 is selected?

    while (playerinput != '1'):
        if playerinput == '2':
            break
        print ('Everyone is waiting for you to throw!')
        print ('Enter 1 for a steady shot, or 2 for a trick shot.')
        playerinput = input()
#Not sure if this next bit is needed, will take it out and do some testing
#but keep in for now
    if playerinput == 1:
        playerinput =1
    elif playerinput ==2:
        playerinput =2        
#Randomisation of either 1 or 2 given to  randominput
    randominput= random.randint(1,2)
##BATTLE LOGIC
#Player chooses 1 or 2. Randomiser creates either a 1 or a 2. If the numbers
#match then the player scores a hit, nothing happens if not

#//<-----Jack Notes----->\\#
#Possibly make it that a trick shot means you can get rid of 2 health, or that the other player takes two turns to make it riskier.
#If you miss you can also loose 2, or the mob gets 2 goes. The same can be said for missing a standard shot means they only lose one / get a single go?:
    
    # if playerinput==randominput:
        #mobhealth=mobhealth-playerinput
        #print ('You throw the ball and get it into one of', TGs[MOB], 'cups.')
        #print(TGs[MOB], 'has',mobhealth, 'cups left.')
    #elif playerinput != randominput:
        #playerHealth=playerHealth-playerinput
        #print ('You missed. you lose %s cups.') % (playerinput)
        #print (TGs[MOB], 'still has',mobhealth, 'cups left.')

#MOB then has the same logic applied, except that its 'input' is also
#randomised
    if playerinput==randominput:
        mobhealth=mobhealth-1
        print ('You throw the ball and get it into one of', TGs[MOB], 'cups.')
        print(TGs[MOB], 'has',mobhealth, 'cups left.')
    elif playerinput != randominput:
        print ('You missed.')
        print (TGs[MOB], 'still has',mobhealth, 'cups left.')
#MOB then has the same logic applied, except that its 'input' is also

#//<-----Jack Notes----->\\#
#Could apply the same negative logic here - The mob can hurt itself?
#If not now then possibly in a later chapter (or in a different form e.g. tool health?)

#randomised
    if mobhealth!=0:
        print (TGs[MOB], ' lines up a shot and throws...')
        mobinput = random.randint(1,2)
        mrandominput = random.randint(1,2)
        if mobinput== mrandominput:
            print(TGs[MOB], 'gets the shot in one of your cups!')
            playerhealth = playerhealth-1
            print ('You have ',playerhealth, 'cups left.')
        elif mobinput!= mrandominput:
            print(TGs[MOB], ' missed!')
            print('You still have ',playerhealth, 'cups left.')
#The only scenarios that end the game are a win or a lose
if playerhealth==0:
    print('You have lost all of your cups.')
    print('YOU LOSE!')
if mobhealth==0:
    print (TGs[MOB], 'has lost all of their cups.')
    print ('YOU WIN!')
#-------END----------------------------------------------------##
