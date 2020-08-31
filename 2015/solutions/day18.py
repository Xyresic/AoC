with open('../inputs/input18.txt', 'r') as f:
    data = f.readlines()
    grid = [list(line.strip()) for line in data]
    corners = ((0, 0), (0, 99), (99, 0), (99, 99))

    def is_on(y, x):
        try:
            if y < 0:
                return False
            if x < 0:
                return False
            return grid[y][x] == '#'
        except IndexError:
            return False

    def run_conway(part_two=False):
        global grid
        for i in range(100):
            nextGrid = [[None] * 100 for j in range(100)]
            for y in range(100):
                for x in range(100):
                    if part_two and (y, x) in corners:
                        nextGrid[y][x] = '#'
                        continue
                    neighborsOn = 0
                    if is_on(y - 1, x - 1):
                        neighborsOn += 1
                    if is_on(y - 1, x):
                        neighborsOn += 1
                    if is_on(y - 1, x + 1):
                        neighborsOn += 1
                    if is_on(y, x - 1):
                        neighborsOn += 1
                    if is_on(y, x + 1):
                        neighborsOn += 1
                    if is_on(y + 1, x - 1):
                        neighborsOn += 1
                    if is_on(y + 1, x):
                        neighborsOn += 1
                    if is_on(y + 1, x + 1):
                        neighborsOn += 1
                    if is_on(y, x) and neighborsOn == 2 or neighborsOn == 3:
                        nextGrid[y][x] = '#'
                    else:
                        nextGrid[y][x] = '.'
            grid = [row for row in nextGrid]
        return sum(grid, []).count('#')

    # part one
    print(run_conway())

    # part two
    grid = [list(line.strip()) for line in data]
    grid[0][0] = '#'
    grid[0][99] = '#'
    grid[99][0] = '#'
    grid[99][99] = '#'
    print(run_conway(True))
