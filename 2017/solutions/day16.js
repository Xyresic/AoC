const fs = require('fs');

let swap = (obj, a, b) => {
    let temp = obj[a];
    obj[a] = obj[b];
    obj[b] = temp;
}

let key_from_val = (obj, val) => {
    return Object.keys(obj)[Object.values(obj).indexOf(val)];
}

let dance = (programs, moves) => {
    for (let move of moves) {
        switch (move[0]) {
            case 's':
                for (let p in programs) programs[p] = (programs[p] + parseInt(move.match(/\d+/)[0])) % 16
                break;
            case 'x':
                let a = key_from_val(programs, parseInt(move.match(/\d+(?=\/)/)[0]));
                let b = key_from_val(programs, parseInt(move.match(/(?<=\/)\d+/)[0]));
                swap(programs, a, b);
                break;
            default:
                swap(programs, move[1], move[3]);
        }
    }
    return [...Array(16).keys()].map(x => key_from_val(programs, x)).join('');
}

fs.readFile('../inputs/input16.txt', 'utf-8', (err, data) => {
    data = data.trim().split(',');
    let seen = [];
    let programs = {};
    for (let i = 0; i < 16; i++) programs[String.fromCharCode('a'.charCodeAt() + i)] = i;

    //part one
    seen.push(dance(programs, data));
    console.log(seen[0]);

    //part two
    let start, cycle;
    while (true) {
        let next = dance(programs, data);
        if (seen.includes(next)) {
            start = seen.indexOf(next);
            cycle = seen.length - start;
            break;
        } else seen.push(next);
    }
    console.log(seen[start + (1000000000 - start) % cycle - 1]);
});