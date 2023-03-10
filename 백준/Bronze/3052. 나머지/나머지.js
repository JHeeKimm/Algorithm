const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const arr = input.map(x => x % 42);
const setSize = new Set(arr).size;

console.log(setSize);


