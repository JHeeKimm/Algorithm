const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const count = Number(input[0]);
let result = '';

for(let i=1; i<=count; i++){
    let numbers = input[i].split(' ').map(Number);
    result += numbers[0] + numbers[1] +'\n';
}
console.log(result);