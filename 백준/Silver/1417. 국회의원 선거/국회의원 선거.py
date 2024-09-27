# 1. 입력
#   - 첫째 줄: 후보의 수 N
#   - 둘째 줄 ~ N개의 줄: 기호 n번을 찍으려는 사람의 수

# 2. 출력
#   - 다솜이가 매수해야 하는 사람의 최솟값 

# 3. 문제 해결
#   - 다솜이는 기호 1번
#   - 다솜이 득표수가 가장 많아야겠으니 최대힙
#   - 매수해야 하는 사람의 최솟값은 카운트로 해준다

import heapq

n = int(input())
dasom = int(input()) # 다솜 (기호 1번)을 찍으려는 사람의 수

hq = []

for _ in range(n-1):
    vote = int(input())
    heapq.heappush(hq, -vote)

count = 0
while hq:
    # 가장 많은 득표수 가져오기
    vote = -heapq.heappop(hq)

    # 다솜이가 표가 많다면 종료
    if vote < dasom:
        break

    # 매수 -> 가장 많은 표 -1, 다솜 표 +1, 카운트 +1
    vote -= 1
    dasom += 1
    count += 1

    # 줄어든 수 다시 넣음
    heapq.heappush(hq, -vote) 

print(count)