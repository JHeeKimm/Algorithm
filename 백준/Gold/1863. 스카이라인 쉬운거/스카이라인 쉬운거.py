# 1. 입력
#   - 첫째 줄: n (고도가 바뀌는 지점의 좌표 개수)
#   - 둘째 줄 ~ n개의 줄: 스카이라인의 고도가 바뀌는 지점의 좌표 x y
#       - 첫 번째 지점의 x 좌표는 항상 1이다

# 2. 출력
#   - 최소 건물 개수

# 3. 문제 해결
#   - 태양이 질 때 보이는 건물들의 윤곽을 보고서 최소 몇 채인지 알아내는 프로그램 작성
#   - 건물 모양은 직사각형.. 
#   - 일단 y를 비교해서 y가 바뀔때 세서 건물 개수를 셀 수 있겠다
#   - 스택에 담아서 풀면 될 것 같다
#   -> 스택이 비었거나, y가 스택의 마지막 값보다 크면 건물이 시작되므로 스택에 추가
#   -> 스택이 비어있지 않고, y가 스택의 마지막 값보다 작으면 건물이 끝나므로 스택에서 제거, count 증가
#   -> 여기서 연속된 값은 스택에 넣지 않아야 하므로 예외처리 해준다.
#   -> 마지막에 0으로 끝나지 않으면 건물이 있는걸로 보고 더해줘야한다.

import sys
input = sys.stdin.readline

n = int(input())
stack = []
count = 0

for _ in range(n):
    x, y = map(int, input().split())

    while stack and y < stack[-1]: 
        count += 1
        stack.pop()
    if stack and y == stack[-1]: # 같은 높이가 나오면 스택에 넣지 않음
        continue
    elif not stack or y > stack[-1]:
        stack.append(y)

while stack:
    if stack[-1] > 0: # 스택에 남아 있는 값이 0보다 크면 카운트 증가
        count += 1
    stack.pop()

print(count)
