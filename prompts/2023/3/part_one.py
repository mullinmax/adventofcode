
def calculate_parts(schematic: str) -> int:
    rows = schematic.split("\n")
    total = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if not rows[i][j].isdigit():
                directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    if 0 <= ni < len(rows) and 0 <= nj < len(rows[i]) and rows[ni][nj].isdigit():
                        total += int(rows[ni][nj])
    return total

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        schematic = f.read()
        print(calculate_parts(schematic))
