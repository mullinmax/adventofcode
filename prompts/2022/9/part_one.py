def print_board(links):
    for y in reversed(range(-10,10)):
        for x in range(-10,10):
            print_char = '.'
            for i in range(len(links)):
                if links[i][0] == x and links[i][1] == y:
                    print_char = str(i)
                    break
            print(print_char, end='')
        print()
    print()

def print_visited(visited_positions):
    for y in reversed(range(-20,20)):
        for x in range(-20,20):
            if (x, y) in visited_positions:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

import sys
with open(sys.argv[1]) as f:
    lines = f.readlines()

commands = []
for line in lines:
    commands += line[0] * int(line.split(' ')[1])
print(commands)

def next_link_pos(tar, pos):
    x_dif = abs(tar[0] - pos[0])
    y_dif = abs(tar[1] - pos[1])
    # are they touching
    touching = x_dif <= 1 and y_dif <= 1
    
    if tar[0] == pos[0] and y_dif > 1: # same x with gap in y
        if pos[1] < tar[1]:
            pos[1] += 1
        else:
            pos[1] -= 1
    elif tar[1] == pos[1] and x_dif > 1: # same y with gap in x
        if pos[0] < tar[0]:
            pos[0] += 1
        else:
            pos[0] -= 1            
    elif not (x_dif <= 1 and y_dif <= 1): # the tar and pos aren't "touching"
        if pos[0] < tar[0]:
            pos[0] += 1   
        if pos[0] > tar[0]:
            pos[0] -= 1
        if pos[1] < tar[1]:
            pos[1] += 1
        if pos[1] > tar[1]:
            pos[1] -= 1



links = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

visited_positions = set()
visited_positions.add((0, 0))
for command in commands:
    # print_board(head_pos, tail_pos)
    # print(command)
    if command == "U":
        links[0][1] += 1
    elif command == "D":
        links[0][1] -= 1
    elif command == "L":
        links[0][0] -= 1
    elif command == "R":
        links[0][0] += 1

    for i in range(len(links)-1):
        next_link_pos((links[i]), links[i+1])

    # print_board(links)
    # input('')
    visited_positions.add((links[-1][0], links[-1][1]))
print_visited(visited_positions)
print(len(visited_positions))
# print(visited_positions)
