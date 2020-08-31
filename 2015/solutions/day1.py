with open('../inputs/input1.txt', 'r') as f:
    data = f.read()

    # part one
    print(data.count('(') - data.count(')'))

    # part two
    pos = 1
    floor = 0
    for c in data:
        if c == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print(pos)
            break
        pos += 1
