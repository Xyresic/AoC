const fs = require('fs');

let run_packet = (delay, firewall) => {
    let sum = 0;
    for (let i = 0; i < 99; i++) {
        if (firewall[i] !== undefined && (i + delay) % (2 * (firewall[i] - 1)) === 0) sum += i * firewall[i];
    }
    return sum;
}

fs.readFile('../inputs/input13.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\n');
    let firewall = Array(99);
    for (let layer of data) {
        let depth, range;
        [depth, range] = layer.split(': ').map(x => parseInt(x));
        firewall[depth] = range;
    }

    //part one
    console.log(run_packet(0, firewall));

    //part two
    let delay = 0;
    while (run_packet(delay++, firewall) !== 0 || (delay - 1) % 4 === 0);
    console.log(delay - 1);
});