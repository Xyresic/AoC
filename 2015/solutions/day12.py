import re
import json

i = open('../inputs/input12.json', 'r').read()

#part one
print(sum([int(num)for num in re.findall(r'-?\d+', i)]))

#part two
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

print(parse(json.loads(i)))