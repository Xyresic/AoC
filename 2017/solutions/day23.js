//part one
//the mul at line 5 never gets invoked, only the one at line 13 does
//it's inside a double loop: d from 2 to b, e from 2 to b
//b starts at 79 and is static, so the mul is invoked (79 - 2)**2 times
console.log(77**2);

//part two
//lines 11 through 24 are a loop that checks if b is a prime
//if it is, f is 1; if not, f is 0
//h only gets incremented if f is not 0 => b is not prime
//b loops from 107900 to 124900, 1001 times
let is_prime = (num) => {
    for (let d = 2; d < Math.floor(Math.sqrt(num)); d++) {
        if (num % d === 0) return false;
    }
    return true;
}

let h = 0;
for (let b = 107900; b < 124917; b += 17) {
    if (!is_prime(b)) h++;
}
console.log(h);