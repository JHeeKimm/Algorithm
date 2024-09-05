# 1. 입력 : 세 정수 a, b, c가 한 줄씩 주어진다. 마지막 줄은 -1, -1, -1

# 2. 로직
# 2-1. 주어진 재귀 함수로는 시간이 오래걸리므로 같은 계산은 값을 저장해서 사용한다.
# 2-2. 3차원 배열 초기화 - 각 인덱스는 계산되지 않은 상태를 나타내기 위해 -1로 초기화한다.
# 2-3. 함수 w(a, b, c) - 주어진 조건에 맞게 재귀적으로 계산하고 저장된 값을 반환한다.

# 3. 출력 : 주어진 각각의 a, b, c에 대해서, w(a, b, c)
# 출력 형식은 'w(a, b, c) = 결과'

# 3차원 배열 초기화
arr = [[[-1]*21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: 
        return 1
    if a > 20 or b > 20 or c > 20: 
        return w(20, 20, 20)
    
    # 이미 계산된 값이 있는 경우
    if arr[a][b][c] != -1: 
        return arr[a][b][c]

    # 재귀 호출 및 값 저장
    if a < b < c:
        arr[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        arr[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return arr[a][b][c]

while True:
    # 입력 받기
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1: # -1 -1 -1일때 반복 종료
        break
    
    # 계산된 결과 출력
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')