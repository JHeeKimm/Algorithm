const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

for(let i=1; i<=input[0]; i++){
    const n = input[i].length - 1;
    console.log(input[i][0] + input[i][n]);    
}

