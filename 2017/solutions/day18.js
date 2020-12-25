const fs  = require('fs');

class Program {
    constructor(p) {
        this.index = 0;
        this.waiting = false;
        this.registers = {'a':0, 'b':0, 'f':0, 'i':0, 'p':p};
        this.queue = [];
        this.sent = 0;
    }
}

let run_assembly = (line, queue, program, part_two=false) => {
    if (program.waiting && program.queue.length === 0) return;
    let val;
    if (line.length > 2) val = parseInt(line[2]);
    switch (line[0]) {
        case 'snd':
            queue.push(program.registers[line[1]]);
            program.sent++;
            break;
        case 'set':
            if (isNaN(val)) program.registers[line[1]] = program.registers[line[2]];
            else program.registers[line[1]] = val;
            break;
        case 'add':
            if (isNaN(val)) program.registers[line[1]] += program.registers[line[2]];
            else program.registers[line[1]] += val;
            break;
        case 'mul':
            if (isNaN(val)) program.registers[line[1]] *= program.registers[line[2]];
            else program.registers[line[1]] *= val;
            break;
        case 'mod':
            if (isNaN(val)) program.registers[line[1]] %= program.registers[line[2]];
            else program.registers[line[1]] %= val;
            break;
        case 'rcv':
            if (part_two) {
                if (program.queue.length > 0) {
                    program.waiting = false;
                    program.registers[line[1]] = program.queue.shift();
                }
                else {
                    program.waiting = true;
                    program.index--;
                }
            } else if (program.registers[line[1]]) program.waiting = true;
            break;
        case 'jgz':
            if (parseInt(line[1]) > 0 || program.registers[line[1]] > 0) {
                if (isNaN(val)) program.index += program.registers[line[2]] - 1;
                else program.index += val - 1;
            }
    }
    program.index++;
}

fs.readFile('../inputs/input18.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\n').map(x => x.split(' '));
    let a = new Program(0);
    let b = new Program(0);
    let c = new Program(1);

    while (!a.waiting && a.index > -1 && a.index < data.length) run_assembly(data[a.index], a.queue, a);

    //part one
    console.log(a.queue.slice(-1)[0]);

    while (((b.index > -1 && b.index < data.length) || (c.index > -1 && c.index < data.length)) && !(b.waiting && c.waiting)) {
        run_assembly(data[b.index], c.queue, b, true);
        run_assembly(data[c.index], b.queue, c, true);
    }

    //part two
    console.log(c.sent);
});