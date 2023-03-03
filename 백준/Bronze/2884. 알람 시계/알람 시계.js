let [hour, minute] = require('fs').readFileSync('/dev/stdin').toString().split(' ').map(Number);
minute -= 45;

if(minute < 0){
    minute += 60;
    hour--;
    
    if(hour === -1){
        hour = 23;
    }
}else{
    if(hour === -1){
        hour = 23;
    }
}

console.log(`${hour} ${minute}`);