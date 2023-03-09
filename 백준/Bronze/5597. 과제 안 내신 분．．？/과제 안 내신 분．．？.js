const arr = require('fs').readFileSync('/dev/stdin').toString().split('\n').map(Number);
let newArr = [];

for(let i=1; i<=30; i++){
    if(!arr.includes(i)){
        newArr.push(i);
    }
}
console.log(newArr.sort((a, b) => a - b).join('\n'));