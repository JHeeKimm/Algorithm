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


def dfs(p):
    for i in graph[p]:
        if visited[i] == 0:
            visited[i] = visited[p]+1
            dfs(i)
dfs(a)
if visited[b] > 0:
    print(visited[b])
else:
    print(-1)