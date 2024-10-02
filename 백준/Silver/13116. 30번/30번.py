# 1. 입력: 
#   - 첫째 줄: 테스트 케이스의 수 T
#   - 둘째 줄~: 각 테스트 케이스에 대한 두 개의 정수 a b
# 2. 출력
#   - 문제의 첫 번째 칸에 a를, 두 번째 칸에 b를 넣었을 때의 답을 한 줄에 하나씩 출력

# 3. 문제 해결
#   - k: 1에서 a까지 가는 경로와 1에서 b까지 가는 경로에 공통으로 포함되는 수 중 최댓값
#   -> a와 b의 부모노드가 공통되는 값이 되겠다.
#   -> a의 부모 노드는 a//2 값이다.

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    while True:
        if a == b: # 업데이트한 a와 b 부모 노드가 같으면 출력하고 반복문 나오기
            print(10*a)
            break
        elif a > b: # a가 b보다 더 크면 a를 반으로 나눠줘서 부모노드 값으로 업데이트
            a //= 2
        elif a < b: # b가 a보다 더 크면 b를 반으로 나눠줘서 부모노드 값으로 업데이트
            b //= 2