const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const arr = input[1].split('').map(Number)
const result = arr.reduce((prev, cur)=>{
  return prev + cur;
	}, 0)
console.log(result);