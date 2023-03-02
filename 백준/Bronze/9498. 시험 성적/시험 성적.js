const input = require('fs').readFileSync('/dev/stdin').toString();
const num = parseInt(input);
if(num>89){
    console.log('A');
}else if(num>79){
    console.log('B');
}else if(num>69){
    console.log('C');
}else if(num>59){
    console.log('D');
}else{
    console.log('F');
}
