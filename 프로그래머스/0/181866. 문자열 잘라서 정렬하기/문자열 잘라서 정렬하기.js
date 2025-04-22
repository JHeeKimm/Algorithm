function solution(myString) {
    let answer = [];
    // x 기준으로 잘라내고 배열로 만들기 -> 사전순으로 정렬
    // 빈 문자열은 제외
    answer = myString.split('x').filter(e=> e !== '').sort()
    
    return answer;
}