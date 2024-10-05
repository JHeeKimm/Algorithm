# 1. 입력
#   - 첫째 줄: 정점의 수 N, 간선의 수 M, 시작 정점 R
#   - 둘째 줄 ~ M개의 줄: u v   (1 ≤ u < v ≤ N, u ≠ v)
#                       정점 u와 정점 v의 가중치 1인 양방향 간선을 나타냄

# 2. 출력
#   - i번째 줄에는 정점 i의 방문 순서를 한 줄씩 출력
#   - 시작 정점에서 방문할 수 없는 경우 0을 출력

# 3. 문제 해결
#   - 무방향 그래프이고, 인접 정점인데 dfs로 풀라고요?!
#   - 정점 u, v의 연결 정보를 담고, 
#   - 시작 정점부터 출발해서 그것의 인접 정점을 오름차순으로 방문한다.
#   - 연결 안되어 있는 정점은 방문이 어려우니 0 출력해준다.
#   - visited를 0으로 넣어주고 방문하면서 count 횟수를 재할당 해준다
#   - 인접 정보가 없는 번호의 정점은 재할당 안되고 0인 상태가 될테니..

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(V):
    global count
    visited[V] = count # 방문한 경우 카운트 수로 재할당
    graph[V].sort() # 인접정점 오름차순 정렬

    for i in graph[V]:
        if visited[i] == 0: # 방문한 적 없는 경우
            count += 1
            dfs(i)

# 입력 받기
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)] # 간선 정보 담을 변수
visited = [0]*(n+1) # 정점 방문 체크 변수, 정점 번호가 1부터 시작하므로 n+1

count = 1 # 시작 정점의 방문 순서 넣어줌

# 입력 받아와서 양방향 간선 정보 넣어주기
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 시작 정점 전달해서 함수 실행
dfs(r)
# 출력
for i in range(1, n+1):
    print(visited[i])