class valve():
    def __init__(self, raw_str):
        self.name = raw_str.split(' ')[1]
        self.rate = int(raw_str.split(' ')[4].split('=')[-1][:-1])
        self.connections = [c.strip() for c in raw_str.split('lead to valves ')[-1].split(', ')]
    
    def __str__(self):
        return f'{self.name}:{self.rate}->{self.connections}'

import sys
with open(sys.argv[1]) as f:
    valves = [valve(line) for line in f.readlines()]
    v_dict = {v.name:v for v in valves}
    valves = v_dict
    
    for v in valves:
        print(valves[v])

# Find the source valve (AA)
source = valves['AA']

maximum_pressure_rate = sum([valves[v].rate for v in valves])

def explore(time_remaining, location, open_valves, pressure_rate, total_pressure, all_valves):
    if time_remaining <= 0 and pressure_rate < maximum_pressure_rate:
        return (total_pressure, location, open_valves) 
    # baseline no action
    best_result = (total_pressure + pressure_rate, location, open_valves)
    # try opening valve
    if location not in open_valves and all_valves[location].rate > 0:
        new_open_valves = open_valves.copy()
        new_open_valves.add(location)
        results = explore(
            time_remaining-1, 
            location, 
            new_open_valves, 
            pressure_rate + all_valves[location].rate,
            total_pressure + pressure_rate,
            all_valves
        )
        if results[0] > best_result[0]:
            best_result = results
    
    # try each path
    for tunnel in all_valves[location].connections:
        results = explore(
            time_remaining-1, 
            tunnel, 
            open_valves.copy(), 
            pressure_rate,
            total_pressure + pressure_rate,
            all_valves
        )
        if results[0] > best_result[0]:
            best_result = results
    return best_result


print(explore(30,'AA', set(), 0, 0, valves))