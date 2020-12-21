const fs = require('fs');

fs.readFile('../inputs/input2.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\n').map(x => x.split('\t').map(y => parseInt(y)));
    let sum = data.map(x => Math.max(...x) - Math.min(...x)).reduce((a, b) => a + b);

    //part one
    console.log(sum);

    sum = data.map(x => {
        for (let i = 0; i < x.length - 1; i++) {
            for (let j = i + 1; j < x.length; j++) {
                if (x[i] % x[j] === 0) {
                    return x[i] / x[j];
                } else if (x[j] % x[i] === 0) {
                    return x[j] / x[i];
                }
            }
        }
    }).reduce((a, b) => a + b);

    //part two
    console.log(sum);
});