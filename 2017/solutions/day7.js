/*
I believe this solution is not completely general as it does not properly deal with the case
where the unbalanced disk only has two programs on it, in which case it would be necessary
to determine which change is correct as a change may cause the next disk down to become unbalanced.
*/

const fs = require('fs');
let found = false;

class Tree {
    constructor(name, weight, subtree=[]) {
        this.name = name;
        this.weight = weight;
        this.subtree = subtree;
    }
}

let make_tree = (program, data, graph, processed) => {
    let tree = new Tree(program[0], parseInt(program[1].slice(1, program[1].length)));
    graph.push(tree);
    processed.push(tree.name);
    if (program.length > 2) {
        for (let child of program.slice(3)) {
            child = child.replace(',', '');
            if (!processed.includes(child)) {
                let child_program = data.splice(data.map(x => x[0]).indexOf(child), 1)[0];
                make_tree(child_program, data, graph, processed);
            }
            tree.subtree.push(graph.splice(graph.map(x => x.name).indexOf(child), 1)[0]);
        }
    }
}

let weigh = (tree) => {
    if (tree.subtree.length === 0) return tree.weight;
    else {
        let weights = tree.subtree.map(x => weigh(x));
        if (!found && !weights.every(x => x === weights[0])) {
            let sorted = [...weights].sort();
            if (sorted[0] !== sorted[1]) {
                console.log(tree.subtree[weights.indexOf(sorted[0])].weight + sorted[1] - sorted[0]);
            } else {
                console.log(tree.subtree[weights.indexOf(sorted[sorted.length - 1])].weight - sorted[sorted.length - 1] + sorted[0]);
            }
            found = true;
        } else return weights.reduce((a, b) => a + b) + tree.weight;
    }
}

fs.readFile('../inputs/input7.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\n').map(x => x.split(' '));
    let graph = [];
    let processed = [];

    while (data.length > 0) make_tree(data.pop(), data, graph, processed);

    //part one
    console.log(graph[0].name);

    //part two
    weigh(graph[0]);
});