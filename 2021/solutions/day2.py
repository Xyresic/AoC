with open('../inputs/input2.txt', 'r') as f:
    data = [s.strip().split(' ') for s in f.readlines()]

    pos1 = 0+0j
    pos2 = 0+0j
    aim = 0
    for inst in data:
        num = int(inst[1])
        match inst[0]:
            case 'forward':
                pos1 += num
                pos2 += num
                pos2 += aim * num * 1j
            case 'down':
                pos1 += num * 1j
                aim += num
            case _:
                pos1 -= num * 1j
                aim -= num

    # part 1
    print(int(pos1.real * pos1.imag))

    # part 2
    print(int(pos2.real * pos2.imag))
