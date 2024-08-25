from collections import deque
import sys

def bfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = deque([(x, y)])
    grid[x][y] = '.'
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<H and 0<=ny<W and grid[nx][ny]=='#':
                grid[nx][ny] = '.'
                queue.append((nx, ny))
                
input = sys.stdin.readline
T = int(input().strip())

for _ in range(T):
    H, W = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]
    
    count = 0
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                bfs(i, j)
                count += 1
    print(count)