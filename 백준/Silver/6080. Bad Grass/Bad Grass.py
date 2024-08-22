from collections import deque
import sys

# 상하좌우, 대각선 
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def bfs(x, y):
    queue = deque([(x, y)])
    grid[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<R and 0<=ny<C and grid[nx][ny]!=0:
                grid[nx][ny] = 0
                queue.append((nx, ny))
                
input = sys.stdin.readline
R, C = map(int, input().split())

grid = [list(map(int,input().split())) for _ in range(R)]

count = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] != 0:
            bfs(i, j)
            count += 1
print(count)
    