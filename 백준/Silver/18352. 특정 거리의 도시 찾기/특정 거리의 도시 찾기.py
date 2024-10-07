# 1. 입력
#   - 첫째 줄: 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
#   - 둘째 줄 ~ M개의 줄: 서로 다른 자연수 A B (1 ≤ A, B ≤ N) 
#           A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재함을 의미

# 2. 출력
#   - X 도시에서 출발해 도달할 수 있는 도시 중, 최단 거리가 K인 모든 도시의 번호
#   - 오름차순으로 출력
#   - 하나도 없으면 -1 출력

# 3. 문제 해결
#   - 단방향 그래프.. 인접 리스트를 만들어 연결된 도시 번호 담기
#   - 방문하면서 거리 갱신

from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [-1]*(n+1) # 도시간 거리 -1로 초기화
distance[x] = 0 # 시작 도시 거리 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v) # 단방향 그래프로 연결된 도시 번호 담기


q = deque([x]) # 출발 도시
while q:
    x = q.popleft()
    for i in graph[x]:
        if distance[i] == -1: # 방문한적 없는 도시인 경우
            distance[i] = distance[x] + 1 # 거리 갱신
            q.append(i)

# 최단 거리가 k인 도시 번호 담기(작은 번호부터 담으면서 오름차순 정렬됨)
result = [i for i in range(1, n+1) if distance[i] == k]

# 출력
print('\n'.join(map(str, result)) if result else -1)