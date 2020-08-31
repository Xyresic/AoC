with open('../inputs/input3.txt', 'r') as f:
    data = f.read()

    # part one
    houses = [0j]
    pos = 0j
    for c in data:
        if c == '>':
            pos += 1
        elif c == '<':
            pos -= 1
        elif c == '^':
            pos += 1j
        else:
            pos -= 1j
        if pos not in houses:
            houses.append(pos)
    print(len(houses))

    # part two
    houses = [0j]
    santa = 0j
    roboSanta = 0j
    for i in range(len(data)):
        if data[i] == '>':
            delta = 1
        elif data[i] == '<':
            delta = -1
        elif data[i] == '^':
            delta = 1j
        else:
            delta = -1j
        if i % 2 == 0:
            santa += delta
            if santa not in houses:
                houses.append(santa)
        else:
            roboSanta += delta
            if roboSanta not in houses:
                houses.append(roboSanta)
    print(len(houses))
