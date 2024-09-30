# 1. 입력
#   - 첫째 줄: 게임 구역의 크기 (2<=N<=3)
#   - 둘째 줄 ~ N개의 줄: 게임판의 구역(맵)
#       - 오른쪽 맨 아래 칸: 승리 지점, -1
#       - 나머지 칸: 0이상 100이하의 정수

# 2. 출력
#   - '쩰리'가 끝 점에 도달할 수 있으면 "HaruHaru", 아니면 "Hing" 출력

# 3. 문제 해결
#   - 새로운 점프 게임의 조건
#       - 가로와 세로의 칸 수가 같은 정사각형의 구역 내부에서만 이동 가능(외부로 나가면 패배)
#       - 이동 가능한 방향은 오른쪽과 아래 (위, 왼쪽으로 이동 불가) -> [(1,0), (0,1)]
#       - 맨 왼쪽 위 칸에서 출발해, 가장 오른쪽 아래 칸에 도달하면 승리로 게임 종료 -> [0][0]에서 출발
#       - 칸마다 쓰여있는 수만큼 한 번에 이동 가능
#   -> 칸과 좌표도 헷갈리고 문제 규칙도 헷갈렸다..
#   -> 칸에 적힌 수만큼 점프를 하는데, 오른쪽과 아래쪽으로 다 이동
#   -> 마지막 칸에 도달해야만 승리이고 벗어나서 도달하면 패배이다.
#   -> 시작 노드부터 인접한 노드를 탐색하고, 다음 노드로 이동? 이게 bfs인가?


from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def bfs(x, y):
    q = deque([(x,y)]) # 큐 만들고 시작점 넣기
    directions = [(1,0), (0,1)] # 이동 방향 오른쪽, 아래쪽
    
    while q:
        x, y = q.popleft() # 현재 위치 좌표

        if board[x][y] == -1: # 종료 지점인 경우
            return "HaruHaru"
        
        jump = board[x][y] # 현재 칸에 적힌 수

        for dx, dy in directions:
            nx, ny = x+dx*jump, y+dy*jump # 점프 수만큼 오른쪽과 아래쪽으로 이동

            # 판을 벗어나지 않고 방문하지 않은 경우에
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny] = True # 방문 true해주고
                q.append((nx,ny)) # 이동한 위치 좌표 큐에 담아주기

    return "Hing"

print(bfs(0,0))