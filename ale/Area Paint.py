#Just try to get all the things you need to finish this
height = input('What is the height of the room you want to paint, in feet? ')
height = int(height)
width = input('What is the width of the room you want to pain, in feet? ')
width = int(width)
lengh = input('what is the lengh of the room you want to paint, in feet? ')
lengh = int(lengh)
num_of_windows = input('How many windows are in the room you want to feet? ')
num_of_windows = int(num_of_windows)
num_of_doors = input('How many doors are in the room you want to feet? ')
num_of_doors = int(num_of_doors)


wall_area = ((2*lengh*height)+(2*width*height))
wall_area = int(wall_area)
no_paint_area = ((20*num_of_doors)+(15*num_of_windows))
no_paint_area = int(no_paint_area)
paint_area = (wall_area-no_paint_area)
print('The area you want to paint is' , paint_area,'in feet.')

gallons_to_wall_area = (round(paint_area/350, 2))
                        
print('You will need', gallons_to_wall_area,'gallons to paint the room.')

