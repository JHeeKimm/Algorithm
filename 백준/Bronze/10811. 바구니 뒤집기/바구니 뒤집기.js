const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(' ');
let arr = Array.from({ length: N }, (v, index) => index + 1);

for(let i=1; i<=M; i++){
    const [a, b] = input[i].split(' ');
    const sliceReverse = arr.slice(a-1, b).reverse();
    
    arr.splice(a-1, b-a+1, ...sliceReverse);
}
console.log(arr.join(' '));