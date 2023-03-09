const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(' ').map(Number);
let arr = Array.from({length:N}, (v, index) => index + 1);

for(let i=1; i<=M; i++){
    let [a, b] = input[i].split(' ').map(Number);
    let valueA = arr[a-1];
    arr[a-1] = arr[b-1];
    arr[b-1] = valueA;
}
console.log(arr.join(' '));