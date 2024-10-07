# 1. 입력
#   - 첫째 줄: 테스트 케이스의 개수
#   - 각 테스트 케이스의 첫째 줄: 체스판 한 변의 길이 l 
#   - 각 테스트 케이스의 둘째 줄: 나이트가 현재 있는 칸
#   - 각 테스트 케이스의 셋째 줄: 나이트가 이동하려고 하는 칸

# 2. 출력
#   - 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력

# 3. 문제 해결
#   - 시작 좌표에서 도착 좌표까지 이동해야 하는 최소 횟수 구하자.
#   - 이동 가능한 방향 좌표를 담고 8번 반복해 이동한다.
#   - 이동할 때마다 방문 표시 및 카운트 증가해주고, 도착 좌표에 도달하면 저장된 횟수 반환

from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_x, start_y, end_x, end_y):
    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [2,1,-1,-2,-2,-1,1,2]
    q = deque([(start_x, start_y)])

    while q:
        x, y = q.popleft()
        if x == end_x and y == end_y:
            return graph[x][y] 
        
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            
            if 0<=nx<l and 0<=ny<l and graph[nx][ny]==0 : # 체스판 범위 안에 있고, 방문하지 않았으면
                graph[nx][ny] = graph[x][y] + 1 # 방문 표시 및 이동 횟수 증가
                q.append((nx, ny))

t = int(input())
for _ in range(t):
    l = int(input().rstrip())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    graph = [[0]*l for _ in range(l)]

    print(bfs(start_x, start_y, end_x, end_y))