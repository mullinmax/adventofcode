
def rotate(l):
    l_len = len(l)
    res = [[0 for x in range(l_len)] for y in range(l_len)] 
    for i in range(l_len):
        for j in range(l_len):
            res[j][l_len-1-i] = l[i][j]
    return res

def ltr_visable(grid, is_visable):
    for r, row in enumerate(grid):
        tallest = -1
        for t, tree in enumerate(row):
            if tree > tallest:
                is_visable[r][t] = 1
                tallest = tree

def ltr_viewing_score(r, c, grid):
    starting_height = grid[r][c]
    for col in range(c, len(grid[r])):
        if grid[r][col] >= starting_height:
            return col-c
            

import sys
with open(sys.argv[1]) as f:
    grid = []
    
    for row in f.readlines():
        grid.append([int(cell) for cell in row.strip()])
    
    is_visable = []
    for row in grid:
        v_row = []
        for cell in row:
            v_row.append(0)
        is_visable.append(v_row)

    ltr_visable(grid, is_visable)
    grid = rotate(grid)
    is_visable = rotate(is_visable)
    ltr_visable(grid, is_visable)
    grid = rotate(grid)
    is_visable = rotate(is_visable)
    ltr_visable(grid, is_visable)
    grid = rotate(grid)
    is_visable = rotate(is_visable)
    ltr_visable(grid, is_visable)

    is_visable[0][0] = 1
    for row in is_visable:
        print(row)
    print()
    for row in grid:
        print(row)
    print(sum(sum(is_visable, [])))
    