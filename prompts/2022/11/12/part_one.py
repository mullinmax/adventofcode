
import sys
with open(sys.argv[1]) as f:
    lines = f.readlines()

height_map = []
for line in lines:
    height_map.append(list(line.strip()))

start_positions = []
end_pos = None
for row in range(len(height_map)):
    for col in range(len(height_map[row])):
        if height_map[row][col] == 'a':
            start_positions.append([row, col])
        if height_map[row][col] == 'S':
            start_positions.append([row, col])
            height_map[row][col] = 'a'
        elif height_map[row][col] == 'E':
            print('mapped end')
            end_pos = [row, col]
            height_map[row][col] = ['z', 0]

print(height_map[end_pos[0]][end_pos[1]])
recently_updated = [end_pos]
while len(recently_updated) > 0:
    next_recently_updated = []
    for poi in recently_updated:
        print(f'checking {poi}')
        rows = [poi[0]]
        cols = [poi[1]]
        if poi[0] > 0:
            rows.append(poi[0] - 1)
        if poi[0] < len(height_map)-1:
            rows.append(poi[0] + 1)
        if poi[1] > 0:
            cols.append(poi[1] - 1)
        if poi[1] < len(height_map[0])-1:
            cols.append(poi[1] + 1)
        for row in rows:
            for col in cols:
                if (row != poi[0] or col != poi[1]) and (row == poi[0] or col == poi[1]): # don't check yourself and no diagonals
                    print(f'    moving to {row},{col}')
                    if len(height_map[row][col]) == 1 or height_map[row][col][1] > height_map[poi[0]][poi[1]][1]+1: # if it hasn't been visited or the path can be improved
                        print(f'        checking diff {row},{col}')
                        if ord(height_map[row][col])-ord(height_map[poi[0]][poi[1]][0]) >= -1: # if the height is within 1 diff
                            height_map[row][col] = [height_map[row][col], height_map[poi[0]][poi[1]][1]+1]
                            print(f'        adding {row},{col}')
                            next_recently_updated.append([row, col])
        recently_updated = next_recently_updated


# for row in range(len(height_map)):
#     for col in range(len(height_map[row])):
#         if row == start_pos[0] and col == start_pos[1]:
#             print(' ', end='')
#         elif len(height_map[row][col]) > 1:
#             print(height_map[row][col][0].upper(), end='')
#         else:
#             print(height_map[row][col][0], end='')
#     print()

# for row in range(len(height_map)):
#         print([h[-1] if isinstance(h[-1], int) else ' ' for h in height_map[row]])

print(min([height_map[s_pos[0]][s_pos[1]][1] for s_pos in start_positions if isinstance(height_map[s_pos[0]][s_pos[1]][-1], int)]))
# print(height_map[start_pos[0]][start_pos[1]])


# def find_shortest_path(heightmap):
#     path = []
#     visited = []
#     current_position = 'S'
#     while current_position != 'E':
#         adjacent_squares = get_adjacent_squares(heightmap, current_position)
#         adjacent_heights = get_adjacent_heights(heightmap, adjacent_squares)
#         min_height_index = adjacent_heights.index(min(adjacent_heights))
#         new_position = adjacent_squares[min_height_index]
#         path.append(new_position)
#         visited.append(new_position)
#         current_position = new_position
#     return path

# def get_adjacent_squares(heightmap, position):
#     x, y = map(int, position.split(','))
#     adjacent_squares = []
#     if x > 0: adjacent_squares.append(f'{x-1},{y}')
#     if x < len(heightmap[0])-1: adjacent_squares.append(f'{x+1},{y}')
#     if y > 0: adjacent_squares.append(f'{x},{y-1}')
#     if y < len(heightmap)-1: adjacent_squares.append(f'{x},{y+1}')
#     return adjacent_squares

# def get_adjacent_heights(heightmap, adjacent_squares):
#     adjacent_heights = []
#     for square in adjacent_squares:
#         x, y = map(int, square.split(','))
#         adjacent_heights.append(heightmap[y][x])
#     return adjacent_heights

# path = find_shortest_path(heightmap)
# print('->'.join(path))