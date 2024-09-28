# 1. 입력
#   - 첫째 줄: 센티를 제외한 인구수 N, 센티의 키 정수 H, 뿅망치 횟수 제한 T
#   - 둘째 줄 ~ N개의 줄: 각 거인의 키 정수 H

# 2. 출력
#   - 마법 뿅망치를 사용해 센티가 다른 거인보다 키가 크게 할 수 있는 경우 'YES', 뿅망치 최소 사용 횟수
#   - 아니면 'NO', 뿅망치 사용 후 가장 큰 거인의 키 출력

# 3. 문제 해결
#   - 센티가 가장 키가 크게 해야 한다 -> 최대힙
#   - 뿅망치 횟수가 있고, 최소로 사용해야 한다 -> 카운트
#   - 뿅망치를 맞으면 키가 반으로 줄어든다
#   - 키가 1이면 영향이 없으니 예외처리 해주기
#   - while문 조건을 뭘로 해줘야할까..?

import sys, heapq
input = sys.stdin.readline

n, centi, t = map(int, input().split()) # 비교할 인구수, 센티 키, 횟수제한
max_h = []
count = 0

for _ in range(n):
    heapq.heappush(max_h, -(int(input()))) # 최대힙 구현을 위해 음수로 저장 

while max_h and centi <= -max_h[0] and count < t:
    giant = -heapq.heappop(max_h)

    if giant == 1: # 거인 키가 1이면 뿅망치 영향이 없음
        heapq.heappush(max_h, -giant) # 왜 다시 넣어야 할까..?
        break
    giant = giant // 2 # 반으로 줄이기
    count += 1
    
    heapq.heappush(max_h, -giant) # 줄인 값 다시 넣기

if -max_h[0] < centi: 
    print(f"YES\n{count}")
else: 
    print(f"NO\n{-max_h[0]}")