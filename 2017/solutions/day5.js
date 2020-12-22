const fs = require('fs');

fs.readFile('../inputs/input5.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\n').map(x => parseInt(x));
    let clone = [...data];
    let steps = 0;
    let index = 0;

    while(index > -1 && index < data.length) {
        index += data[index]++;
        steps++;
    }

    //part one
    console.log(steps);

    steps = 0;
    index = 0;

    while(index > -1 && index < clone.length) {
        if (clone[index] > 2) index += clone[index]--;
        else index += clone[index]++;
        steps++;
    }

    //part one
    console.log(steps);
});