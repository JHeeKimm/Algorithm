const input = require('fs').readFileSync('/dev/stdin').toString().trim();
let result = '';
for (let i=0; i<=Math.floor(input.length/2); i++) {
  let a = input[i];
  let b = input[input.length-1-i];
  if(a !== b){
      result = 0;
      break;
  }else{
      result = 1;
  }
}
console.log(result);