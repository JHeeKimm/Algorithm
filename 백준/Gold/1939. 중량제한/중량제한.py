# 1. 입력
#   - 첫째 줄: 섬 개수 N(2 ≤ N ≤ 10,000), M(1 ≤ M ≤ 100,000)
#   - ~ M개의 줄: 세 정수 A, B(1 ≤ A, B ≤ N), C(1 ≤ C ≤ 1,000,000,000)
#       - A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미
#   - 마지막 줄: 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수

# 2. 출력
#   - 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값 구하기

# 3. 문제 해결
#   - 다익스트라가 아닐까 했지만 분류에 이분 탐색이라고 되어 있다..
#   - 중량 제한의 최솟값, 최댓값을 start, end로 하고,
#   - mid가 한 번 이동에 옮길 수 있는 중량
#   - 탐색하면서 mid가 다리의 중량보다 작은지 아닌지에 따라 
#     mid와 end 값을 조절하며 반환해야하는 중량값을 찾아야겠다

from collections import deque
import sys
input = sys.stdin.readline

def bfs(mid):
    q = deque([i1])
    visited = [False]*(n+1) # 방문 확인 변수 각 탐색마다 False로 초기화
    visited[i1] = True # 섬1 방문 표시

    while q:
        now = q.popleft()
        
        if now == i2: # 섬2에 도착했으면 True 반환
            return True
        for node, weight in graph[now]:
            if not visited[node] and mid <= weight:
                visited[node] = True
                q.append(node)
    return False

# 입력 받기
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)] # 연결 다리 정보 넣어줄 배열 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 연결 정보, 중량이랑 같이 담기
    graph[b].append((a, c))

i1, i2 = map(int, input().split()) # 섬1, 섬2

start, end = 1, 1000000000 # 중량의 최솟값, 최댓값(1 ≤ C ≤ 1,000,000,000)

result = 0
while start <= end:
    mid = (start+end)//2

    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)