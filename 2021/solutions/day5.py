def add_coord(grid, pos, axial):
    coord = (pos[0], pos[1])
    if coord not in grid:
        grid[coord] = [0, 0]
    counts = grid[coord]
    counts[1] += 1
    if axial:
        counts[0] += 1

with open('../inputs/input5.txt', 'r') as f:
    data = [[[int(c) for c in p.split(',')] for p in s.strip().split(' -> ')] for s in f.readlines()]
    grid = {}

    for line in data:
        pos = line[0]
        end = line[1]
        dx = end[0] - pos[0]
        dy = end[1] - pos[1]
        dx = 0 if dx == 0 else 1 if dx > 0 else -1
        dy = 0 if dy == 0 else 1 if dy > 0 else -1
        axial = pos[0] == end[0] or pos[1] == end[1]
        while pos != end:
            add_coord(grid, pos, axial)
            pos[0] += dx
            pos[1] += dy
        add_coord(grid, pos, axial)

    # part 1
    print(len([key for key, item in grid.items() if item[0] >= 2]))

    # part 2
    print(len([key for key, item in grid.items() if item[1] >= 2]))
