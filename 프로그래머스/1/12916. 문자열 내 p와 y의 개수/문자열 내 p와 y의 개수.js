function solution(s){
    // 1. 문자열 소문자로 변환
    // 2. 배열로 변환
    // 3. filter로 'p'와 'y'의 개수 세고 비교해서 리턴
    const lowerStr = s.toLowerCase().split('')
    const count_p = lowerStr.filter((e) => e==='p').length
    const count_y = lowerStr.filter((e) => e==='y').length

    if(count_p !== count_y) return false
    if(count_p === count_y || (count_p === 0 && count_y === 0)) return true
}