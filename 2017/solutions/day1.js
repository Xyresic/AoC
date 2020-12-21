const fs = require('fs');

let summation = (a, b) => {return parseInt(a) + parseInt(b)};

fs.readFile('../inputs/input1.txt', 'utf-8', (err, data) => {
    data = data.trim();
    let re = /(.)(?=\1)/g;
    let sum = data.match(re).reduce(summation);
    if (data.charAt(0) === data.slice(-1)) sum += parseInt(data.charAt(0));

    //part one
    console.log(sum);

    let half = data.length / 2
    re = new RegExp(`(.)(?=.{${half - 1}}\\1)`, 'g');
    let looped = data.slice(half) + data.slice(0, half);
    sum = data.match(re).reduce(summation);
    sum += looped.match(re).reduce(summation);

    //part two
    console.log(sum);
});