from re import findall
from json import loads

with open('../inputs/input12.json', 'r') as f:
    data = f.read()

    # part one
    print(sum([int(num)for num in findall(r'-?\d+', data)]))

    # part two
    def parse(j):
        if isinstance(j, int):
            return j
        if isinstance(j, str):
            return 0
        if isinstance(j, list):
            return sum([parse(l) for l in j])
        if isinstance(j, dict):
            if 'red' in j.values():
                return 0
            else:
                return sum([parse(v) for v in j.values()])

    print(parse(loads(data)))
