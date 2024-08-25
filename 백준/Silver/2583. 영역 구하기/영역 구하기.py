from collections import deque
import sys

input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[0]*M for _ in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1
            
def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque([(x, y)])
    graph[x][y] = 1
    area_cnt = 0
    
    while q:
        x, y = q.popleft()
        area_cnt += 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny))
                
    return area_cnt
            
result = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            area_cnt = bfs(i, j)
            result.append(area_cnt)
result.sort()

print(len(result))
print(' '.join(map(str, result)))