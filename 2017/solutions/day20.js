const fs = require('fs');

class Particle {
    constructor(id, pos, vel, acc) {
        this.id = id;
        this.pos = pos;
        this.vel = vel;
        this.acc = acc;
    }
}

let magnitude = (arr) => {
    return arr.map(x => Math.abs(x)).reduce((a, b) => a + b);
}

let arr_equals = (arr1, arr2) => {
    return arr1.map((x, i) => x === arr2[i]).reduce((a, b) => a && b);
}

fs.readFile('../inputs/input20.txt', 'utf-8', (err, data) => {
    data = data.trim().split('\n');
    let particles = [];
    let copy = [];
    for (let i = 0; i < data.length; i++) {
        let values = [];
        for (let match of data[i].matchAll(/-*\d+/g)) values.push(parseInt(match[0]));
        particles.push(new Particle(i, values.slice(0, 3), values.slice(3, 6), values.slice(6, 9)));
        copy.push(new Particle(i, values.slice(0, 3), values.slice(3, 6), values.slice(6, 9)));
    }

    let min_acc = Math.min(...copy.map(p => magnitude(p.acc)));
    copy = copy.filter(p => magnitude(p.acc) === min_acc);
    let min_vel = Math.min(...copy.map(p => magnitude(p.vel)));
    copy = copy.filter(p => magnitude(p.vel) === min_vel);
    copy.sort((a, b) => magnitude(a.pos) - magnitude(b.pos));

    //part one
    console.log(copy[0].id);

    let wait_time = Math.ceil(Math.abs(Math.min(...particles.map(p => Math.min(...[...Array(3).keys()].map(x => p.acc[x] === 0? Number.MAX_VALUE:p.vel[x] / p.acc[x]))))));
    for (let t = 0; t < wait_time; t++) {
        particles.forEach(p => {
            p.vel = p.vel.map((v, i) => v + p.acc[i]);
            p.pos = p.pos.map((d, i) => d + p.vel[i]);

        });
        for (let i = 0; i < particles.length - 1; i++) {
            let collision = false;
            for (let j = i + 1; j < particles.length; j++) {
                if (arr_equals(particles[i].pos, particles[j].pos)) {
                    particles.splice(j, 1);
                    collision = true;
                    j--;
                }
            }
            if (collision) {
                particles.splice(i, 1);
                i--;
            }
        }
    }
    //part two
    console.log(particles.length);
});