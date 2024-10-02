# 1. 입력: 
#   - 첫째 줄: 도로의 깊이 K -> 노드 레벨
#   - 둘째 줄~: 상근이가 방문한 빌딩의 번호가 들어간 순서대로 주어짐(중복 없음)

# 2. 출력
#   - K개의 줄에 걸쳐서, i번째 줄에는 레벨이 i인 빌딩의 번호 출력(왼쪽에서 오른쪽 순으로)
#   -> 각 레벨에 있는 번호 값 출력

# 3. 문제 해결
#   - 깊이가 K인 완전 이진 트리는 총 2K-1개의 노드로 이루어짐
#   - left->mid->right 순인거 보니 중위순회인 것 같다.
#   - 주어진 수의 가운데 값은 루트 노드이겠다.
#   - 루트 노드를 기준으로 왼쪽 트리와 오른쪽 트리를 나눠보자.

# 입력 받기
k = int(input())
buildings = list(map(int, input().split()))

# 트리 담을 배열 초기화
trees = [[] for _ in range(k)]

def binary_tree(buildings, level):
    mid = len(buildings)//2 # 루트 노드 인덱스
    trees[level].append(buildings[mid]) # 루트 노드 추가

    if len(buildings) == 1: # 재귀 탈출
        return
    
    binary_tree(buildings[:mid], level+1) # 왼쪽 트리 재귀 함수 호출
    binary_tree(buildings[mid+1:], level+1) # 오른쪽 트리 재귀 함수 호출

binary_tree(buildings, 0)

# 출력
for tree in trees:
    print(*tree)