from re import search

with open('../inputs/input16.txt') as f:
    data = f.readlines()

    def find_sue(part_one=True):
        for line in data:
            if 'children' in line and search(r'(?<=children: )\d+', line)[0] != '3':
                continue
            if 'cats' in line:
                cats = int(search(r'(?<=cats: )\d+', line)[0])
                if cats != 7 if part_one else cats <= 7:
                    continue
            if 'samoyeds' in line and search(r'(?<=samoyeds: )\d+', line)[0] != '2':
                continue
            if 'pomeranians' in line:
                poms = int(search(r'(?<=pomeranians: )\d+', line)[0])
                if poms != 3 if part_one else poms >= 3:
                    continue
            if 'akitas' in line and search(r'(?<=akitas: )\d+', line)[0] != '0':
                continue
            if 'vizslas' in line and search(r'(?<=vizslas: )\d+', line)[0] != '0':
                continue
            if 'goldfish' in line:
                goldfish = int(search(r'(?<=goldfish: )\d+', line)[0])
                if goldfish != 5 if part_one else goldfish >= 5:
                    continue
            if 'trees' in line:
                trees = int(search(r'(?<=trees: )\d+', line)[0])
                if trees != 3 if part_one else trees <= 3:
                    continue
            if 'cars' in line and search(r'(?<=cars: )\d+', line)[0] != '2':
                continue
            if 'perfumes' in line and search(r'(?<=perfumes: )\d+', line)[0] != '2':
                continue
            return line[:-1]

    # part one
    print(find_sue())

    # part two
    print(find_sue(False))
