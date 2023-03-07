const input = require('fs').readFileSync('/dev/stdin').toString();
let result = '';
for(let i=1; i<=input; i++){
    result += "*"
    console.log(result);
}