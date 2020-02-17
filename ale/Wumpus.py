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

def superinput(input_text, valid_option_list):
    # input_text is a string that I will print every time I ask the player for input.
    # valid_option_list is a list of strings that includes all valid options for entry.

    #first, let's convert every item in the list to a STRING! This is because
    #the input command returns a string, and we don't know what we might get
    new_list = [str(i) for i in valid_option_list]

    print(input_text) #we print the question
    valid_answers = 'You can enter' #now let's start building a string with all the valid options.
    last_item = new_list.pop() #we take the last value from the list (as that's the value that needs an OR)
    for i in new_list:
        valid_answers = valid_answers + ' ' + i + ',' #concatenate each option
    valid_answers = valid_answers[:-1] #the string now has an extra comma, so we remove it.
    valid_answers = valid_answers + ' or ' + last_item +'.' #now we add the OR and the last item.
    print(valid_answers)
    new_list.append(last_item) #and we add the item to the list again.

    while (True):
        temp_input = input('Enter your response: ')
        if temp_input not in new_list:
            print('Invalid entry. Please try again.')
        else:
            return(temp_input)

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
        # print(f'You see in front of your 3 rooms: {maze[player][0]}, {maze[player][1]}, and {maze[player][2]}.')

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

        # IF player_armed = true       
        #    ask "move or shoot?"
        #    if "shoot"
        #       ask "Where do you want to shoot the arrow? 0, 1, 2?"
        #       shoot the arrow to room x
        #       if wumpus in room x
        #           they win
        #           end
        #       else
        #           player_armed = false
        #           arrow move to random room without wumpus or player
        #           repeat

        # ask "what room? 0, 1, 2?"
        input_text = 'What room do you want to go to?'
        input_list = [maze[player][0], maze[player][1], maze[player][2]]
        move_answer = superinput(input_text, input_list)
        # move to room x 
        player = int(move_answer)
        # repeat           

        #TODO: Make the wumpus move! random.randint(0,2). Before that, sometimes he doesnt move (random). Wumpus doesnt return to previous room.
    play_again = input('Would you like to play again? ')
    if(play_again == 'no'):
        break
        
    
    

    

