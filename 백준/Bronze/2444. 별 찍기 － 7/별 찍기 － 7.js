const input = require('fs').readFileSync('/dev/stdin').toString();
let result = [];

for(let i=1; i<input; i++){
    const blank = ' '.repeat(input - i);
    const star = '*'.repeat(2 * i - 1);
    result.push(blank + star);
}
for(let j=input; j>=1; j--){
    const blank = ' '.repeat(input - j);
    const star = '*'.repeat(2 * j - 1);
    result.push(blank + star);
}
console.log(result.join('\n'));