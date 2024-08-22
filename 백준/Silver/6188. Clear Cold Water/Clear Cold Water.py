import sys
from collections import deque
input = sys.stdin.readline

N, C = map(int, input().split())
connections = [tuple(map(int, input().split())) for _ in range(C)]

def calculate_distances(N, connections):
    tree = [[] for _ in range(N+1)]
    
    for E, B1, B2 in connections:
        tree[E].append(B1)
        tree[E].append(B2)
        
    distances = [-1]*(N+1)
    queue = deque([1])
    distances[1] = 1
    
    while queue:
        current = queue.popleft()
        current_distance = distances[current]
        
        for neighbor in tree[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)
    
    for i in range(1, N+1):
        print(distances[i])

calculate_distances(N, connections)