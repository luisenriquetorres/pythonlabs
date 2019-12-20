# Restaurant bill and tip calculator
# ==================================
# This program will find the bill and tip for each person
# when a number of people go to a restaurant and eat.

#first we'll get the bill amount
total_bill = input ('How much was the total bill in dollars? $')

#We need this to be an integer, so we convert using INT
total_bill = int(total_bill)

#now let's get the percentage
tip_percentage = input ('What percentage is the tip? ')
tip_percentage = int(tip_percentage)

#finally, the number of people who had the meal
num_people = input('How many people are we dividing this bill between? ')
num_people = int(num_people)

#now for the calculations! First, let's divide the bill
bill_per_person = total_bill / num_people
print ('Each person will pay', bill_per_person, 'dollars for the food')

#now let's get the tip. Remember that the percentage is divided by 100!
tip_per_person = bill_per_person * tip_percentage / 100
print ('and will pay', tip_per_person,' dollars for the tip')

#finally, total bill plus tip.
total_bill_and_tip = total_bill + tip_per_person*num_people
print ('for a total bill of', total_bill_and_tip,'dollars!')
