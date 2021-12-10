from math import prod

def is_valid(i, j, di, dj, data):
    return (abs(di) ^ abs(dj)) and (0 <= i < len(data)) and (0 <= j < len(data[0]))

with open('../inputs/input9.txt', 'r') as f:
    data = [[int(s) for s in list(line.strip())] for line in f.readlines()]

    risks = 0
    lows = []
    for i, line in enumerate(data):
        for j, num in enumerate(line):
            is_min = True
            for di in range(-1, 2):
                if not is_min:
                    break
                for dj in range(-1, 2):
                    ni = i + di
                    nj = j + dj
                    if is_valid(ni, nj, di, dj, data) and data[ni][nj] <= num:
                        is_min = False
                        break
            if is_min:
                lows.append((i, j))
                risks += num + 1

    # part 1
    print(risks)

    basin_sizes = []
    for low in lows:
        to_expand = {low}
        visited = {low}
        while to_expand:
            next_layer = set()
            for point in to_expand:
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ni = point[0] + di
                        nj = point[1] + dj
                        neighbor = (ni, nj)
                        if is_valid(ni, nj, di, dj, data) and neighbor not in visited and data[ni][nj] != 9:
                            next_layer.add(neighbor)
                            visited.add(neighbor)
            to_expand = next_layer
        basin_sizes.append(len(visited))

    # part 2
    print(prod(sorted(basin_sizes)[-3:]))
