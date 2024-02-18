#Rock,Paper,Scissor
import random
rpc=['rock','paper','scissor']
choice=int(input('pick 1.Rock 2.Paper 3.Scissor'))
if(choice>3):
    print('You chose a wrong number and lost')
    #exit()
else:
    mychoice=rpc[choice-1]

    opponent=random.randint(0,2)
    opponentChoice=rpc[opponent]

    if(mychoice==rpc[0] and opponentChoice==rpc[2]):
        print('You win')
    elif(mychoice==rpc[1] and opponentChoice==rpc[0]):
        print('You win')
    elif(mychoice==rpc[2] and opponentChoice==rpc[1]):
        print('You win')
    elif(mychoice==rpc[0] and opponentChoice==rpc[0]):
        print('Draw')
    elif(mychoice==rpc[1] and opponentChoice==rpc[1]):
        print('Draw')
    elif(mychoice==rpc[2] and opponentChoice==rpc[2]):
        print('Draw')
    else:
        print(f'You lost.Opponent chose {opponentChoice}')


