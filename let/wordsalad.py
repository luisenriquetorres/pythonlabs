#WORDSALAD - Program I wrote to disprove the theory that you can read any
# word with the letters scrambled as long as the first and last letters of the
# word are kept. You send a paragraph through the function below and see the
# results
# LET - 1/27/2020

import random

def randomize_sentence(sentence):
    words = sentence.split() #create a list of words
    result = ''
    for oneword in words:
        letters = list(oneword) #create a list of letters
        word_length = len(letters) #number of letters 
        if (word_length < 4):
            result = result + oneword + ' '
            continue
        last_letter = letters[word_length-1]
        del letters[word_length-1]
        result = result + letters[0]
        del letters[0]
        word_length = len(letters)

        for x in range(word_length):
            current_length = len(letters)
            random_letter = random.randint(0,current_length-1)
            result = result + letters[random_letter]
            del letters[random_letter]
        result = result + last_letter + ' '
    return result

frase = 'The incredible problem with tergiversing sentences is that you almost never acquiesce to their changes'
print(randomize_sentence(frase))