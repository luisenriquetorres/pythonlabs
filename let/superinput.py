def superinput(input_text, valid_option_list):
    # input_text is a string that I will print every time I ask the player for input.
    # valid_option_list is a list of strings that includes all valid options for entry.

    #first, let's convert every item in the list to a STRING! This is because
    #the input command returns a string, and we don't know what we might get
    new_list = [str(i) for i in valid_option_list]

    print(input_text)
    valid_answers = 'You can enter'
    last_item = new_list.pop()
    for i in new_list:
        valid_answers = valid_answers + ' ' + i
        if len(new_list) > 1:
            valid_answers = valid_answers + ','
    valid_answers = valid_answers + ' or ' + last_item +'.'
#    valid_answers = valid_answers + '.'
    print(valid_answers)
    new_list.append(last_item)

    while (True):
        temp_input = input('Enter your response: ')
        if temp_input not in new_list:
            print('Invalid entry. Please try again.')
        else:
            return(temp_input)

a = 'What room do you want to go to?'
b = [2, 4, '88']
#b = [2,4]
#print('what room should I go to?')
#print(f'Valid options are {b[0]}, {b[1]} and {b[2]}.')
answer = superinput(a, b)
print(f'you entered: {answer}')


