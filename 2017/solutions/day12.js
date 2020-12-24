const fs = require('fs');

class Node {
    constructor(id, neighbors=[]) {
        this.id = id;
        this.neighbors = neighbors;
    }
}

let superset = (large, small) => {
    for (let element of small) if (!large.includes(element)) return false;
    return true;
}

let count_members = (visited, node, global, part_two=false) => {
    if (visited.includes(node.id)) return 0;
    if (part_two) global.splice(global.indexOf(node), 1);
    visited.push(node.id);
    if (superset(visited, node.neighbors)) return 1;
    else {
        return 1 + node.neighbors.map(x => count_members(visited, x, global, part_two)).reduce((a, b) => a + b);
    }
}

fs.readFile('../inputs/input12.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\n');
    let nodes = [...Array(2000).keys()].map(x => new Node(x));
    for (let line of data) {
        let base_node = line.match(/\d+/)[0];
        for (let match of line.matchAll(/\d+(?<=>.*)/g)) nodes[base_node].neighbors.push(nodes[parseInt(match[0])]);
    }

    //part one
    console.log(count_members([], nodes[0]));

    let count = 0;
    while (nodes.length > 0) {
        count_members([], nodes[0], nodes, true);
        count++;
    }

    //part two
    console.log(count);
});