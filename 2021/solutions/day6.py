with open('../inputs/input6.txt', 'r') as f:
    data = f.read()
    counts = {i: data.count(str(i)) for i in range(9)}

    days = 256
    for _ in range(days):
        to_birth = counts[0]
        for i in range(8):
            counts[i] = counts[i + 1]
        counts[6] += to_birth
        counts[8] = to_birth
        # part 1
        if _ == 79:
            print(sum(counts.values()))

    # part 2
    print(sum(counts.values()))
