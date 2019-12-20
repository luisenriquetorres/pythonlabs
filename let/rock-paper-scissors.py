# Rock Paper Scissors
import random
import time

gestures = ['rock', 'paper', 'scissors']

print('ROCK PAPER SCISSORS')
print('===================')

game_is_still_on = True

while (game_is_still_on == True):
    player_needs_to_choose = True
    while (player_needs_to_choose == True):
        player_input = input('Choose: (r)ock, (p)aper or (s)cissors? ')
        player_input = player_input.lower()
        player_input = player_input[0]
        if (player_input != 'r' and player_input != 'p' and player_input != 's'):
            print('Sorry, you need to choose rock, paper or scissors')
        else:
            player_needs_to_choose = False
            player_choice = player_input

    print ('The computer is making its choice now...')
    time.sleep(1)
    computer_choice = gestures[random.randint(0,2)]
    print('get ready...')
    time.sleep(1)
    print ('ONE...')
    time.sleep(1)
    print ('TWO...')
    time.sleep(1)
    print ('THREE!')
    print ('The computer chose',computer_choice,'.')

    #now for the comparison.
    if ((player_input == 'r' and computer_choice[0] == 'p') or 
       (player_input == 'p' and computer_choice[0] == 's') or
       (player_input == 's' and computer_choice[0] == 'r')):
        print('the computer wins!')
        game_is_still_on = False
    elif ((player_input == 'r' and computer_choice[0] == 's') or 
       (player_input == 'p' and computer_choice[0] == 'r') or
       (player_input == 's' and computer_choice[0] == 'p')):
        print('you win!')
        game_is_still_on = False
    else:
        print('We tied. another round!')
        
    
    
