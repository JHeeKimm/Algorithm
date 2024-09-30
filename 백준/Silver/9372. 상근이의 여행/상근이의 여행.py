# 1. 입력
#   - 첫째 줄: 테스트 케이스의 수 T(T ≤ 100)
#   - 둘째 줄: 국가의 수 N(2 ≤ N ≤ 1,000)과 비행기의 종류 M(1 ≤ M ≤ 10,000)
#   - ~ M개의 줄: a와 b(1 ≤ a,b ≤ n; a ≠ b) 
#       - a와 b를 왕복하는 비행기가 있다는 것을 의미
#       - 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다

# 2. 출력
#   - 모든 국가를 여행하기 위해 타야하는 비행기 종류의 최소 개수 출력 

# 3. 문제 해결
#   - 가장 적은 종류의 비행기를 타고 모든 국가들을 여행하는 경우 수
#   -> 각 지역을 1번씩만 방문하기

import sys
from collections import deque

input = sys.stdin.readline

def dfs(node, count):
    visited[node] = 1 # 현재 노드 방문 표시

    for i in graph[node]:
        if visited[i] == 0:
            count = dfs(i, count+1)
    return count


t = int(input()) # 테스트 케이스 수
for _ in range(t):
    n, m = map(int, input().split()) # 국가의 수 n, 비행기의 종류 m
    graph = [[] for _ in range(n+1)] # 각 국가 간의 비행 경로를 저장할 인접 리스트
    visited = [0]*(n+1)
    
    for _ in range(m):
        a, b = map(int, input().split()) # a, b 국가
        graph[a].append(b) # 양방향 저장
        graph[b].append(a)

    print(dfs(1, 0))