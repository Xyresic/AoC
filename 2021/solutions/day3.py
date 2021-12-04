with open('../inputs/input3.txt', 'r') as f:
    data = [[int(c) for c in s.strip()] for s in f.readlines()]

    gamma = ''
    length = len(data[0])
    total = len(data)
    counts = [0] * length
    for i in range(length):
        counts[i] = sum(n[i] for n in data)
        gamma += '1' if counts[i] >= total / 2 else '0'
    gamma = int(gamma, base=2)

    # part 1
    print(gamma * (2 ** length - 1 - gamma))

    o2_candidates = [n.copy() for n in data]
    co2_candidates = [n.copy() for n in data]
    i = 0
    while len(o2_candidates) > 1 or len(co2_candidates) > 1:
        if len(o2_candidates) > 1:
            count = sum(n[i] for n in o2_candidates)
            match = 1 if count >= len(o2_candidates) / 2 else 0
            o2_candidates = [n for n in o2_candidates if n[i] == match]
        if len(co2_candidates) > 1:
            count = sum(n[i] for n in co2_candidates)
            match = 0 if count >= len(co2_candidates) / 2 else 1
            co2_candidates = [n for n in co2_candidates if n[i] == match]
        i += 1

    # part 2
    o2 = int(''.join([str(i) for i in o2_candidates[0]]), base=2)
    co2 = int(''.join([str(i) for i in co2_candidates[0]]), base=2)
    print(o2 * co2)
