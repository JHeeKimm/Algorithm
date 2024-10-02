# 1. 입력
#   - 첫째 줄: 각각 영역의 세로와 가로의 길이 R, C (3 ≤ R, C ≤ 250)
#   - 둘째 줄 ~ 각 R줄: C개의 문자가 주어짐
#       - 빈 공간을 '.' 울타리를 '#', 늑대를 'v', 양을 'k'

# 2. 출력
#   - 살아남게 되는 양과 늑대의 수를 각각 순서대로 출력

# 3. 문제 해결
#   - 한 구역 안에 양이 늑대보다 많으면 양이 살고, 수가 같거나 늑대가 많으면 늑대가 산다.
#   -> 방문 여부 확인 필요
#   -> 그래프에서 울타리로 둘러싸인 각 영역의 양과 늑대 수를 확인 필요
#   -> 상하좌우 이동하며 확인하고, 범위 안에 있는 방문한적 없는 울타리가 아닌 좌표를 큐에 담는다
#   -> 큐에서 꺼내와서 양인지 늑대인지 확인해서 카운트 해준다
#   -> 양과 늑대의 수를 비교해서 살아남게 한다

from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

visited = [[False]*c for _ in range(r)]
directions = [(0,-1), (0,1), (-1,0), (1,0)]
total_wolf, total_sheep = 0, 0

def bfs(x, y):
    global total_wolf, total_sheep
    wolf, sheep = 0, 0
    visited[x][y] = True
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        if graph[x][y] == 'v':
            wolf += 1
        elif graph[x][y] == 'k':
            sheep += 1

        for dx, dy in directions: # 상하좌우 이동하며 확인
            nx, ny = x+dx, y+dy
            if 0<=nx<r and 0<=ny<c and graph[nx][ny] != '#' and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))

    if wolf >= sheep:
        total_wolf += wolf
    else:
        total_sheep += sheep

# 방문하지 않았고 울타리가 아닌 경우 탐색 실행
for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] != '#':
            bfs(i, j)
print(total_sheep, total_wolf)