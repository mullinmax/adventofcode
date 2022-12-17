import re
import sys
with open(sys.argv[1]) as f:
	lines = [line.split(':') for line in f.readlines()]
	point_sets = [l[0].split(' ')[-2:] + l[1].strip().split(' ')[-2:] for l in lines]
	point_sets = [[int(re.sub('[xy,=]','',c)) for c in s] for s in point_sets]
	all_beacons = {(p[2], p[3]) for p in point_sets}
	all_sensors = {(p[0], p[1]) for p in point_sets}
	for c in point_sets:
		c.append(abs(c[0]-c[2])+abs(c[1]-c[3])) # add radius
	
	row = 0
	done = False
	while not done and row <= 4000000: 
		col = 0
		while col <= 4000000 and not done:
			done = True
			for p in point_sets:
				vert_dist = abs(p[1] - row)
				dist = abs(p[0] - col) + vert_dist
				if dist <= p[4]: #if within radius
					# print(p)
					col = p[0]+p[4]-vert_dist+1 # one outside of the circle of impossibility
					done = False
		if not done:
			row += 1
		print(row)
	if done:
		print(row, col)
		print(col * 4000000+row)
	else:
		print('no solution found :(')