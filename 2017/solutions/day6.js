const fs = require('fs');

fs.readFile('../inputs/input6.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\t').map(x => parseInt(x));
    let cycles = 0;
    let states = [];

    while(!states.includes(data.join(''))) {
        states.push(data.join(''));
        let index = data.indexOf(Math.max(...data));
        let val = data[index];
        data[index] = 0;
        let i = (index + 1) % data.length;
        while (val > 0) {
            data[i]++;
            i = (i + 1) % data.length;
            val--;
        }
        cycles++;
    }

    //part one
    console.log(cycles);

    //part two
    console.log(cycles - states.indexOf(data.join('')));
});