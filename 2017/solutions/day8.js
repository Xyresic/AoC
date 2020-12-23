const fs = require('fs');

fs.readFile('../inputs/input8.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\n').map(x => x.split(' '));
    let registers = {};
    let vals = [];
    for (let line of data) {
        if (!(line[0] in registers)) registers[line[0]] = 0;
        if (!(line[4] in registers)) registers[line[4]] = 0;
        let delta = parseInt(line[2]);
        if (eval(`registers.${line[4]}${line[5]}${line[6]}`)) {
            registers[line[0]] += line[1] === 'inc'? delta:-delta;
            vals.push(registers[line[0]]);
        }
    }

    //part one
    console.log(Math.max(...Object.values(registers)));

    //part two
    console.log(Math.max(...vals));
});