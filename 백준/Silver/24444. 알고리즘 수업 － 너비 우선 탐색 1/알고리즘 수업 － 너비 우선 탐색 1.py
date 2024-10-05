# 1. 입력
#   - 첫째 줄: 정점의 수 N, 간선의 수 M, 시작 정점 R
#   - 둘째 줄 ~ M개의 줄: u v   (1 ≤ u < v ≤ N, u ≠ v)
#                       정점 u와 정점 v의 가중치 1인 양방향 간선을 나타냄

# 2. 출력
#   - i번째 줄에는 정점 i의 방문 순서를 한 줄씩 출력
#   - 시작 정점에서 방문할 수 없는 경우 0을 출력

# 3. 문제 해결
#   - 무방향 그래프이고, 인접 정점 문제인데 bfs로 풀기 -> 큐
#   - u v 간선 정보 담고, 방문하면서 인접 정점 방문 순서 카운트 수로 업데이트 하고 큐에 담기
#   - 큐에서 꺼내오면서 다음 인접 정점 방문하는거 반복

from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)] # 간선 정보 담을 변수
visited = [0]*(n+1) # 정점 방문 체크 변수, 정점 번호가 1부터 시작하므로 n+1

# 입력 받아와서 양방향 간선 정보 넣어주기
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque([r]) 
visited[r] = 1 # 시작 정점 순서 1
count = 1
while q:
    now = q.popleft()
    graph[now].sort()
    for i in graph[now]:
        if visited[i] == 0:
            count += 1
            visited[i] = count
            q.append(i)

for i in range(1, n+1):
    print(visited[i])