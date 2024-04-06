const input = require('fs').readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt").toString().split('\n').map(x=>x.split(' ').map(Number));
const [N, M] = input[0];
let A = [];
let B = [];
for(let i=1; i<input.length; i++){
    if(i<=N){
        A.push(input[i])
    }else{
        B.push(input[i])
    }
}

let arr = [];
for(let i=0; i<N; i++){
    arr.push([])
    for(let j=0; j<M; j++){
        arr[i].push(A[i][j]+B[i][j]);
    }
}
let result='';
for(let i=0; i<N; i++){
    for(let j=0; j<M; j++){
        result += `${arr[i][j]} `
    }
    result += `\n`
}
console.log(result)