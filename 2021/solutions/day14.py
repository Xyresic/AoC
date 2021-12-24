from math import ceil

def add_pair(pairs, pair, count):
    if pair not in pairs:
        pairs[pair] = 0
    pairs[pair] += count

def get_val(pairs):
    counts = {chr(ord('A') + i): 0 for i in range(26)}
    for pair in pairs:
        counts[pair[0]] += pairs[pair]
        counts[pair[1]] += pairs[pair]
    counts = {key: ceil(value / 2) for key, value in counts.items() if value != 0}
    return max(counts.values()) - min(counts.values())

with open('../inputs/input14.txt', 'r') as f:
    data = [s.strip().split(' ') for s in f.readlines()]
    rules = {}
    for rule in data[2:]:
        rules[rule[0]] = rule[2]

    pairs = {}
    for i in range(len(polymer := data[0][0]) - 1):
        add_pair(pairs, polymer[i:i + 2], 1)

    for step in range(40):
        new_pairs = {}
        for pair in pairs:
            if pair in rules:
                insert = rules[pair]
                add_pair(new_pairs, pair[0] + insert, pairs[pair])
                add_pair(new_pairs, insert + pair[1], pairs[pair])
        pairs = new_pairs

        # part 1
        if step == 9:
            print(get_val(pairs))

    # part 2
    print(get_val(pairs))
