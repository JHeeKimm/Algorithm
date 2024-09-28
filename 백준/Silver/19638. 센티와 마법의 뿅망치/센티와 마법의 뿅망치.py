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