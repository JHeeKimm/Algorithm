# 1. 입력
#   - 'B' 불이 난 헛간, 'L' 호수, 'R' 바위가 하나씩 구성된 10x10 행열

# 2. 출력
#   - 실행 가능한 버킷 여단을 구성하는 데 필요한 최소 소의 수

# 3. 문제 해결
#   - 호수에 소가 인접해있어야 하고, 바위는 피하고 '.'인 곳만 소를 위치 시켜야한다.
#   - 소들은 상하좌우로 인접해있어야 버킷을 옮길 수 있다.
#   - 호수에서 헛간까지의 최단 경로 찾기
#   -> 상하좌우로 이동하면서 방문 거리 증가 시키기, 'L'까지 도달하면 갱신한 거리 길이 반환

from collections import deque
import sys
input = sys.stdin.readline

graph = [list(input().strip()) for _ in range(10)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<10 and 0<=ny<10:
                if graph[nx][ny] == 'L':
                    return graph[x][y]
                elif graph[nx][ny] == '.':
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

for i in range(10):
    for j in range(10):
        if graph[i][j] == 'B': # 헛간에서 탐색 시작
            print(bfs(i, j))