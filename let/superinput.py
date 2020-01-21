def superinput(input_text, valid_options):
    # input_text is a string that I will print every time I ask the player for input.
    # valid_options is a list of strings that includes all valid options for entry.
    while (True):
        temp_input = input(input_text)
        if temp_input not in valid_options:
            print('Invalid entry. Please try again.')
        else:
            return(temp_input)

a = 'Enter the room number: '
b = ['02', '04', '88']
print('what room should I go to?')
print(f'Valid options are {b[0]}, {b[1]} and {b[2]}.')
answer = superinput(a, b)
print(f'you entered: {answer}')


