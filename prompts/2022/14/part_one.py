
import sys
with open(sys.argv[1]) as f:
    lines = f.readlines()
    coordinates_sets = [[[int(c.split(',')[0]),int(c.split(',')[1])] for c in line.split(' -> ')] for line in lines]

    print(coordinates_sets[0][0])

    min_col = min([min([c[0] for c in coordinate_set]) for coordinate_set in coordinates_sets])
    max_col = max([max([c[0] for c in coordinate_set]) for coordinate_set in coordinates_sets])
    min_row = min([min([c[1] for c in coordinate_set]) for coordinate_set in coordinates_sets])
    max_row = max([max([c[1] for c in coordinate_set]) for coordinate_set in coordinates_sets])
    print(min_col, max_col, min_row, max_row)


    offset = [min_col, 0]
    print('offset', offset)
    size = [max_col - min_col, max_row-offset[1]+3]
    print('size', size)
    cave = [['.' for i in range(size[0])] for i in range(size[1])]

    for coordinate_set in coordinates_sets:
        for coordinate in coordinate_set:
            coordinate[0] -= offset[0]
            coordinate[1] -= offset[1]

    # for x in range(len(cave)):
    #     print(''.join(cave[x]))

    for coordinate_set in coordinates_sets:
        for i in range(len(coordinate_set)-1):
            print(coordinate_set[i])
            if coordinate_set[i][0] != coordinate_set[i+1][0]:
                for col in range(min(coordinate_set[i][0], coordinate_set[i+1][0]), max(coordinate_set[i][0], coordinate_set[i+1][0])+1):
                    cave[coordinate_set[i][1]][col] = '#'
            if coordinate_set[i][1] != coordinate_set[i+1][1]:
                for row in range(min(coordinate_set[i][1], coordinate_set[i+1][1]), max(coordinate_set[i][1], coordinate_set[i+1][1])+1):
                    cave[row][coordinate_set[i][0]] = '#'


    for x in range(len(cave)):
        print(''.join(cave[x]))


    # Start at source of sand
    source = [0, 500-offset[0]]
    total_sand = 0
    current_pos = source
    while True:  # while current position is not bottom of cave
        try:
            below_pos = [current_pos[0]+1, current_pos[1]]
            left_pos = [below_pos[0], below_pos[1]-1]  
            right_pos = [below_pos[0], below_pos[1]+1] 
            
            # print(left_pos, below_pos, right_pos)
            # print(left_pos, cave[left_pos[0]][left_pos[1]]) 
            # print(below_pos, cave[below_pos[0]][below_pos[1]])
            # print(right_pos, cave[right_pos[0]][right_pos[1]])
            
            if below_pos[0] >= len(cave[0])-1: # hit floor on the bottom
                total_sand += 1
                cave[current_pos[0]][current_pos[1]] = 'o'
                current_pos = source

            elif cave[below_pos[0]][below_pos[1]] == '.':  # if tile below is air drop one
                # print('going down', below_pos, cave[below_pos[0]][below_pos[1]])
                cave[current_pos[0]][current_pos[1]] = '.'
                current_pos = below_pos

            elif left_pos[1] < 0: # if you fall off the map to the left
                # print('fell off left')
                # print(left_pos, below_pos, right_pos)
                # print(left_pos, cave[left_pos[0]][left_pos[1]]) 
                # print(below_pos, cave[below_pos[0]][below_pos[1]])
                cave = [row+['.'] for row in cave]
                cave[current_pos[0]][current_pos[1]] = '.'
                current_pos = left_pos

            elif cave[left_pos[0]][left_pos[1]] == '.':
                # print('going left', left_pos, cave[left_pos[0]][left_pos[1]])
                cave[current_pos[0]][current_pos[1]] = '.'
                current_pos = left_pos

            elif right_pos[1] > len(cave[0])-1: # if you fall off the map to the right
                # print('fell off right', size[1]-1)
                # print(left_pos, below_pos, right_pos)
                # print(left_pos, cave[left_pos[0]][left_pos[1]]) 
                # print(below_pos, cave[below_pos[0]][below_pos[1]])
                # print(right_pos, cave[right_pos[0]][right_pos[1]])
                cave = [['.']+row for row in cave]
                cave[current_pos[0]][current_pos[1]] = '.'
                current_pos = right_pos

            elif cave[right_pos[0]][right_pos[1]] == '.':
                # print('going right', right_pos, cave[right_pos[0]][right_pos[1]])
                cave[current_pos[0]][current_pos[1]] = '.'
                current_pos = right_pos

            else: # no where to go
                print()
                for x in range(len(cave)):
                    print(''.join(cave[x]))
                if current_pos[0] == source[0] and current_pos[1] == source[1]:
                    break
                total_sand += 1 
                cave[current_pos[0]][current_pos[1]] = 'o'
                current_pos = source
            cave[current_pos[0]][current_pos[1]] = 'X'
            # for x in range(len(cave)):
            #     print(''.join(cave[x]))
        except:
            print(current_pos)
            print(left_pos, below_pos, right_pos)
            print(left_pos, cave[left_pos[0]][left_pos[1]]) 
            print(below_pos, cave[below_pos[0]][below_pos[1]])
            print(right_pos, cave[right_pos[0]][right_pos[1]])
            raise Exception()
    for x in range(len(cave)):
        print(''.join(cave[x]))
        
    print(total_sand)