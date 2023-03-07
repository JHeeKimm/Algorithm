const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

for(let i=0; i<input.length-2; i++){
    let nums = input[i].split(' ').map(Number);
    console.log(nums[0]+nums[1]);
}