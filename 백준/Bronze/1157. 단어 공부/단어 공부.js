let input = require('fs').readFileSync('/dev/stdin').toString().toUpperCase().trim().split('');
let obj = {};
input.forEach((x)=>{
    obj[x] = (obj[x] || 0)+1;
});

let result = '';
let count = 0;
for( key in obj){
    if(obj[key]>count){
        count = obj[key];
        result = key;
    }else if(obj[key] === count){
        result = '?';
    }
}
console.log(result);