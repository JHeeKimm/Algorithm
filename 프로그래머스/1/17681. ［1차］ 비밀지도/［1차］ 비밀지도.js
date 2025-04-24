// 1. 입력: 지도 한 변의 크기 n, 정수 배열 arr1, arr2
// 2. 출력: '#'과 ' '으로 구성된 문자열 배열
// 3. 문제풀이
// 3-1. 두 개의 지도 배열을 합쳐 하나의 지도가 나온다.
// 3-2. 10진수를 2진수로 변환한다.(n 자릿수 일치시키기)
// 3-3. 1은 벽, 0은 공백으로 보고, 하나라도 1이면 '#' 모두 0이면 공백으로 한다.

function changeBinary(arr, count){
    return arr.map((num)=>
        num.toString(2).padStart(count, 0)
    )
}

function solution(n, arr1, arr2) {
    let result = [];
    arr1 = changeBinary(arr1, n)
    arr2 = changeBinary(arr2, n)
    
    for(let i=0; i<n; i++){
        let line = ''
        for(let j=0; j<n; j++){
            if(arr1[i][j] === '1' || arr2[i][j] === '1'){
                line += '#'
            }else{
                line += ' '
            }
        }
        result.push(line)
    }
    
    return result;
}