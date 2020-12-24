let input = '106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36';

let reverse = (list, start, end) => {
    let prev_end = -1;
    while (start !== end && start !== prev_end) {
        let temp = list[start];
        list[start] = list[end];
        list[end] = temp;
        prev_end = end;
        start = ++start % list.length;
        end = (--end + list.length) % list.length;
    }
}

let knot_hash = (input, rounds, part_two=false) => {
    let lengths;
    if (part_two) lengths = input.split('').map(x => x.charCodeAt()).concat([17, 31, 73, 47, 23]);
    else lengths = input.split(',').map(x => parseInt(x))
    let list = [...Array(256).keys()];
    let pos = 0;
    let skip = 0;
    for (let i = 0; i < rounds; i++) {
        for (let length of lengths) {
            if (length > 0) reverse(list, pos, (pos + length + 255) % 256);
            pos = (pos + length + skip) % 256;
            skip++;
        }
    }
    if (part_two) {
        let dense_hash = [];
        for (let i = 0; i < 16; i++) dense_hash.push(list.slice(16 * i, 16 * i + 16).reduce((a, b) => a ^ b));
        return dense_hash.map(x => ('00' + x.toString(16)).substr(-2)).join('');
    } else return list[0] * list[1];
}

//part one
console.log(knot_hash(input, 1));

//part two
console.log(knot_hash(input, 64, true));

exports.knot_hash = knot_hash;