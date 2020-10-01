from numpy import uint16

with open('../inputs/input7.txt', 'r') as f:
    data = f.readlines()

    def run_circuit(part_two=False):
        instructions = data.copy()
        copy = data.copy()
        wires = {}
        while 'a' not in wires:
            for line in instructions:
                instr = line.strip().split()
                if 'NOT' in line:
                    if instr[1] in wires:
                        wires[instr[3]] = uint16(~ wires[instr[1]])
                        copy.remove(line)
                elif 'LSHIFT' in line:
                    if instr[0] in wires:
                        wires[instr[4]] = uint16(wires[instr[0]] << int(instr[2]))
                        copy.remove(line)
                elif 'RSHIFT' in line:
                    if instr[0] in wires:
                        wires[instr[4]] = uint16(wires[instr[0]] >> int(instr[2]))
                        copy.remove(line)
                elif 'OR' in line:
                    if instr[0] in wires and instr[2] in wires:
                        wires[instr[4]] = uint16(wires[instr[0]] | wires[instr[2]])
                        copy.remove(line)
                elif 'AND' in line:
                    if instr[2] in wires:
                        if instr[0] == '1':
                            wires[instr[4]] = uint16(1 & wires[instr[2]])
                            copy.remove(line)
                        elif instr[0] in wires:
                            wires[instr[4]] = uint16(wires[instr[0]] & wires[instr[2]])
                            copy.remove(line)
                elif instr[0].isnumeric():
                    if part_two and instr[2] == 'b':
                        wires['b'] = uint16(3176)
                    else:
                        wires[instr[2]] = uint16(instr[0])
                    copy.remove(line)
                elif instr[0] in wires:
                    wires[instr[2]] = wires[instr[0]]
                    copy.remove(line)
            instructions = copy
        return wires['a']

    # part one
    print(run_circuit())

    # part two
    print(run_circuit(True))
