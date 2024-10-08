# 1. 입력
#   - 수빈이 위치 N(0 ≤ N ≤ 100,000), 동생 위치 K(0 ≤ K ≤ 100,000)

# 2. 출력
#   - 수빈이가 동생을 찾는 가장 빠른 시간

# 3. 문제 해결
#   - 수빈이가 x일 때 걷는다면 1초 후에 x-1 또는 x+1로 이동
#   - 순간이동을 한다면, 1초 후에 2*x로 이동
#   - 배열 크기만 정하면 방향 설정해서 bfs로 풀면 되겠다

from collections import deque
n, k = map(int, input().split())

visited = [0]*100001 # N,K 최대 크기+1로 배열 크기 지정

q = deque([n])
while q:
    x = q.popleft()
    if x == k:
        print(visited[x])
        break
    for nx in [x-1, x+1, 2*x]:
        if 0<=nx<100001 and not visited[nx]:
            visited[nx] = visited[x]+1
            q.append(nx)
