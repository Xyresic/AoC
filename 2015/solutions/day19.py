from re import finditer

with open('../inputs/input19.txt') as f:
    data = f.readlines()
    med = data[-1].strip()
    replacements = [sub.strip().split() for sub in data[:-2]]

    # part one
    molecules = set()
    for rep in replacements:
        for match in finditer(rep[0], med):
            molecules.add(med[:match.start()] + rep[2] + med[match.end():])
    print(len(molecules))

    # part two
    replacements = sorted(replacements, key=lambda rep: len(rep[2]), reverse=True)

    def find_steps(mol, step):
        if mol == 'e':
            return step
        else:
            for rep in replacements:
                for match in finditer(rep[2], mol):
                    steps = find_steps(mol[:match.start()] + rep[0] + mol[match.end():], step + 1)
                    if steps != -1:
                        return steps
            return -1
    print(find_steps(med, 0))
