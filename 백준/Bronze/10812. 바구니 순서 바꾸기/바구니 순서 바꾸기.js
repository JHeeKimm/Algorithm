const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(' ');
let arr = Array.from({length : N}, (v, index) => index + 1);

for(let i=1; i<=M; i++){
    const [a, b, c] = input[i].split(' ');
    let newArr1 = arr.slice(c-1, b);
    let newArr2 = arr.slice(a-1, c-1);
    let newArr3 = newArr1.concat(newArr2)
    arr.splice(a-1, b-a+1, ...newArr3).flat();
}
console.log(arr.join(' '));
