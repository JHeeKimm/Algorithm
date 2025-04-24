// 1. 수포자 삼인방의 패턴을 배열에 담는다.
// 2. 반복문으로 정답 배열과 패턴 배열을 비교해 맞힌 문제 수를 센다.
// 3. 가장 많이 맞힌 문제수 확인한다.
// 4. max 값인 사람의 번호만 새 배열에 담아 출력한다.

function solution(answers) {
    const one = [1, 2, 3, 4, 5]
    const two = [2, 1, 2, 3, 2, 4, 2, 5]
    const three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    let score = [0,0,0]
    
    for(let i=0; i<answers.length; i++){
        if(answers[i] === one[i % one.length]) score[0]++
        if(answers[i] === two[i % two.length]) score[1]++
        if(answers[i] === three[i % three.length]) score[2]++
    }

    let result = []
    const maxValue = Math.max(...score)
    for(let i=0; i<3; i++){
        if(maxValue === score[i]) result.push(i+1)
    }
    
    return result;
}