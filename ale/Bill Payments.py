#how much every person pays
#how much they pay in total
#how many people there are in total
bill_amount =input('What was the total amount you paid? ')
bill_amount = int(bill_amount)
percentage = input('What percentage would you like to tip? ')
percentage = int(percentage)
people_paying =input('How many people are here paying today? ')
people_paying =int(people_paying)
#From here on, it's no longer asking for data.
total_tip=((percentage / 100) * bill_amount)
total_bill=(bill_amount+total_tip)
final_bill=(total_bill / people_paying)

print('Your total cost will be' , final_bill, 'dollars per person.')
print('Enjoy your day.')
print('It may be your last.')
