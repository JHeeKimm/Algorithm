const input = require('fs').readFileSync('dev/stdin').toString().split('\n');
for(let i=1; i<=input[0]; i++){
    const arr = input[i].split(' ').map(Number)
    const N = arr[0];
    let sliceArr = arr.slice(1);
    const average = sliceArr.reduce((sum, current)=>sum+current)/N;
    console.log((sliceArr.filter(x => x > average).length/arr[0]*100).toFixed(3) + '%')
}