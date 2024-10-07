# 1. 입력
#   - 첫째 줄: 컴퓨터의 수 N(1~100)
#   - 둘째 줄: 연결된 컴퓨터 쌍의 수 M
#   - ~ M개의 줄: 연결된 번호 쌍

# 2. 출력
#   - 1번 컴퓨터가 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수

# 3. 문제 해결
#   - 연결된 컴퓨터를 리스트에 담아서 방문하며 1로 방문 표시해준다.
#   - 연결된 개수를 확인하는 문제니 방문 표시한 수를 합하고 1번은 제외하고 출력하면 되겠다.

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1) 

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = 1 # 1번 컴퓨터 방문 표시
q = deque([1])
while q:
    c = q.popleft()
    for i in graph[c]:
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)

print(sum(visited)-1) # 1번을 제외한 개수 출력