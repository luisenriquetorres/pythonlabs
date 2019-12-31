# Hunt the Wumpus
import random
from colorama import init, Fore, Back, Style
init(convert=True)

# First let's make a 24 room maze.
maze = [
    [5,6,1], #room0
    [0,8,2], #room1
    [1,9,3], #room2
    [2,11,4], #room3
    [3,13,5], #room4
    [0,14,4], #room5
    [0,15,7], #room6
    [6,16,8], #room7
    [7,1,9], #room8
    [8,2,10], #room9
    [9,17,11], #room10
    [12,10,3], #room11
    [13,17,11], #room12
    [14,12,4], #room13
    [5,15,13], #room14
    [6,16,14], #room15
    [15,7,17], #room16
    [16,12,10]] #room17

room_name = ['Main Gate', 'Dark Cave', 'Small Temple', 'Unknown Corridor', 'Crystal Chamber',
'Creepy Crevice', 'Slippery Slope', 'Cold Chamber', 'Freezing Room', 'Marble Chamber',
'Sandy Arena', 'Heathen Hall', 'Minion Quarters', 'Stone Sanctum', 'Mossy Quarry',
'Narrow Corridor', 'Throne Room', 'Large Temple']

#print_maze: visually print the maze and show player location
def print_maze(player_location):
    rooms=[' 0',' 1',' 2',' 3', ' 4', ' 5',
        ' 6', ' 7', ' 8', ' 9', '10',
        '11', '12', '13', '14', '15',
        '16', '17']

    rooms[player_location] = Back.BLUE + rooms[player_location] + Style.RESET_ALL
    print('')
    print(f'         /---{rooms[0]}---\ ')
    print(f'        /     |    \ ')
    print(f'   /---/    /{rooms[6]}\    \---\ ')
    print(f'  /        /    \        \ ')
    print(f'{rooms[5]}       {rooms[15]}     {rooms[7]}\      {rooms[1]}')
    print(f' | \--\  / \   /   \ /--/ |')
    print(f' |     {rooms[14]}    {rooms[16]}    {rooms[8]}     |')
    print(f' |      |     |     |     |')
    print(f' |     {rooms[13]}    {rooms[17]}    {rooms[9]}     |')
    print(f' | /--/ \  /   \   / \--\ |')
    print(f'{rooms[4]}       {rooms[12]}     {rooms[10]}/      {rooms[2]}')
    print(f'  \        \    /        /')
    print(f'   \---\    \\{rooms[11]}/    /---/')
    print(f'        \     |    /')
    print(f'         \---{rooms[3]}---/')
    print('')
    # print('         /---00---\ ')
    # print('        /     |    \ ')
    # print('   /---/    /06\    \---\ ')
    # print('  /        /    \        \ ')
    # print('05       15     07\      01')
    # print(' | \--\  / \   /   \ /--/ |')
    # print(' |     14    16    08     |')
    # print(' |      |     |     |     |')
    # print(' |     13    17    09     |')
    # print(' | /--/ \  /   \   / \--\ |')
    # print('04       12     10/      02')
    # print('  \        \    /        /')
    # print('   \---\    \\11/    /---/')
    # print('        \     |    /')
    # print('         \---03---/')

def random_arrow_location(other_place):
    while True:
        arrow = random.randint(1,17)
        if (other_place != arrow):
            break
    return arrow

player = 0
wumpus = random.randint(1,17)
arrow = random_arrow_location(wumpus)
player_has_arrow = False

while (True):
    print_maze(player)
#    print(f'You are in room  {player}.')
#    print(f'There are exits that take you to rooms {maze[player][0]}, {maze[player][1]} and {maze[player][2]}.')
    if (arrow == maze[player][0] or arrow == maze[player][1] or arrow == maze[player][2]):
        print('you see the glint of reflected light coming from somewhere. The arrow is in a room nearby!')
    
    if (wumpus == maze[player][0] or wumpus == maze[player][1] or wumpus == maze[player][2]):
        print('you hear a menacing growl. The wumpus is in a room nearby!')
    
    if (player == wumpus):
        print('The wumpus is here! It lunges at you and kills you in a few seconds.')
        print('GAME OVER. YOU LOSE!')
        quit()
    
    if (player == arrow):
        print('the bow and arrow are here! You grab them. Now you can use them to kill the wumpus!')
        arrow = 18 #a non-existent room
        player_has_arrow = True

    new_location = player
    while(new_location == player):
        input_ask = 'Enter a room number to move to'
        if (player_has_arrow == True):
            input_ask = input_ask + ', or enter A to fire the arrow'
        input_ask = input_ask + ': '
        player_input = input(input_ask)
        if (player_input.lower() == 'a' and player_has_arrow == True):
            #player is firing the arrow (he has it)
            while True:
                print(f'You can fire the arrow at room {maze[player][0]}, {maze[player][1]} or {maze[player][2]}.')
                arrow_input = input('Which room do you want to fire it at?')
                if (arrow_input.isnumeric()):
                    arrow_destination = int(arrow_input)
                    if (arrow_destination == maze[player][0] or arrow_destination == maze[player][1] or arrow_destination == maze[player][2]):
                        break
            
            if (arrow_destination == wumpus):
                print('The wumpus screams in pain and dies. You killed the wumpus!')
                print('GAME OVER. YOU WON!')
                quit()
            
            print('the arrow flies noiselessly into an empty room. You missed the wumpus and lost the arrow.')
            print('hopefully there is another arrow somewhere nearby.')
            player_has_arrow = False
            while True:
                arrow = random_arrow_location(wumpus)
                if (arrow != player):
                    break
        else:
            #player is moving to a different room
            if (player_input.isnumeric() == False):
                player_input = '18'
            new_location = int(player_input)
            if (new_location != maze[player][0] and new_location != maze[player][1] and new_location != maze[player][2]):
                print('That is not a valid entry, please try again.')
                new_location = player
            else:
                print('you move to the new room.')
                player = new_location
                new_location = 18
        
    #TODO: Wumpus moves!
