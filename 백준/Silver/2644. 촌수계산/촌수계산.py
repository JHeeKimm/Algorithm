# 1. 입력
#   - 첫째 줄: 전체 사람 수 n
#   - 둘째 줄: 촌수 계산해야하는 두 사람의 번호
#   - 셋째 줄: 부모 자식들 간의 관계 개수 m
#   - 넷째 줄 ~ : x y (x는 y의 부모 번호)

# 2. 출력
#   - 두 사람의 촌수를 나타내는 정수 출력
#   - 관계가 없으면 -1 출력

# 3. 문제 해결
#   - 부모-자식 1촌, 나와 할아버지 2촌, 나와 아버지 형제들 3촌 
#   - visited -1해놓고 방문하면서 촌수 계산

from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
n = int(input()) # 총 인원 수
a, b = map(int, input().split()) # 촌수 계산해야하는 사람들 번호
m = int(input()) # 부모 자식 관계 수

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(a, b):
    q = deque([a])
    while q:
        p = q.popleft()

        if p == b:
            return visited[b]
        
        for i in graph[p]:
            if visited[i] == 0:
                visited[i] = visited[p] + 1
                q.append(i)
    return -1

print(bfs(a, b))
