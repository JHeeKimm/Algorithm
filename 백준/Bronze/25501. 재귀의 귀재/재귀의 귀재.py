# 1. 입력
# 1-1. 첫째 줄: 테이스케이스의 개수 `T`
# 1-2. 둘째 줄 부터 T개의 줄: 알파벳 대문자로 구성된 문자열 `S`

# 2. 로직
# 2-1. 팰린드롬인지 재귀적으로 판별한다 -> 문자열을 왼쪽과 오른쪽 끝부터 안쪽으로 좁혀가며 같은지 다른지 확인한다
# 2-2. 다음 줄의 문자열을 받아올 때마다 count를 0으로 초기화한다

# 3. 출력 : 팰린드롬 판별 결과와 재귀 함수 호출 횟수를 한 줄에 공백으로 구분하여 출력
# 3-1. 주어진 문자열이 팰린드롬이면 1, 팰린드롬이 아니면 0을 반환
# 3-2. 팰린드롬 판별 과정에서 재귀 함수가 몇 번 호출됐는지 횟수 반환

T = int(input())

def recursion(s, l, r):
    global count
    count += 1

    if l>=r:
        return 1, count
    elif s[l] != s[r]:
        return 0, count
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(T):
    s = input().strip()
    count = 0 # 각 줄마다 count 초기화
    result, count = isPalindrome(s)
    print(result, count)