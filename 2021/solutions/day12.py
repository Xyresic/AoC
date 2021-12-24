def add_to_dict(key, value, dict):
    if key not in dict:
        dict[key] = set()
    if key != 'end' and value != 'start':
        dict[key].add(value)

with open('../inputs/input12.txt', 'r') as f:
    data = [s.strip().split('-') for s in f.readlines()]
    connections = {}
    for line in data:
        add_to_dict(line[0], line[1], connections)
        add_to_dict(line[1], line[0], connections)

    paths = []
    paths_deeper = []
    to_explore = {('start',): True}
    while to_explore:
        next_layer = {}
        for path in to_explore:
            cave = path[-1]
            for neighbor in connections[cave]:
                new_path = path + (neighbor,)
                if neighbor == 'end':
                    if to_explore[path]:
                        paths.append(new_path)
                    paths_deeper.append(new_path)
                else:
                    if not (neighbor.islower() and neighbor in path):
                        next_layer[new_path] = to_explore[path]
                    elif to_explore[path]:
                        next_layer[new_path] = False
        to_explore = next_layer

    # part 1
    print(len(paths))

    # part 2
    print(len(paths_deeper))
