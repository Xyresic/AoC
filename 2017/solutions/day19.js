const fs = require('fs');

let in_bounds = (map, y, x) => {
    return y >= 0 && y < map.length && x >= 0 && x < map[y].length;
}

let is_valid = (map, y, x, vertical=true) => {
    if (!in_bounds(map, y, x)) return false;
    let char = map[y][x];
    return char !== ' ' && char !== (vertical? '-':'|');
}

fs.readFile('../inputs/input19.txt', 'utf-8', (err, data) => {
    data = data.split('\n').slice(0, 200);
    let pos = [0, 135], dir = [1, 0], visited = ['|'];
    while (true) {
        if (Math.abs(dir[0]) === 1 ) {
            if (is_valid(data, pos[0] + dir[0], pos[1])) {
                pos[0] += dir[0];
                visited.push(data[pos[0]][pos[1]]);
            }
            else if (data[pos[0]][pos[1]] !== '+' && is_valid(data, pos[0] + dir[0] * 2, pos[1])) {
                pos[0] += dir[0] * 2;
                visited.push('|');
                visited.push(data[pos[0]][pos[1]]);
            }
            else if (is_valid(data, pos[0], pos[1] - 1, false)) dir = [0, -1];
            else if (is_valid(data, pos[0], pos[1] + 1, false)) dir = [0, 1];
            else break;
        } else {
            if (is_valid(data, pos[0], pos[1] + dir[1], false)) {
                pos[1] += dir[1];
                visited.push(data[pos[0]][pos[1]]);
            }
            else if (data[pos[0]][pos[1]] !== '+' && is_valid(data, pos[0], pos[1] + 2 * dir[1], false)) {
                pos[1] += dir[1] * 2;
                visited.push('-');
                visited.push(data[pos[0]][pos[1]]);
            }
            else if (is_valid(data, pos[0] - 1, pos[1])) dir = [-1, 0];
            else if (is_valid(data, pos[0] + 1, pos[1])) dir = [1, 0];
            else break;
        }
    }

    //part one
    console.log(visited.filter(x => x.charCodeAt() > 64 && x.charCodeAt() < 91).join(''));

    //part two
    console.log(visited.length)
});