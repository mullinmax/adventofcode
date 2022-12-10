
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

def ltr_senic_score(r, c, grid):
    if c + 1 == len(grid[r]): # if we're on the edge return 0 distance
        return 0

    visable_dist = 1
    while c + visable_dist < len(grid[r])-1 and grid[r][c+visable_dist] < grid[r][c]:
        visable_dist += 1
    
    return visable_dist

            

import sys
with open(sys.argv[1]) as f:
    grid = []
    
    for row in f.readlines():
        grid.append([int(cell) for cell in row.strip()])
    
    senic_score = []
    for row in grid:
        s_row = []
        for cell in row:
            s_row.append(1)
        senic_score.append(s_row)
    #right
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            senic_score[r][c] *= ltr_senic_score(r, c, grid)
    grid = rotate(grid)
    senic_score = rotate(senic_score)
    #up
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            senic_score[r][c] *= ltr_senic_score(r, c, grid)
    grid = rotate(grid)
    senic_score = rotate(senic_score)
    # left
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            senic_score[r][c] *= ltr_senic_score(r, c, grid)            
    grid = rotate(grid)
    senic_score = rotate(senic_score)
    # down
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            senic_score[r][c] *= ltr_senic_score(r, c, grid)
    grid = rotate(grid)
    senic_score = rotate(senic_score)

    for row in senic_score:
        print(row)

    print()
    print(max([max(row) for row in senic_score]))