const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const arr = input.map(Number);
const max = Math.max(...arr);
console.log(max);
console.log(arr.indexOf(max)+1);