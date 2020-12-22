const fs = require('fs');

fs.readFile('../inputs/input4.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\n').map(x => x.split(' '));
    let count = 0;
    for (let line of data) {
        for (let i = 0; i < line.length - 1; i++) {
            if (line.slice(i + 1).includes(line[i])) {
                count++;
                break;
            }
        }
    }

    //part one
    console.log(data.length - count);

    //note: problem considers words to be anagrams of themselves
    count = 0;
    for (let line of data) {
        for (let i = 0; i < line.length - 1; i++) {
            let found = false;
            for (let j = i + 1; j < line.length; j++) {
                if (line[i].length !== line[j].length) continue;
                else if (line[i].split('').sort().join('') === line[j].split('').sort().join('')) {
                    count++;
                    found = true;
                    break;
                }
            }
            if (found) break;
        }
    }

    //part two
    console.log(data.length - count);
});