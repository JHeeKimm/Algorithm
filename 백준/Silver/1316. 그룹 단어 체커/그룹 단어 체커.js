const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let count = Number(input[0]);

for(let i=1; i<=input[0]; i++){
    for(let j=0; j<input[i].length-1; j++){
        if(input[i].slice(j+1).includes(input[i][j]) && input[i][j+1] !== input[i][j]){
            count--;
            break;
        }
    }
}
console.log(count);