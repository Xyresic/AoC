with open('../inputs/input23.txt') as f:
    data = f.readlines()

    def process_instructions(part_one=True):
        a = 0 if part_one else 1
        b = 0
        ind = 0
        while 0 <= ind < len(data):
            if 'inc' in data[ind]:
                if 'a' in data[ind]:
                    a += 1
                else:
                    b += 1
            elif 'tpl' in data[ind]:
                a *= 3
            elif 'hlf' in data[ind]:
                a /= 2
            elif 'jmp' in data[ind]:
                ind += int(data[ind].split()[1])
                continue
            elif 'jie' in data[ind]:
                if a % 2 == 0:
                    ind += int(data[ind].split()[2])
                    continue
            else:
                if a == 1:
                    ind += int(data[ind].split()[2])
                    continue
            ind += 1
        return b

    # part one
    print(process_instructions())

    # part two
    print(process_instructions(False))
