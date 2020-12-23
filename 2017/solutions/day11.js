const fs = require('fs');

let dist_from_origin = (coord) => {
    return Math.max(Math.abs(coord[0]), Math.abs(coord[1]), Math.abs(coord[0] + coord[1]));
}

fs.readFile('../inputs/input11.txt', 'utf-8', (err, data) => {
    data = data.trim().split(',');
    let coord = [0, 0];
    let visited = [[...coord]];

    for (let move of data) {
        switch (move) {
            case 'n':
                coord[1]++;
                break;
            case 's':
                coord[1]--;
                break;
            case 'ne':
                coord[0]++;
                break;
            case 'sw':
                coord[0]--;
                break;
            case 'se':
                coord[0]++;
                coord[1]--;
                break;
            default:
                coord[0]--;
                coord[1]++;
        }
        visited.push([...coord]);
    }

    //part one
    console.log(dist_from_origin(coord));

    //part two
    console.log(Math.max(...visited.map(x => dist_from_origin(x))));
});