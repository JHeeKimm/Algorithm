const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const index = input[1] - 1;
console.log(input[0][index]);