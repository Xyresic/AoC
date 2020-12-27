const fs = require('fs');

fs.readFile('../inputs/input25.txt', 'utf-8', (err, data) => {
    let states = {'A':{0:[1, 1, 'B'], 1:[0, -1, 'C']},
                  'B':{0:[1, -1, 'A'], 1:[1, -1, 'D']},
                  'C':{0:[1, 1, 'D'], 1:[0, 1, 'C']},
                  'D':{0:[0, -1, 'B'], 1:[0, 1, 'E']},
                  'E':{0:[1, 1, 'C'], 1:[1, -1, 'F']},
                  'F':{0:[1, -1, 'E'], 1:[1, 1, 'A']}};
    let tape = {0:0}, pos = 0, state = 'A', count = 0;

    for (let i = 0; i < 12656374; i++) {
        let delta = states[state][tape[pos]];
        tape[pos] = delta[0];
        pos += delta[1];
        if (!(pos in tape)) tape[pos] = 0;
        state = delta[2];
    }

    for (let index in tape) if (tape[index] === 1) count++;

    //part one
    console.log(count);
});