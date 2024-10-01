# 1. 입력
#   - 첫째 줄: 테스트 데이터 수 T
#   - 둘째 줄: 소설을 구성하는 장의 수 K
#   - 셋째 줄: 1~K장까지 수록한 파일 크기 K개

# 2. 출력
#   - 모든 장을 합치는데 필요한 최소비용(각 테스트 데이터마다 한 행에 출력)

# 3. 문제 해결
#   - 파일을 2개씩 합쳐서 임시 파일을 만들고 그 임시 파일들을 합치고
#   - 파일이 하나가 될때까지 수행
#   -> 작은 값들부터 더해줘야 누적값이 최소가 될 수 있을 것 같다
#   -> 최소 값들을 pop해서 더하고 다시 넣는다
#   -> 케이스마다 2행에 걸쳐 나오니 for문은 한 번만 해도 되겠다

import sys, heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    file = list(map(int, input().split()))
    heapq.heapify(file)

    result = 0
    while len(file)>1:
        c1 = heapq.heappop(file)
        c2 = heapq.heappop(file)
        result += (c1+c2)

        heapq.heappush(file, (c1+c2))

    print(result)