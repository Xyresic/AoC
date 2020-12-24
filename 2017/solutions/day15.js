function* a_gen() {
    let val = 116;
    while (true) {
        val = (val * 16807) % 2147483647;
        yield val;
    }
}

function* b_gen() {
    let val = 299;
    while (true) {
        val = (val * 48271) % 2147483647;
        yield val;
    }
}

const a = a_gen();
const b = b_gen();
let a_vals = [], b_vals = [], count = 0;

let test_val = (val, is_a=true) => {
    if (is_a) {
        if (val % 4 === 0) a_vals.push(val);
    } else if (val % 8 === 0) b_vals.push(val);
    return val;
}

for (let i = 0;  i < 40000000; i++) {
    if (test_val(a.next().value) % 2**16 === test_val(b.next().value, false) % 2**16) count++;
}

//part one
console.log(count);

while (a_vals.length < 5000000) test_val(a.next().value);
while (b_vals.length < 5000000) test_val(b.next().value, false);

//part two
console.log(a_vals.filter((x, i) => x % 2**16 === b_vals[i] % 2**16).length);