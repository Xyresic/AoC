import re

with open('../inputs/input13.txt', 'r') as f:
    data = f.read().split('\n\n')
    points = set(tuple(int(s) for s in p.split(',')) for p in data[0].split('\n'))
    folds = data[1].split('\n')

    switch = True
    for fold in folds:
        coord = int(re.search(r'\d+', fold)[0])
        new_points = set()
        ind = 0 if 'x' in fold else 1
        for point in points:
            if point[ind] > coord:
                new_point = list(point)
                new_point[ind] = 2 * coord - point[ind]
                new_points.add(tuple(new_point))
            else:
                new_points.add(point)
        points = new_points

        if switch:
            switch = False
            print(len(points))

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    grid = [['.'] * (max(xs) - min(xs) + 1) for _ in range(max(ys) - min(ys) + 1)]
    for x, y in points:
        grid[y][x] = '#'
    print('\n'.join(''.join(l) for l in grid))
