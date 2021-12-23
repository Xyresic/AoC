def is_valid(i, j, di, dj, data):
    return (not (di == 0 and dj == 0)) and (0 <= i < len(data)) and (0 <= j < len(data[0]))

with open('../inputs/input11.txt', 'r') as f:
    data = [[int(c) for c in s.strip()] for s in f.readlines()]

    count = 0
    step = 0
    while True:
        step += 1
        to_flash = set()
        flashed = set()
        for i, row in enumerate(data):
            for j, num in enumerate(row):
                data[i][j] += 1
                if num == 9:
                    to_flash.add((i, j))
        while to_flash:
            next_flash = set()
            for oct in to_flash:
                count += 1
                flashed.add(oct)
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ni = oct[0] + di
                        nj = oct[1] + dj
                        if is_valid(ni, nj, di, dj, data):
                            data[ni][nj] += 1
                            if (ni, nj) not in flashed and (ni, nj) not in to_flash and data[ni][nj] > 9:
                                next_flash.add((ni, nj))
            to_flash = next_flash
        if len(flashed) == len(data) * len(data[0]):
            # part 2
            print(step)
            break
        for oct in flashed:
            data[oct[0]][oct[1]] = 0

        # part 1
        if step == 100:
            print(count)
