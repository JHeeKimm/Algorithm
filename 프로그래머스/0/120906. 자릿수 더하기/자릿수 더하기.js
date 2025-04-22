function solution(n) {
    let answer = 0;
    const str = n.toString()
    
    for(let i=0; i<str.length; i++){
        answer += Number(str[i])
    }
    return answer;
}