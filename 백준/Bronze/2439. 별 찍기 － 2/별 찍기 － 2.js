const input = require('fs').readFileSync('/dev/stdin').toString();

for(let i=0; i<input; i++){
    let result = '';
    
    for(let j=input-1; j>=0; j--){
        result += j<=i? '*' : ' ';
    }
    console.log(result);
}