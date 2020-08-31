from itertools import permutations

with open('../inputs/input13.txt', 'r') as f:
    data = f.readlines()

    def find_best():
        paths = []
        people = len(adjacency) - 1
        for perm in list(permutations(range(people + 1))):
            happiness = 0
            for i in range(people):
                happiness += adjacency[perm[i]][perm[i + 1]]
                happiness += adjacency[perm[i + 1]][perm[i]]
            happiness += adjacency[perm[people]][perm[0]]
            happiness += adjacency[perm[0]][perm[people]]
            paths.append(happiness)
        return max(paths)

    # part one
    hash = {'Alice': 0,
            'Bob': 1,
            'Carol': 2,
            'David': 3,
            'Eric': 4,
            'Frank': 5,
            'George': 6,
            'Mallory': 7}

    adjacency = [[0] * 8 for i in range(8)]
    for line in data:
        parsed = line.split()
        val = int(parsed[3]) if parsed[2] == 'gain' else -int(parsed[3])
        adjacency[hash[parsed[0]]][hash[parsed[-1][:-1]]] = val
    print(find_best())

    # part two
    for row in adjacency:
        row.append(0)
    adjacency.append([0] * 8)
    print(find_best())
