const fs = require('fs');

let make_bridges = (port, components, cur_length) => {
    let filtered = components.filter(x => x.includes(port));
    if (filtered.length === 0) return [port, cur_length, port];
    else {
        let strengths = [];
        let long_strengths = [];
        let max_length = cur_length;
        for (let component of filtered) {
            let other_port = component[0] === port? component[1]:component[0];
            let copy = [...components];
            copy.splice(copy.map(x => x.join('/')).indexOf(component.join('/')), 1)
            let info = make_bridges(other_port, copy, cur_length + 1);
            strengths.push(info[0] + port);
            if (info[1] > max_length) {
                long_strengths = [];
                max_length = info[1];
            }
            if (info[1] === max_length) long_strengths.push(info[2] + port);
        }
        return [Math.max(...strengths) + port, max_length, Math.max(...long_strengths) + port];
    }
}

fs.readFile('../inputs/input24.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\n').map(x => x.split('/').map(y => parseInt(y)));
    let info = make_bridges(0, data, 0);

    //part one
    console.log(info[0]);

    //part two
    console.log(info[2]);
});