const numbers = require('fs').readFileSync('/dev/stdin').toString().split(' ').map(Number);
const A = numbers[0];
const B = numbers[1];
const C = numbers[2];
const maxNum = Math.max(...numbers);

if(A === B && A === C){
    console.log(10000 + (A * 1000));
}else if(A === B || A === C || B === C){
    if(A === B || A === C){
        console.log(1000 + (A * 100));
    }else{
        console.log(1000 + (B * 100));
    }
}else if(A !== B && A !== C && B !== C){
    console.log(maxNum * 100);
}
