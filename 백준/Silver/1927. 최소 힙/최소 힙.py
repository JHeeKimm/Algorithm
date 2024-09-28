# 1. 입력
#   - 첫째 줄: 연산의 개수 N(1<=N<=100,000)
#   - 둘째 줄 ~ N개의 줄: 연산에 대한 정보인 정수 X (음수는 아님)
#       - X가 자연수 -> X값 추가 연산
#       - X가 0 -> 배열에서 가장 작은 값 출력하고, 그 값을 배열에서 제거

# 2. 출력
#   - 입력에서 0이 주어진 횟수만큼 답을 출력한다
#   - 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 하는 경우엔 0 출력

# 3. 문제 해결
#   - 최소 힙을 이용해 연산 프로그램을 작성을 하라고 한다
#   - x가 0인 경우를 세고 그 횟수만큼 출력해야한다?
#   -> 0일 때 가장 작은 값 출력하고 제거, 0이 아닐 때 추가
#   -> 비어있는데 출력하라고 하면 0 출력

import sys, heapq
input = sys.stdin.readline

n = int(input())
min_num = [] # 빈 배열로 시작하기?
x = 0

for _ in range(n):
    x = int(input().rstrip())

    if x != 0:      # 주어진 수가 0이 아니면 힙에 추가
        heapq.heappush(min_num, x)
    else:           # 주어진 수가 0이고 
        if min_num: # 배열이 있으면 출력 및 제거, 
            print(heapq.heappop(min_num))
        else:
            print(0) # 배열이 없으면 0출력