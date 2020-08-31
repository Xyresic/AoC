from numpy import uint16

with open('../inputs/input7.txt', 'r') as f:
    data = f.readlines()
    wires = {}
    gates = []

    class Component:
        def __init__(self, name):
            self.name = name
            self.inputs = []
            self.outputs = []
            self.output = None

        def add_input(self, input):
            self.inputs.append(input)

        def add_output(self, output):
            self.outputs.append(output)

        def has_inputs(self):
            for input in self.inputs:
                if input.output is None:
                    return False
            return True

        def has_output(self):
            return self.output is not None

        def send_signal(self):
            for output in self.outputs:
                output.output = self.output

    class NotGate(Component):
        def __init__(self, name, i_wire, o_wire):
            super().__init__(name)
            self.add_input(i_wire)
            self.add_output(o_wire)

        def send_signal(self):
            self.outputs[0].output = uint16(~ self.inputs[0].output)

    class LShiftGate(Component):
        def __init__(self, name, shift, i_wire, o_wire):
            super().__init__(name)
            self.shift = shift
            self.add_input(i_wire)
            self.add_output(o_wire)

        def send_signal(self):
            self.outputs[0].output = uint16(self.inputs[0].output << self.shift)

    class RShiftGate(Component):
        def __init__(self, name, shift, i_wire, o_wire):
            super().__init__(name)
            self.shift = shift
            self.add_input(i_wire)
            self.add_output(o_wire)

        def send_signal(self):
            self.outputs[0].output = uint16(self.inputs[0].output >> self.shift)

    class AndGate(Component):
        def __init__(self, name, i_wire1, i_wire2, o_wire):
            super().__init__(name)
            self.add_input(i_wire1)
            self.add_input(i_wire2)
            self.add_output(o_wire)

        def send_signal(self):
            self.outputs[0].output = uint16(self.inputs[0].output & self.inputs[1].output)

    class OrGate(Component):
        def __init__(self, name, i_wire1, i_wire2, o_wire):
            super().__init__(name)
            self.add_input(i_wire1)
            self.add_input(i_wire2)
            self.add_output(o_wire)

        def send_signal(self):
            self.outputs[0].output = uint16(self.inputs[0].output | self.inputs[1].output)

    def add_wire(wire):
        if wire not in wires:
            wires[wire] = Component(wire)
            if wire == '1':
                wires[wire].output = 1
        return wires[wire]

    def setup():
        for line in data:
            instr = line.split()
            if 'NOT' in line:
                wire1 = add_wire(instr[1])
                wire2 = add_wire(instr[3])
                gate = NotGate('NOT', wire1, wire2)
                gates.append(gate)
            elif 'LSHIFT' in line:
                wire1 = add_wire(instr[0])
                wire2 = add_wire(instr[4])
                gate = LShiftGate('LSHIFT', int(instr[2]), wire1, wire2)
                gates.append(gate)
            elif 'RSHIFT' in line:
                wire1 = add_wire(instr[0])
                wire2 = add_wire(instr[4])
                gate = RShiftGate('RSHIFT', int(instr[2]), wire1, wire2)
                gates.append(gate)
            elif 'OR' in line:
                wire1 = add_wire(instr[0])
                wire2 = add_wire(instr[2])
                wire3 = add_wire(instr[4])
                gate = OrGate('OR', wire1, wire2, wire3)
                gates.append(gate)
            elif 'AND' in line:
                wire1 = add_wire(instr[0])
                wire2 = add_wire(instr[2])
                wire3 = add_wire(instr[4])
                gate = AndGate('AND', wire1, wire2, wire3)
                gates.append(gate)
            elif instr[0].isnumeric():
                wire = add_wire(instr[2])
                wire.output = uint16(instr[0])
            else:
                wire1 = add_wire(instr[0])
                wire2 = add_wire(instr[2])
                wire1.add_output(wire2)

    def run():
        while wires['a'].output is None:
            for gate in gates:
                if gate.has_inputs():
                    gate.send_signal()
                    gates.remove(gate)
            for wire in wires:
                if wires[wire].has_output():
                    wires[wire].send_signal()


    # part one
    setup()
    run()
    a = wires['a'].output
    print(a)

    # part two
    wires = {}
    gates = []

    setup()
    wires['b'].output = a
    run()
    print(wires['a'].output)
