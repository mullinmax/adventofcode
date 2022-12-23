
import sys
with open(sys.argv[1]) as f:
    coordinates = f.read().splitlines()

    # Create a list to store the x,y,z coordinates of each cube
    cubes = {}
    for coordinate in coordinates:
        x, y, z = coordinate.split(',')
        cubes[f'{x}-{y}-{z}'] = [int(x), int(y), int(z)]
    
    # Create a variable to store the surface area 
    surface_area = 0

    # Iterate through the list of cubes
    for key, (x, y, z) in cubes.items():
        all_sides = [
            f'{x+1}-{y}-{z}',
            f'{x-1}-{y}-{z}',
            f'{x}-{y+1}-{z}',
            f'{x}-{y-1}-{z}',
            f'{x}-{y}-{z+1}',
            f'{x}-{y}-{z-1}'
        ]
        surface_area += len([side for side in all_sides if side not in cubes])

print(surface_area)