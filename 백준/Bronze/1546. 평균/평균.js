const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const arr = input[1].split(' ');
const max = Math.max(...arr);
const result = [];
arr.forEach( x => result.push(x/max*100))
console.log(result.reduce((sum, currValue)=>sum+currValue,0)/input[0]);