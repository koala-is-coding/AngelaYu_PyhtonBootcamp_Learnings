#Day-3 miniProject(TreasureIsland)
print('Welcome to Treasure Island.Your mission is to find the treasure')
lr=input('Left or Right?').lower()
if(lr=='left'):
    sw=input('Swim or Wait?').lower()
    if(sw=='wait'):
        doorCol=input('Which door?Red,blue or yellow?').lower()
        if(doorCol=='yellow'):
            print('You win :)')
        elif(doorCol=='red'):
            print('Burned by fire.Game Over')
        elif(doorCol=='blue'):
            print('Eaten by beasts.Game Over')
        else:
            print('Game Over')
    else:
        print('Attacked by trouts.Game Over')
else:
    print('Fell into a hole.Game Over')

        
    