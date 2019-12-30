from colorama import Fore, Back, Style
def print_maze(player_location):

    rooms=[' 0',' 1',' 2',' 3', ' 4', ' 5',
        ' 6', ' 7', ' 8', ' 9', '10',
        '11', '12', '13', '14', '15',
        '16', '17']

    rooms[player_location] = Back.BLUE + rooms[player_location] + Style.RESET_ALL

    print(f'         /---{rooms[0]}---\ ')
    print(f'        /     |    \ ')
    print(f'   /---/    /{rooms[6]}\    \---\ ')
    print(f'  /        /    \        \ ')
    print(f'{rooms[5]}       {rooms[15]}     {rooms[7]}\      {rooms[1]}')
    print(f' | \--\  / \   /   \ /--/ |')
    print(f' |     {rooms[14]}    {rooms[16]}    {rooms[8]}     |')
    print(f' |      |     |     |     |')
    print(f' |     {rooms[13]}    {rooms[17]}    {rooms[9]}     |')
    print(f' | /--/ \  /   \   / \--\ |')
    print(f'{rooms[4]}       {rooms[12]}     {rooms[10]}/      {rooms[2]}')
    print(f'  \        \    /        /')
    print(f'   \---\    \\{rooms[11]}/    /---/')
    print(f'        \     |    /')
    print(f'         \---{rooms[3]}---/')

    # print('         /---00---\ ')
    # print('        /     |    \ ')
    # print('   /---/    /06\    \---\ ')
    # print('  /        /    \        \ ')
    # print('05       15     07\      01')
    # print(' | \--\  / \   /   \ /--/ |')
    # print(' |     14    16    08     |')
    # print(' |      |     |     |     |')
    # print(' |     13    17    09     |')
    # print(' | /--/ \  /   \   / \--\ |')
    # print('04       12     10/      02')
    # print('  \        \    /        /')
    # print('   \---\    \\11/    /---/')
    # print('        \     |    /')
    # print('         \---03---/')

print_maze(10)
