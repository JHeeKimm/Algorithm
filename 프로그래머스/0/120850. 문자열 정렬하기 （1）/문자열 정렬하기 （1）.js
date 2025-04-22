function solution(my_string) {
    let answer = [];
    // 문자열 배열로 -> 숫자인 문자만 필터 -> 숫자 변환 후 오름차순 정렬
    answer = my_string.split('').filter(e => !isNaN(e)).map(e => Number(e)).sort((a,b)=>a-b)
    return answer;
}