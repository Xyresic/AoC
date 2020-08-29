i = [list(line.strip()) for line in open('../inputs/input18.txt', 'r').readlines()]
corners = ((0, 0), (0, 99), (99, 0), (99, 99))

def is_on(y, x):
    try:
        if y < 0:
            return False
        if x < 0:
            return False
        return i[y][x] == '#'
    except IndexError:
        return False

def run_conway(part_two=False):
    global i
    for n in range(100):
        next_grid = [[None] * 100 for j in range(100)]
        for y in range(100):
            for x in range(100):
                if part_two and (y, x) in corners:
                    next_grid[y][x] = '#'
                    continue
                neighbors_on = 0
                if is_on(y - 1, x - 1):
                    neighbors_on += 1
                if is_on(y - 1, x):
                    neighbors_on += 1
                if is_on(y - 1, x + 1):
                    neighbors_on += 1
                if is_on(y, x - 1):
                    neighbors_on += 1
                if is_on(y, x + 1):
                    neighbors_on += 1
                if is_on(y + 1, x - 1):
                    neighbors_on += 1
                if is_on(y + 1, x):
                    neighbors_on += 1
                if is_on(y + 1, x + 1):
                    neighbors_on += 1
                if is_on(y, x) and neighbors_on == 2 or neighbors_on == 3:
                    next_grid[y][x] = '#'
                else:
                    next_grid[y][x] = '.'
        i = [row for row in next_grid]
    return sum(i, []).count('#')

#part one
print(run_conway())

#part two
i = [list(line.strip()) for line in open('../inputs/input18.txt', 'r').readlines()]
i[0][0] = '#'
i[0][99] = '#'
i[99][0] = '#'
i[99][99] = '#'
print(run_conway(True))