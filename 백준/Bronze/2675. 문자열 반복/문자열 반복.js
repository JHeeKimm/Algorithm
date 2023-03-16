const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

for(let i=1; i<=input[0]; i++){
    let result = [];
    let [R, S] = input[i].split(' ');
    for(let j=0; j<S.length; j++){
        result.push(S[j].repeat(R));
    }
    console.log(result.join(''));
}