import random

game_over = False
play_again= True

while (play_again == True):
    while (game_over == False):
        #preguntarle al jugador cual quiere
        player_choice = input('Which one do you prefer? Rock, paper, or scissors? ')
        player_choice = player_choice.lower()
        computer_choice = random.randint(1,3)
        if (computer_choice == 1):
            computer_new_choice = 'rock'
        if (computer_choice == 2):
            computer_new_choice = 'scissors'
        if (computer_choice == 3):
            computer_new_choice = 'paper'

        # print(computer_new_choice)
        print('You chose', player_choice,'.')
        print('The computer chose', computer_new_choice,'.')

        if (computer_new_choice == 'paper' and player_choice == 'rock'):
            print('The computer won. ')
            game_over = True
        elif (computer_new_choice == 'scissors' and player_choice == 'paper'):
            print('The computer won. ')
            game_over = True
        elif (computer_new_choice == 'rock' and player_choice == 'scissors'):
            print('The computer won. ')
            game_over = True
        elif (computer_new_choice == 'paper' and player_choice == 'scissors'):
            print('You have won.')
            game_over = True
        elif (computer_new_choice == 'rock' and player_choice == 'paper'):
            print('You have won. ')
            game_over = True
        elif (computer_new_choice == 'scissors' and player_choice == 'rock'):
            print('You have won. ')
            game_over = True
        else:
            print('It is a tie.')

    play_again = False
    new_game = input('do you want to play again? (yes/no)')
    if (new_game == 'yes'):
        play_again = True
        game_over = False
