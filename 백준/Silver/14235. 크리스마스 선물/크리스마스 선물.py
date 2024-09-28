# 1. 입력
#   - 첫째 줄: 아이들, 거점지를 방문한 횟수 N(1<=N<=5,000)
#   - 둘째 줄 ~ N개의 줄: a와 a개의 숫자
#       - a: 거점지에서 충전한 선물 수
#       - ex) 2 3 2 -> 선물 2개 충전, 선물 가치 각각 3, 2
#       - a가 0 -> 아이들을 만난 것

# 2. 출력
#   - a가 0일 때마다(아이들을 만났을 때마다), 아이들에게 준 선물의 가치를 출력
#   - 만약 줄 선물이 없다면 -1 출력

# 3. 문제 해결
#   - 가장 높은 가치의 선물부터 준다 -> 최대힙!

import sys, heapq
input = sys.stdin.readline

n = int(input())
max_value = []

for _ in range(n):
    a = list(map(int, input().rstrip().split()))

    if a[0] == 0:
        if not max_value:
            print(-1)
            continue
        else:
            print(-heapq.heappop(max_value))
            continue
    
    for i in range(1, len(a)):
        heapq.heappush(max_value, -a[i])