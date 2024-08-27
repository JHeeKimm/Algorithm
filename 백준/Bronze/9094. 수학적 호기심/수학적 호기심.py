# 1. 입력
# 첫째 줄 `T` : 테스트 케이스 개수
# 둘째 줄부터 `n`, `m` : T개의 각 테스트 케이스가 한 줄씩 나옴. 0보다 크고 100보다 작은 정수.

# 2. 로직
# 2-1. `0 < a < b < n` 를 만족하는 모든 쌍 `(a, b)` 확인
# 2-2. `(a^2 + b^2+m)/(ab)`의 결과가 정수인지 확인

# 3. 출력
# 각 테스트 케이스마다 문제의 조건을 만족하는 (a, b)쌍의 개수를 한 줄씩 출력

def count_pairs(n, m):
    count = 0
    for a in range(1, n):
        for b in range(a+1, n):
            if(a**2 + b**2 + m)%(a*b) == 0:
                count += 1
    return count

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    result = count_pairs(n, m)
    print(result)