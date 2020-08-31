from itertools import permutations

with open('../inputs/input9.txt', 'r') as f:
    data = f.readlines()

    # part one
    hash = {'AlphaCentauri': 0,
            'Snowdin': 1,
            'Tambi': 2,
            'Faerun': 3,
            'Norrath': 4,
            'Straylight': 5,
            'Tristram': 6,
            'Arbre': 7}

    adjacency = [[0] * 8 for i in range(8)]
    for line in data:
        parsed = line.split()
        adjacency[hash[parsed[0]]][hash[parsed[2]]] = int(parsed[4])
        adjacency[hash[parsed[2]]][hash[parsed[0]]] = int(parsed[4])

    paths = []
    for perm in list(permutations([0, 1, 2, 3, 4, 5, 6, 7])):
        dist = 0
        for i in range(7):
            dist += adjacency[perm[i]][perm[i+1]]
        paths.append(dist)
    print(min(paths))

    # part two
    print(max(paths))
