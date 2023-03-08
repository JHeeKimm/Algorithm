const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, X] = input[0].split(' ');
const numbers = input[1].split(' ').map(Number);
const result = numbers.filter(number=>number < X);
console.log(result.join(' '));