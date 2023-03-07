let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let [length, arr, num] = input;
let count = 0;
arr = arr.split(' ');

for(let i=0; i<length; i++){
    if(arr[i] === num){
        count++;
    }
}
console.log(count);
