let arr = require('fs').readFileSync('/dev/stdin').toString().split(' ').map(Number);
let newArr = [];
for(let i=0; i<=1; i++){
    newArr.push(arr[i] = 1 - arr[i]);
};
for(let j=2; j<=4; j++){
    newArr.push(arr[j] = 2 - arr[j]);
};
newArr.push(arr[5] = 8 - arr[5]);
console.log(newArr.join(' '));