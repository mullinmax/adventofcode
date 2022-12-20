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
    # v_dict = {v.name:v for v in valves}
    # valves = v_dict
    
    for v in valves:
        print(v)

    # valve_order = [v.name for k, v in valves.items()]
    valves.sort(key=lambda x: x.name)
    valve_id_lkp = [v.name for v in valves]
    print(valve_id_lkp)
    
    for valve in valves:
        valve.con_ids = [valve_id_lkp.index(c) for c in valve.connections]
    
    print(valves[0].con_ids)

    graph = []
    for valve in valves:
        row = [ 1 if i in valve.con_ids else 0 for i in range(len(valves)) ]
        graph.append(row)
        print(row)

    size = len(graph)
    changes = True
    while changes:
        changes = False
        for valve in range(size): # for each valve
            for con_id in range(size): # iterate over it's connections
                if graph[valve][con_id] > 0:
                    for cons_con_id in range(size): # iterate over their connections
                        if valve != cons_con_id and graph[con_id][cons_con_id] > 0:
                            if graph[valve][cons_con_id] == 0:
                                print(f'{valve_id_lkp[valve]} connects to {valve_id_lkp[cons_con_id]} via {valve_id_lkp[con_id]} in {graph[con_id][cons_con_id] + graph[valve][con_id]} steps')
                                graph[valve][cons_con_id] = graph[con_id][cons_con_id] + graph[valve][con_id]
                                changes = True
                            elif graph[valve][cons_con_id] > graph[con_id][cons_con_id] + graph[valve][con_id]:
                                print(f'{valve_id_lkp[valve]} shorter route to {valve_id_lkp[cons_con_id]} via {valve_id_lkp[con_id]} in {graph[con_id][cons_con_id] + graph[valve][con_id]} steps down from {graph[valve][cons_con_id]}')
                                graph[valve][cons_con_id] = graph[con_id][cons_con_id] + graph[valve][con_id]
                                changes = True

    print('\nstandard graph')
    for row in graph:
        print(row)

    non_zero_valves = [valves[0]] + [v for v in valves if v.rate > 0]
    non_zero_valves.sort(key=lambda x: x.name)
    print(non_zero_valves)
    non_zero_valve_ids = [valve_id_lkp.index(v.name) for v in non_zero_valves]
    print(non_zero_valve_ids)
    simple_graph = []
    for row in range(size):
        if row in non_zero_valve_ids:
            simple_graph.append([graph[row][col] for col in non_zero_valve_ids])

    print('\nsimple graph')
    for row in range(len(simple_graph)):
        print(f'{valve_id_lkp[non_zero_valve_ids[row]]} {simple_graph[row]}')

    # with open('diagram.puml', 'w') as f:
    #     f.write('@startuml\n')
    #     f.write('[*] -> AA\n')
    #     for v_id in non_zero_valve_ids:
    #         f.write(f'{valves[v_id].name} : {valves[v_id].rate}\n')

    #     for row in range(len(simple_graph)):
    #         for col in range(row, len(simple_graph)):
    #             if simple_graph[row][col] > 0:
    #                 f.write(f'{non_zero_valves[row].name} --> {non_zero_valves[col].name} : {simple_graph[row][col]}\n')

    #     f.write('@enduml')

    def dfs(graph, location, visited, pressure_rate, total_pressure, time_remaining, score_to_beat):
        options = [i for i, t in enumerate(graph[location]) if i not in visited and t < time_remaining]

        if len(options) == 0:
            return total_pressure + pressure_rate*time_remaining

        for option in options:
            time_for_option = 1 + graph[location][option]
            score = dfs(
                graph, 
                option, 
                visited + [option], 
                pressure_rate + non_zero_valves[option].rate, 
                total_pressure + pressure_rate * time_for_option, 
                time_remaining - time_for_option, 
                score_to_beat
            )
            if score > score_to_beat:
                score_to_beat = score
        return score_to_beat


    print(dfs(
        graph = simple_graph, 
        location = 0,
        visited = [0], 
        pressure_rate = 0, 
        total_pressure = 0, 
        time_remaining = 30,
        score_to_beat = 0    
    ))
        

# Find the source valve (AA)
# source = valves['AA']

# maximum_pressure_rate = sum([valves[v].rate for v in valves])

# def explore(time_remaining, location, open_valves, pressure_rate, total_pressure, all_valves):
#     if time_remaining <= 0 and pressure_rate < maximum_pressure_rate:
#         return (total_pressure, location, open_valves) 
#     # baseline no action
#     best_result = (total_pressure + pressure_rate, location, open_valves)
#     # try opening valve
#     if location not in open_valves and all_valves[location].rate > 0:
#         new_open_valves = open_valves.copy()
#         new_open_valves.add(location)
#         results = explore(
#             time_remaining-1, 
#             location, 
#             new_open_valves, 
#             pressure_rate + all_valves[location].rate,
#             total_pressure + pressure_rate,
#             all_valves
#         )
#         if results[0] > best_result[0]:
#             best_result = results
    
#     # try each path
#     for tunnel in all_valves[location].connections:
#         results = explore(
#             time_remaining-1, 
#             tunnel, 
#             open_valves.copy(), 
#             pressure_rate,
#             total_pressure + pressure_rate,
#             all_valves
#         )
#         if results[0] > best_result[0]:
#             best_result = results
#     return best_result


# print(explore(30,'AA', set(), 0, 0, valves))