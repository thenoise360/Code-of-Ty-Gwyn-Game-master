import random

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
        10: "Ben"}

MOB = random.randint(1,10)

playerhealth = 3
mobhealth = 3
print('You are approached by', TGs[MOB], ' to play a game of Ty Gwyndo. You excitedly accept. You need to throw the ball into all 3 of NAMEs cup. The first person to lose all 3 cups is the loser.')
while (playerhealth != 0 and mobhealth !=0):
    
    print ('You can either throw a steady shot(1) or a trick shot (2)')
    playerinput=input()
    if playerinput == '1':
        playerinput =1
    elif playerinput =='2':
        playerinput =2
    else: input('Everyone is waiting for you to throw! Enter 1 for a steady shot, or 2 for a trick shot.\n')
    randominput= random.randint(1,2)
    if playerinput==randominput:
        mobhealth=mobhealth-1
        print ('You throw the ball and get it into one of', TGs[MOB], 'cups.', TGs[MOB], ' has ',mobhealth, 'cups left.')
    elif playerinput != randominput:
        print ('You missed.', TGs[MOB], ' still has',mobhealth, 'cups left.')
        
    if mobhealth!=0:
        print (TGs[MOB], ' lines up a shot and throws...')
        mobinput = random.randint(1,2)
        mrandominput = random.randint(1,2)
        if mobinput== mrandominput:
            print(TGs[MOB], ' gets the shot in one of your cups!')
            playerhealth = playerhealth-1
            print ('You have ',playerhealth, 'cups left.')
        else: print(TGs[MOB], ' missed! You still have ',        playerhealth, 'cups left.')
if playerhealth==0:
    print('You have lost all of your cups. You Lose!')
if mobhealth==0:
    print (TGs[MOB], ' has lost all of their cups. You win!')
