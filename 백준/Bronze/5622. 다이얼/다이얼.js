const input = require('fs').readFileSync('/dev/stdin').toString().split('');
const dial = {
    ABC: 3,
    DEF: 4,
    GHI: 5,
    JKL: 6,
    MNO: 7,
    PQRS: 8,
    TUV: 9,
    WXYZ: 10,
};
let seconds = 0;
for(let i=0; i<input.length; i++){
    for(key in dial){
        if(key.includes(input[i])){
           seconds += dial[key];
       }
    }
}
console.log(seconds);