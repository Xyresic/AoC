with open('../inputs/input2.txt', 'r') as f:
    data = [s.strip().split(' ') for s in f.readlines()]
    pos1 = 0+0j
    pos2 = 0+0j
    aim = 0
    for inst in data:
        num = int(inst[1])
        if inst[0] == 'forward':
            pos1 += num
            pos2 += num
            pos2 += aim * num * 1j
        elif inst[0] == 'down':
            pos1 += num * 1j
            aim += num
        else:
            pos1 -= num * 1j
            aim -= num
    print(int(pos1.real * pos1.imag))
    print(int(pos2.real * pos2.imag))
