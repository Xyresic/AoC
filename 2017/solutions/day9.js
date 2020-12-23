const fs = require('fs');

fs.readFile('../inputs/input9.txt', 'utf-8', (err, data) => {
    data = data.trim();
    let level = 1;
    let score = 0;
    let count = 0;
    let garbage = false;

    for (let i = 0; i < data.length; i++) {
        let char = data[i];
        if (!garbage) {
            switch (char) {
                case '<':
                    garbage = true;
                    break;
                case '{':
                    score += level;
                    level++;
                    break;
                case '}':
                    level--;
            }
        } else {
            switch (char) {
                case '>':
                    garbage = false;
                    break;
                case '!':
                    i++;
                    break;
                default:
                    count++;
            }
        }
    }

    //part one
    console.log(score);

    //part two
    console.log(count);
});