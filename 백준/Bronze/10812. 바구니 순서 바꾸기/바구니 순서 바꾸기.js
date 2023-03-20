const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(' ').map(Number);
let arr = Array.from({length : N}, (v, index) => index + 1);

for(let i=1; i<=M; i++){
    const [a, b, c] = input[i].split(' ').map(Number);
    let newArr = [];
    newArr.push(arr.slice(c-1, b));
    newArr.push(arr.slice(a-1, c-1));
    arr.splice(a-1, b-a+1, ...newArr.flat());
}
console.log(arr.flat().join(' '));
