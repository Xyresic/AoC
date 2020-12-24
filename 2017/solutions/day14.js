//I don't know how else to suppress the logs so ¯\_(ツ)_/¯
let log = console.log;
console.log = () => {};
const hash = require('./day10.js');
console.log = log;

let grid = [];
let visited = [];
let regions = 0;

let traverse = (x, y) => {
    if (x >= 0 && y >= 0 && x < 128 && y < 128 && grid[x][y] === '1' && !visited.includes(`${x},${y}`)) {
        visited.push(`${x},${y}`);
        for (let d = -1; d < 2; d += 2) {
            traverse(x + d, y);
            traverse(x, y + d);
        }
    }
}

for (let i = 0; i < 128; i++) {
    let hex = hash.knot_hash(`ugkiagan-${i}`, 64, true);
    grid.push(hex.split('').map(digit => ('0000' + parseInt(digit, 16).toString(2)).slice(-4)).join(''));
}

for (let i = 0; i < 128; i++) {
    for (let j = 0; j < 128; j++) {
        if (grid[i][j] === '1' && !visited.includes(`${i},${j}`)) {
            traverse(i, j);
            regions++;
        }
    }
}

//part one
console.log(visited.length);

//part two
console.log(regions);