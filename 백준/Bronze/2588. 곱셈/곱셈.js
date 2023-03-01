const [a, b] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const num1 = parseInt(a);
const num2 = b.split('').map(Number);
let result = num2.reverse().map((x)=>x*num1);
result.push(num1*parseInt(b));
console.log(result.join('\n'));
