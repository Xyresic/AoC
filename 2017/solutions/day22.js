const fs = require('fs');

fs.readFile('../inputs/input22.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\n');
    let pos = [0, 0], directions = [[-1, 0], [0, 1], [1, 0], [0, -1]], cur_dir = 0, count = 0;
    let grid = {}, evolved = {};
    for (let i = 0; i < data.length; i++) {
        for (let j = 0; j < data[i].length; j++) {
            grid[`${i-12},${j-12}`] = data[i][j];
            evolved[`${i-12},${j-12}`] = data[i][j];
        }
    }
    for (let i = 0; i < 10000; i++) {
        if (grid[`${pos[0]},${pos[1]}`] === '#') {
            cur_dir = ++cur_dir % 4;
            grid[`${pos[0]},${pos[1]}`] = '.';
        }
        else {
            cur_dir = (cur_dir + 3) % 4;
            grid[`${pos[0]},${pos[1]}`] = '#';
            count++;
        }
        pos = pos.map((x, i) => x + directions[cur_dir][i]);
        if (!(`${pos[0]},${pos[1]}` in grid)) grid[`${pos[0]},${pos[1]}`] = '.';
    }

    //part one
    console.log(count);

    pos = [0, 0];
    cur_dir = 0;
    count = 0;
    for (let i = 0; i < 10000000; i++) {
        switch (evolved[`${pos[0]},${pos[1]}`]) {
            case '#':
                cur_dir = ++cur_dir % 4;
                evolved[`${pos[0]},${pos[1]}`] = 'F';
                break;
            case 'F':
                cur_dir = (cur_dir + 2) % 4;
                evolved[`${pos[0]},${pos[1]}`] = '.';
                break;
            case '.':
                cur_dir = (cur_dir + 3) % 4;
                evolved[`${pos[0]},${pos[1]}`] = 'W';
                break;
            default:
                evolved[`${pos[0]},${pos[1]}`] = '#';
                count++;
        }
        pos = pos.map((x, i) => x + directions[cur_dir][i]);
        if (!(`${pos[0]},${pos[1]}` in evolved)) evolved[`${pos[0]},${pos[1]}`] = '.';
    }

    //part two
    console.log(count);
});