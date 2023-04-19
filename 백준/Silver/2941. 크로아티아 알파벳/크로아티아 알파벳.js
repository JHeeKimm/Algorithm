const input = require('fs').readFileSync('dev/stdin').toString().trim();
let result = input;
let regex = [/c=/g, /c-/g, /dz=/g, /d-/g, /lj/g, /nj/g, /s=/g, /z=/g];
regex.map(el => result = result.replace(el, "w"));
console.log(result.length);