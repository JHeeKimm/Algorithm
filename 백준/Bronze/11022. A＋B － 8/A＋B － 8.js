const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const count = Number(input[0]);
let result = '';

for(let i=1; i<=count; i++){
    const numbers = input[i].split(' ').map(Number);
    result += `Case #${i}: ${numbers[0]} + ${numbers[1]} = ${numbers[0]+numbers[1]}` + '\n'
}
console.log(result);