import heapq, sys
input = sys.stdin.readline

n = int(input())
dasom = int(input()) # 다솜 (기호 1번)을 찍으려는 사람의 수

hq = []

for _ in range(n-1):
    vote = int(input())
    heapq.heappush(hq, -vote) # 최대힙으로 하기 위해 '-' 붙임

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