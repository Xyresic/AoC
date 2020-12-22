let get_ring = (num) => {
    let ring = Math.ceil(Math.sqrt(num));
    return ring % 2 === 0? ring + 1:ring;
}

let get_corners = (ring) => {
    return [ring**2-3*(ring-1), ring**2-2*(ring-1), ring**2-ring+1, ring**2];
}

let spiral = (num) => {
    let ring = get_ring(num);
    return Math.max(...get_corners(ring).map(x => ring - 1 - Math.abs((num - x))));
};

//part one
console.log(spiral(289326));

let map = [];
let val = 1;
let step = 1;
while (val < 289326) {
    map.push(val);
    step++;
    let ring = get_ring(step);
    let corners = get_corners(ring);
    let offset = 4 * ring - 11;
    let side = Math.floor((step - (ring - 2)**2 - 1) / (ring - 1));

    corners = corners.slice(0, 3);
    if (!corners.includes(step)) {
        if (step !== (ring - 2) ** 2 + 1) val += map[step - offset - 2 * side - 1];
        if (step !== ring**2 && !corners.map(x => x - 1).includes(step)) val +=  map[step - offset - 2 * side];
    }
    if (step!== (ring - 2) ** 2 + 1) {
        if (step !== (ring - 2) ** 2 + 2 && !corners.map(x => x + 1).includes(step)) val += map[step - offset - 2 * side - 2];
        else val += map[step - 3];
    }
}

//part two
console.log(val);