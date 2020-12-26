const fs = require('fs');

let rotate_flip = (square) => {
    let size = square.length;
    let flipped = [...Array(size)].map(x => Array(size));
    let rotated = [...Array(size)].map(x => Array(size));
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            flipped[i][size-j-1] = square[i][j];
            rotated[j][size-i-1] = square[i][j];
        }
    }
    return [flipped, rotated]
}

let permutations = (grid) => {
    let perms = [grid];
    for (let i = 0; i < 4; i++) {
        grid = rotate_flip(grid);
        perms.push(grid[0]);
        perms.push(grid[1]);
        grid = grid[1];
    }
    return perms.slice(0, perms.length - 1);
}

let match = (enhancements, grid) => {
    let perms = permutations(grid);
    perms = perms.map(x => x.map(y => y.join('')).join('/'));
    for (let enhancement of enhancements) {
        if (perms.includes(enhancement[0])) return enhancement[1].split('/').map(x => x.split(''));
    }
}

let iterate = (enhancements, grid) => {
    let div = grid.length % 2 === 0? 2:3;
    let split = [];
    for (let i = 0; i < grid.length / div; i++) {
        for (let j = 0; j < grid.length / div; j++) {
            let subgrid = [];
            for (let x = i * div; x < (i + 1) * div; x++) {
                let row = []
                for (let y = j * div; y < (j + 1) * div; y++) row.push(grid[x][y]);
                subgrid.push(row);
            }
            split.push(subgrid);
        }
    }
    split = split.map(x => match(enhancements, x));
    grid = [];
    let size = Math.sqrt(split.length);
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < div + 1; j++) {
            let row = [];
            for (let k = i * size; k < (i + 1) * size; k++) {
                row = row.concat(split[k][j]);
            }
            grid.push(row);
        }
    }
    return grid;
}

fs.readFile('../inputs/input21.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\n').map(x => x.split(' => '));
    let grid = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']];
    for (let i = 0; i < 5; i++) grid = iterate(data, grid);

    //part one
    console.log(grid.map(x => x.filter(y => y === '#').length).reduce((a, b) => a+b));

    for (let i = 0; i < 13; i++) grid = iterate(data, grid);

    //part two
    console.log(grid.map(x => x.filter(y => y === '#').length).reduce((a, b) => a+b));
});