with open('../inputs/input8.txt', 'r') as f:
    data = [[set(s) for s in line.strip().split(' ')] for line in f.readlines()]
    for entry in data:
        entry.remove({'|'})

    count = 0
    valid = {2, 3, 4, 7}
    for entry in data:
        for num in entry[-4:]:
            if len(num) in valid:
                count += 1

    output = 0
    for entry in data:
        this_output = ''
        mapping = {i: set() for i in range(10)}
        mapping[1] = [n for n in entry if len(n) == 2][0]
        mapping[4] = [n for n in entry if len(n) == 4][0]
        mapping[7] = [n for n in entry if len(n) == 3][0]
        mapping[8] = [n for n in entry if len(n) == 7][0]
        mapping[3] = [n for n in entry if len(n) == 5 and len(n & mapping[1]) == 2][0]
        mapping[2] = [n for n in entry if len(n) == 5 and len(n & mapping[4]) == 2][0]
        mapping[6] = [n for n in entry if len(n) == 6 and len(n & mapping[1]) == 1][0]
        mapping[5] = [n for n in entry if len(n) == 5 and len(n & mapping[6]) == 5][0]
        mapping[9] = [n for n in entry if len(n) == 6 and len(n & mapping[4]) == 4][0]
        mapping[0] = [n for n in entry if len(n) == 6 and len(n & mapping[5]) == 4][0]
        for num in entry[-4:]:
            for key, value in mapping.items():
                if num == value:
                    this_output += str(key)
                    break
        output += int(this_output)

    # part 1
    print(count)

    # part 2
    print(output)

