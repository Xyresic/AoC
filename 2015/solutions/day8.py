with open('../inputs/input8.txt', 'r') as f:
    data = f.readlines()

    # part one
    print(sum([len(line) - len(eval(line)) - 1 for line in data]))

    # part two
    print(sum([2 + line.count('\\') + line.count('"') for line in data]))
