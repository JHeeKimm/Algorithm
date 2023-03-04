const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const count = Number(input[0]);
let numbers = []; 

for(let i=1; i<=count; i++){
    numbers = input[i].split(' ').map(Number);
    console.log(numbers[0]+numbers[1])
}