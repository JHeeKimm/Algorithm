const input = require('fs').readFileSync('/dev/stdin').toString();
const abc = "abcdefghijklmnopqrstuvwxyz".split('');
let result = [];
for(let i=0; i<abc.length; i++){
    result.push(input.indexOf(abc[i]));
}
console.log(result.join(' '));