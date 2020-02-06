#Hunt the Wumpus
import random
from colorama import init, Fore, Back, Style
init(convert=True)

def print_maze(player_position):
    cuartos=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17']
    cuartos[player_position] = Back.LIGHTRED_EX + cuartos[player_position] + Style.RESET_ALL


    print(f'         /---{cuartos[0]}---\ ')
    print('        /     |    \ ')
    print(f'   /---/    /{cuartos[6]}\    \---\ ')
    print('  /        /    \        \ ')
    print(f'{cuartos[5]}       {cuartos[15]}     {cuartos[7]}\      {cuartos[1]}')
    print(' | \--\  / \   /   \ /--/ |')
    print(f' |     {cuartos[14]}    {cuartos[16]}    {cuartos[8]}     |')
    print(' |      |     |     |     |')
    print(f' |     {cuartos[13]}    {cuartos[17]}    {cuartos[9]}     |')
    print(' | /--/ \  /   \   / \--\ |')
    print(f'{cuartos[4]}       {cuartos[12]}     {cuartos[10]}/      {cuartos[2]}')
    print('  \        \    /        /')
    print(f'   \---\    \\{cuartos[11]}/    /---/')
    print('        \     |    /')
    print(f'         \---{cuartos[3]}---/')

def comparar_wumpus(posicion_wumpus):
    while True:
        objeto = random.randint(1,17)
        if (objeto != posicion_wumpus):
            break
    return objeto

#create a list that contains all the exits 
maze = [
    [5, 6, 1], #room 0
    [0, 8, 2], #room 1
    [1, 9, 3], #room 2
    [2, 11, 4], #room 3
    [3, 13, 5], #room 4
    [4, 14, 0], #room 5
    [0, 7, 15], #room 6
    [6, 16, 8], #room 7
    [7, 1, 9], #room 8
    [8, 10, 2], #room 9
    [11, 17, 9], #room 10
    [12, 10, 3], #room 11
    [13, 17, 11], #room 12
    [4, 14, 12], #room 13
    [5, 15, 13], #room 14
    [14, 6, 16], #room 15
    [15, 7, 17], #room 16
    [16, 12, 10]] #room 17


while(True):
    player = 0  #Player stores the player's current location throughout the game
    wumpus = random.randint(1, 17) #location of the wumpus. It growls.
    arrow = comparar_wumpus(wumpus) #location of the arrow. It glows.
    player_armed = False

    #CODE START: Infinite loop so the player can move.
    #The only way to break this loop is for the player to WIN. Or to DIE.
    
    while(True):
        #FIRST: Print player location info: Where he is, what exits are available, whether there's a growl, smell or shine.
        #player location and exits
        print_maze(player) 
        print(f'You are in room {player}.')
        print(f'You see in front of your 3 rooms: {maze[player][0]}, {maze[player][1]}, and {maze[player][2]}.')

        #now to see if there's a wumpus smell, or if the wumpus is here (player is dead!)
        if(wumpus == player):
            print('The wumpus is here and it kills you. Goodbye.')
            break
        elif (wumpus == maze[player][0] or
              wumpus == maze[player][1] or
              wumpus == maze[player][2]):
            print('You hear a growl. The wumpus is near, probably in one of the rooms you see in front of you.')

        if(arrow == player):
            print('You walk into the room, and you see a single arrow. You pick it up.')
            player_armed = True
            arrow = 18
        elif (arrow == maze[player][0] or
              arrow == maze[player][1] or
              arrow == maze[player][2]):
            print('You see a glow coming from one of the rooms in front of you. That arrow must be close.')


        #TODO: The player should also be able to shoot an arrow at a room. If the wumpus is in the room, it dies and the player wins.
        # if the player misses, he has only one arrow total, so he can't shoot anymore.

        #SECOND: Ask the player what he/she wants to do. Infinite loop that is broken when player enters valid option
        while(True):
            if (player_armed == True):
                first_imput = input('What room do you want to go to? Or, if you want, press A to shoot arrow: ')
                # code to process arrow and movement
            else:
                new_room = input('What room do you want to go to? ')
                new_room = int(new_room) #input returns a string, but we need an integer since room numbers are integers
                if(new_room == maze[player][0] or
                new_room == maze[player][1] or
                new_room == maze[player][2]):
                    break #valid entry, break the loop and continue
                else:
                    print('Learn to read.') #invalid entry. Ask again! 
        player = int(new_room) #Here the player changes location

        #TODO: Make the wumpus move! random.randint(0,2). Before that, sometimes he doesnt move (random). Wumpus doesnt return to previous room.

    play_again = input('Would you like to play again? ')
    if(play_again == 'no'):
        break
        
    
    

    

