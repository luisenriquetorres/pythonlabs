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

a = 'What room do you want to go to?'
b = [2, 4, '88']
#b = [2,4]
#print('what room should I go to?')
#print(f'Valid options are {b[0]}, {b[1]} and {b[2]}.')
answer = superinput(a, b)
print(f'you entered: {answer}')


