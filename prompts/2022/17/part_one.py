import sys
sequence = None
with open(sys.argv[1]) as f:
    jet_sequence = [c == '>' for c in f.read().strip()]

rock_types = [
    [
        [   # block drawing
            '####'
        ],
        [-1,-1,-1,-1], # down contact points
        [-1], # moving left contact points
        [4] # moving right contact points
    ],
    [
        [
            '.#.',
            '###',
            '.#.'
        ],
        [-2,-3,-2],
        [0, -1, 0],
        [2, 3, 2]
    ],
    [
        [
            '..#',
            '..#',
            '###'
        ],
        [-3,-3,-3],
        [1, 1, -1],
        [3, 3, 3]
    ],
    [
        [
            '#',
            '#',
            '#',
            '#'
        ],
        [-4],
        [-1, -1, -1, -1],
        [1, 1, 1, 1]
    ],
    [
        [
            '##',
            '##'
        ],
        [-2,-2],
        [-1, -1],
        [2, 2]
    ]
]


chamber_width = 7
highest_rock = 0
num_rocks = 0
chamber = [['#']*chamber_width]
chamber.append(['.']*chamber_width)
chamber.append(['.']*chamber_width)
chamber.append(['.']*chamber_width)

# print('-------')
# for row in reversed(chamber):
#     print(''.join(row))

jet_index = 0
prev_max = 0
special_rock = 0
while num_rocks < 100000:
    rock_type = num_rocks % len(rock_types)
    rock_width = len(rock_types[rock_type][0][0])
    rock_height = len(rock_types[rock_type][0])
    rock_drawing = rock_types[rock_type][0]
    rock_down_contact_points = rock_types[rock_type][1]
    rock_left_contact_points = rock_types[rock_type][2]
    rock_right_contact_points = rock_types[rock_type][3]
    rock_pos = [highest_rock + +rock_height + 3, 2]
    # expand chamber until high enough 
    while len(chamber) < rock_pos[0]+4:
        chamber.append(['.']*chamber_width)
    
    # simulate fall
    collision = False
    while not collision:
        
        # jets fire
        # print(rock_pos)
        if jet_sequence[jet_index]:
            if rock_pos[1] + rock_width < chamber_width: # move right if not hitting wall
                # print('jet right')
                movement = 1
                for row, col in enumerate(rock_right_contact_points):
                    # print(rock_pos, row, col)
                    if chamber[rock_pos[0]-row][rock_pos[1]+col] == '#':
                        # print('hitting object')
                        movement = 0
                        break
                rock_pos[1] += movement
            # else:
            #     print('hitting right wall')
        else:
            if rock_pos[1] > 0: # move left if not hitting wall
                # print('jet left')
                movement = -1
                for row, col in enumerate(rock_left_contact_points):
                    # print(rock_pos, row, col)
                    if chamber[rock_pos[0]-row][rock_pos[1]+col] == '#':
                        # print('hitting object')
                        movement = 0
                        break
                rock_pos[1] += movement
            # else:
            #     print('hitting left wall')
        jet_index += 1
        jet_index = jet_index % len(jet_sequence)
        # check if rock collides with something bellow
        if rock_pos[0] - rock_height <= highest_rock: # only bother checking if we are low enough to even collide
            for col, row in enumerate(rock_down_contact_points):
                if chamber[rock_pos[0]+row][rock_pos[1]+col] == '#':
                    collision = True
        
        if collision == False:
            rock_pos[0] -= 1
                    
    # draw rock in chamber
    # print(f'collides at {rock_pos}')
    for col in range(rock_width):
        for row in range(rock_height):
            if rock_drawing[row][col] == '#':
                chamber[rock_pos[0]-row][rock_pos[1]+col] = '#'

    # print('-------')
    # for row in reversed(chamber):
    #     print(''.join(row))

    # update highest rock
    if jet_index == 2 and num_rocks % 4 == 0:
        print(jet_index, num_rocks % 4, num_rocks, rock_pos[0]-prev_max, rock_pos[0], highest_rock)
        prev_max = rock_pos[0]
        special_rock = num_rocks + 3272
    highest_rock = max(highest_rock, rock_pos[0])
    if num_rocks == special_rock:
        print('sr', num_rocks, rock_pos[0], highest_rock)
    
    num_rocks += 1
print(num_rocks, highest_rock)
# chamber_strs = [''.join(row) for row in chamber[1000:]]
# print(chamber_ints)

# gap = 10
# not_done = True
# best_gap = gap
# best_gap_matches = 0

# while not_done and gap < len(chamber_strs):
#     not_done = False
#     for i in range(gap * 4):
#         if chamber_strs[i] != chamber_strs[i + gap]:
#             if i > best_gap_matches:
#                 best_gap = gap
#                 best_gap_matches = i
#             gap += 1
#             print(f'bad gap {gap}, {i}')
#             not_done = True
#             break
    
# print(f'best gap: {best_gap} with {best_gap_matches} matches')

# print('-------')
# for row in reversed(chamber):
#     print(''.join(row))