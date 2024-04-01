const input=require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(x=>x.split(" "));
const table = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
let gradePointSum = 0;
let gradeTotal = 0;
for(let [a,b,c] of input){
    if(c==='P') continue;
    gradeTotal += +b;
    gradePointSum += b*table[c];
}
console.log(gradePointSum/gradeTotal)