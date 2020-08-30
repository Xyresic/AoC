i = open('../inputs/input23.txt').readlines()

def process_instructions(part_one=True):
    a = 0 if part_one else 1
    b = 0
    ind = 0
    while 0 <= ind < len(i):
        if 'inc' in i[ind]:
            if 'a' in i[ind]:
                a += 1
            else:
                b += 1
        elif 'tpl' in i[ind]:
            a *= 3
        elif 'hlf' in i[ind]:
            a /= 2
        elif 'jmp' in i[ind]:
            ind += int(i[ind].split()[1])
            continue
        elif 'jie' in i[ind]:
            if a % 2 == 0:
                ind += int(i[ind].split()[2])
                continue
        else:
            if a == 1:
                ind += int(i[ind].split()[2])
                continue
        ind += 1
    return b

#part one
print(process_instructions())

#part two
print(process_instructions(False))