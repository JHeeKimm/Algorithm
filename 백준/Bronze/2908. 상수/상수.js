const input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
let a = Number(input[0].split('').reverse().join(''));
let b = Number(input[1].split('').reverse().join(''));
console.log(a>b ? a : b);