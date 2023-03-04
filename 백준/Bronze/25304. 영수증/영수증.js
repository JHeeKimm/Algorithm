const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const total = Number(input[0]);
const count = Number(input[1]);
let numbers = [];
let multiply;
let sum = 0;

for(let i=2; i<=(count+1); i++){
    numbers = input[i].split(' ').map(Number);
    multiply = numbers[0]*numbers[1];
    sum += multiply;
}
if(sum===total){
    console.log('Yes');
}else{
    console.log('No');
}