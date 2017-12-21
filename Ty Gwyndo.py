import random

playerhealth = 3
mobhealth = 3
print('You are approached by NAME to play a game of Ty Gwyndo. You excitedly accept. You need to throw the ball into all 3 of NAMEs cup. The first person to lose all 3 cups is the loser.')
while (playerhealth != 0 and mobhealth !=0):
    
    print ('You can either throw a steady shot(1) or a trick shot (2)')
    playerinput=input()
    if playerinput == '1':
        playerinput =1
    elif playerinput =='2':
        playerinput =2
    else: input('NAME is waiting for you to throw! Enter 1 for a steady shot, or 2 for a trick shot.\n')
    randominput= random.randint(1,2)
    if playerinput==randominput:
        mobhealth=mobhealth-1
        print ('You throw the ball and get it into one of NAMEs cups. NAME has ',mobhealth, 'cups left.')
    elif playerinput != randominput:
        print ('You missed. NAME still has',mobhealth, 'cups left.')
        
    if mobhealth!=0:
        print ('NAME lines up a shot and throws...')
        mobinput = random.randint(1,2)
        mrandominput = random.randint(1,2)
        if mobinput== mrandominput:
            print('NAME gets the shot in one of your cups!')
            playerhealth = playerhealth-1
            print ('You have ',playerhealth, 'cups left.')
        else: print('NAME missed! You still have ',        playerhealth, 'cups left.')
if playerhealth==0:
    print('You have lost all of your cups. You Lose!')
if mobhealth==0:
    print ('NAME has lost all of their cups. You win!')
