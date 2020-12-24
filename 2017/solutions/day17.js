let spinlock = (insertions, part_two=false, step =335) => {
    let buffer = [0];
    let at_one = 0;
    let pos = 0;
    for (let i = 1; i  < insertions + 1; i++) {
        pos = (pos + step) % buffer.length + 1;
        if (pos === 1) at_one = i;
        if (part_two) buffer.push(0);
        else buffer.splice(pos, 0, i);
    }
    if (part_two) return at_one;
    else return buffer[buffer.indexOf(2017) + 1];
}


//part one
console.log(spinlock(2017));

//part two
console.log(spinlock(50000000, true));