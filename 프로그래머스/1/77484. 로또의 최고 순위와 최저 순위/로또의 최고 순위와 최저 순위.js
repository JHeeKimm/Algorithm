// 1. 입력: 민우 로또 번호 배열 lottos, 당첨 번호 배열 win_nums
// 2. 출력: 당첨 가능한 최고 순위와 최저 순위를 담은 배열
// 3. 문제 접근
// 3-1. lottos 배열에서 0은 알아 볼 수 없는 번호 
// 3-2. 필터해서 일치하는 요소 개수 -> 최저 개수
// 3-3. 최저에 0의 개수만큼 더해주면 -> 최고 개수

function solution(lottos, win_nums) {
    const minCount = lottos.filter(e=>win_nums.includes(e)).length
    const zeroCount = lottos.filter(e=>!e).length
    const min = 7-minCount >= 6 ? 6 : 7-minCount
    const max = min-zeroCount < 1 ? 1: min-zeroCount
    
    return [max, min];
}