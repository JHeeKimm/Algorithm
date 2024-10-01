# 1. 입력
#   - 첫째 줄: n
#   - 둘째 줄 ~ n개의 줄: 유형 1이나 2
#       - 유형 1: 1 a (1명, 학생 번호 a)
#       - 유형 2: 2   (1인분이 준비되어 1명 식사)

# 2. 출력
#   - 식당 입구에 줄을 서서 대기하는 학생 수가 최대가 되었던 순간의 학생 수와
#   - 식당 입구의 맨 뒤에 대기 중인 학생의 번호를 공백을 두고 출력
#   - 대기하는 학생 수가 최대인 경우가 여러 번이라면 맨 뒤에 줄 서 있는 학생의 번호가 가장 작은 경우를 출력

# 3. 문제 해결
#   - 먼저 먹고 먼저 나간다 -> 선입선출 append, popleft
#   - 입력 받은 대기 학생 번호를 넣어주기
#   - 대기줄의 맨 뒤 학생 번호와 대기자 수 넣어주기
#   - 반복문 돌면서 값 갱신해주기

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
waiting = deque()
max_waiting = [0, 0]

for _ in range(n):
    a = list(map(int,input().split()))

    if a[0] == 1:
        waiting.append(a[1])
    elif a[0] == 2:
        waiting.popleft()
    
    if len(waiting) > max_waiting[0]: # 현재 줄이 더 길다면
        max_waiting[0] = len(waiting) # 최대 줄 길이 갱신
        max_waiting[1] = waiting[-1] # 현재 마지막 학생 번호 갱신
    elif max_waiting[0] == len(waiting): # 최대 줄이 여러 번인 경우 처리
        max_waiting[1] = min(max_waiting[1], waiting[-1]) # 작은 값으로 갱신

print(max_waiting[0], max_waiting[1]) # 공백을 두고 출력