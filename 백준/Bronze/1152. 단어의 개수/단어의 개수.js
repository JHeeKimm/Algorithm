let input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');
let count = 0;
input.forEach(x => (x === '' ? 0 : count++));
console.log(count);