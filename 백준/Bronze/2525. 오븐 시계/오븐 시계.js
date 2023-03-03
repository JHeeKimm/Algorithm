const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let [hour, minute] = input[0].split(' ').map(Number);
let cookingTime = Number(input[1]);

minute += cookingTime;
if(minute >= 60){
    hour += Math.floor(minute/60);
    minute %= 60;
}
if(hour > 23){
    hour %= 24;
}
console.log(`${hour} ${minute}`);