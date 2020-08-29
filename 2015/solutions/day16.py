import re

i = open('../inputs/input16.txt').readlines()

def find_sue(part_one=True):
    for line in i:
        if 'children' in line and re.search(r'(?<=children: )\d+', line)[0] != '3':
            continue
        if 'cats' in line:
            cats = int(re.search(r'(?<=cats: )\d+', line)[0])
            if cats != 7 if part_one else cats <= 7:
                continue
        if 'samoyeds' in line and re.search(r'(?<=samoyeds: )\d+', line)[0] != '2':
            continue
        if 'pomeranians' in line:
            poms = int(re.search(r'(?<=pomeranians: )\d+', line)[0])
            if poms != 3 if part_one else poms >= 3:
                continue
        if 'akitas' in line and re.search(r'(?<=akitas: )\d+', line)[0] != '0':
            continue
        if 'vizslas' in line and re.search(r'(?<=vizslas: )\d+', line)[0] != '0':
            continue
        if 'goldfish' in line:
            goldfish = int(re.search(r'(?<=goldfish: )\d+', line)[0])
            if goldfish != 5 if part_one else goldfish >= 5:
                continue
        if 'trees' in line:
            trees = int(re.search(r'(?<=trees: )\d+', line)[0])
            if trees != 3 if part_one else trees <= 3:
                continue
        if 'cars' in line and re.search(r'(?<=cars: )\d+', line)[0] != '2':
            continue
        if 'perfumes' in line and re.search(r'(?<=perfumes: )\d+', line)[0] != '2':
            continue
        return line[:-1]

#part one
print(find_sue())

#part two
print(find_sue(False))