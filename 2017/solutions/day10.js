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

let hash = (lengths, rounds, part_two=false) => {
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
    return part_two? list:list[0] * list[1];
}

//part one
console.log(hash(input.split(',').map(x => parseInt(x)), 1));

input = input.split('').map(x => x.charCodeAt(0)).concat([17, 31, 73, 47, 23]);
let sparse_hash = hash(input, 64, true);
let dense_hash = [];
for (let i = 0; i < 16; i++) dense_hash.push(sparse_hash.slice(16 * i, 16 * i + 16).reduce((a, b) => a ^ b));

//part two
console.log(dense_hash.map(x => ('00' + x.toString(16)).substr(-2)).join(''));