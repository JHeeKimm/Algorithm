# 1. 입력
#   - 테스트 케이스의 개수 T
#   - 각 테스트 케이스의 첫째 줄: 배추밭 가로 M, 세로 N, 배추 위치 개수 K
#   - 각 테스트 케이스의 K개의 줄: 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)

# 2. 출력
#   - 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 수

# 3. 문제 해결
#   - 상하좌우 인접한 곳은 배추흰지렁이 한 마리면 되겠다
#   - 세로 길이가 행, 가로 길이가 열?

from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, i, j):
    q = deque([(i, j)])
    graph[i][j] = 0 # 방문 표시(빈 밭)

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and graph[nx][ny]==1:
                graph[nx][ny] = 0
                q.append((nx, ny))

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 위치 수 
    graph = [[0]*n for _ in range(m)]

    count = 0 # 지렁이 카운트 변수
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(graph, i, j) # 탐색 호출
                count += 1
    
    print(count)
