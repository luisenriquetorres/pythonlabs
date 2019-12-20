# Hunt the Wumpus

# First let's make a 24 room maze.
num_rooms=18
exits_per_room=3

maze = [
    [5,6,1], #room0
    [0,8,2], #room1
    [1,9,3], #room2
    [2,11,4], #room3
    [3,13,5], #room4
    [0,14,4], #room5
    [0,15,7], #room6
    [6,16,8], #room7
    [7,1,9], #room8
    [8,2,10], #room9
    [9,17,11], #room10
    [12,10,3], #room11
    [13,17,11], #room12
    [14,12,4], #room13
    [5,15,13], #room14
    [6,16,14], #room15
    [15,7,16], #room16
    [16,12,10]] #room17

room_name = ['Main Gate', 'Dark Cave', 'Small Temple', 'Unknown Corridor', 'Crystal Chamber',
'Creepy Crevice', 'Slippery Slope', 'Cold Chamber', 'Freezing Room', 'Marble Chamber',
'Sandy Arena', 'Heathen Hall', 'Minion Quarters', 'Stone Sanctum', 'Mossy Quarry',
'Narrow Corridor', 'Throne Room', 'Large Temple']

player = 0

while (1==1):
    print(f'You are in the {room_name[player]}.')
    print(f'There are exits that take you to the {room_name[maze[player][0]]}, the {room_name[maze[player][1]]} and the the {room_name[maze[player][2]]}.')
    
    new_location = player
    while(new_location == player):
        new_location = input('Enter a room number to move to: ')
        new_location = int(new_location)
        if (new_location != maze[player][0] and new_location != maze[player][1] and new_location != maze[player][2]):
            print('invalid location, try again.')
            new_location = player
        else:
            print('you move to the new location.')
            player = new_location
            new_location = 19


