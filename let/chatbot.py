# We will code a chatbot in this example

#first we will say hi
print('Hello! I am your new Chatbot. My name is chatboxxxxx!')
name=input('What is your name? ')  # I'm asking for the name
print('Hello',name,', its nice to meet you!') #now I'm saying hi

#get year information
year = input ('tell me, what year is it?')
year = int(year) #INPUT returns a string, therefore I use INT to convert it to a number
print ('thanks! Of course I knew that!')
myage = input('can you guess how old I am?')
myage = int(myage) 
years_until_hundred = 100 - myage #calculating how many years left until I turn 100
print ('thats right! And in',years_until_hundred + year,'I will be a hundred years old!')

