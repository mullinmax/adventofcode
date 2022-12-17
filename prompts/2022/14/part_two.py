
import sys
with open(sys.argv[1]) as f:
    lines = f.readlines()
    coordinates_sets = [[[int(c.split(',')[0]),int(c.split(',')[1])] for c in line.split(' -> ')] for line in lines]

    print(coordinates_sets[0][0])

    walls = set()

    for coordinate_set in coordinates_sets:
        for i in range(len(coordinate_set)-1):
            start = coordinate_set[i]
            end = coordinate_set[i+1]
            for col in range(min(start[1], end[1]), max(start[1], end[1])+1):
                for row in range(min(start[0], end[0]), max(start[0], end[0])+1):
                    walls.add((row, col))

    print(walls)
    bottom = max([w[1] for w in walls])+3
    rows = []
    rows.append(set())
    rows[-1].add((500, 0))
    while len(rows) < bottom:
        new_row = set()
        for sand in rows[-1]:
            left = (sand[0]-1, sand[1]+1)
            down = (sand[0], sand[1]+1)
            right = (sand[0]+1, sand[1]+1)
            if left not in walls:
                new_row.add(left)
            if down not in walls:
                new_row.add(down)
            if right not in walls:
                new_row.add(right)
        rows.append(new_row)


    min_row = min(min([min([s[1] for s in row]) for row in rows]), min([w[1] for w in walls]))
    min_col = min(min([min([s[0] for s in row]) for row in rows]), min([w[0] for w in walls]))
    max_row = max(max([max([s[1] for s in row]) for row in rows]), max([w[1] for w in walls]))
    max_col = max(max([max([s[0] for s in row]) for row in rows]), max([w[0] for w in walls]))
    
    count = 0
    for r in range(min_row, max_row):
        s = ''
        for c in range(min_col-1, max_col+2):
            if (c, r) in rows[r]:
                s += 'o'
                count += 1
            elif (c, r) in walls:
                s +='#'
            else:
                s += '.'
        
        print(s)
    print(count)




    # for x in range(len(cave)):
    #     print(''.join(cave[x]))


    # # Start at source of sand
    # source = [0, 500-offset[0]]
    # total_sand = 0
    # current_pos = source
    # while True:  # while current position is not bottom of cave
    #     try:
    #         below_pos = [current_pos[0]+1, current_pos[1]]
    #         left_pos = [below_pos[0], below_pos[1]-1]  
    #         right_pos = [below_pos[0], below_pos[1]+1] 
            
    #         # print(left_pos, below_pos, right_pos)
    #         # print(left_pos, cave[left_pos[0]][left_pos[1]]) 
    #         # print(below_pos, cave[below_pos[0]][below_pos[1]])
    #         # print(right_pos, cave[right_pos[0]][right_pos[1]])
            
    #         if below_pos[0] >= len(cave[0])-1: # hit floor on the bottom
    #             total_sand += 1
    #             cave[current_pos[0]][current_pos[1]] = 'o'
    #             current_pos = source

    #         elif cave[below_pos[0]][below_pos[1]] == '.':  # if tile below is air drop one
    #             # print('going down', below_pos, cave[below_pos[0]][below_pos[1]])
    #             cave[current_pos[0]][current_pos[1]] = '.'
    #             current_pos = below_pos

    #         elif left_pos[1] < 0: # if you fall off the map to the left
    #             # print('fell off left')
    #             # print(left_pos, below_pos, right_pos)
    #             # print(left_pos, cave[left_pos[0]][left_pos[1]]) 
    #             # print(below_pos, cave[below_pos[0]][below_pos[1]])
    #             cave = [row+['.'] for row in cave]
    #             cave[current_pos[0]][current_pos[1]] = '.'
    #             current_pos = left_pos

    #         elif cave[left_pos[0]][left_pos[1]] == '.':
    #             # print('going left', left_pos, cave[left_pos[0]][left_pos[1]])
    #             cave[current_pos[0]][current_pos[1]] = '.'
    #             current_pos = left_pos

    #         elif right_pos[1] > len(cave[0])-1: # if you fall off the map to the right
    #             # print('fell off right', size[1]-1)
    #             # print(left_pos, below_pos, right_pos)
    #             # print(left_pos, cave[left_pos[0]][left_pos[1]]) 
    #             # print(below_pos, cave[below_pos[0]][below_pos[1]])
    #             # print(right_pos, cave[right_pos[0]][right_pos[1]])
    #             cave = [['.']+row for row in cave]
    #             cave[current_pos[0]][current_pos[1]] = '.'
    #             current_pos = right_pos

    #         elif cave[right_pos[0]][right_pos[1]] == '.':
    #             # print('going right', right_pos, cave[right_pos[0]][right_pos[1]])
    #             cave[current_pos[0]][current_pos[1]] = '.'
    #             current_pos = right_pos

    #         else: # no where to go
    #             print()
    #             for x in range(len(cave)):
    #                 print(''.join(cave[x]))
    #             if current_pos[0] == source[0] and current_pos[1] == source[1]:
    #                 break
    #             total_sand += 1 
    #             cave[current_pos[0]][current_pos[1]] = 'o'
    #             current_pos = source
    #         cave[current_pos[0]][current_pos[1]] = 'X'
    #         # for x in range(len(cave)):
    #         #     print(''.join(cave[x]))
    #     except:
    #         print(current_pos)
    #         print(left_pos, below_pos, right_pos)
    #         print(left_pos, cave[left_pos[0]][left_pos[1]]) 
    #         print(below_pos, cave[below_pos[0]][below_pos[1]])
    #         print(right_pos, cave[right_pos[0]][right_pos[1]])
    #         raise Exception()
    # for x in range(len(cave)):
    #     print(''.join(cave[x]))
        
    # print(total_sand)