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

# Create a set of coordinates in the given row (y=2000000) 
impossible_points = set()
target_row = 2000000
for s in point_sets:
  # print(s)
  vert_dist = abs(s[1] - target_row)
  if vert_dist <= s[4]: #if within radius
    for i in range(s[0]-s[4]+vert_dist, s[0]+s[4]+1-vert_dist):
      impossible_points.add(i)

output = ''
count = 0
for i in range(min(impossible_points)-2, max(impossible_points)+2):
  if (i, target_row) in all_beacons:
    output += 'B'
  elif (i, target_row) in all_sensors:
    output += 'S'
  elif i in impossible_points:
    output += '#'
    count += 1
  else:
    output += '.'
# print(output)
print(count)
