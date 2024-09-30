# 1. 입력
#   - 첫째 줄: R(1 <= R <= 100) 행과 C(1 <= C <= 100) 열이 공백으로 구분되어 주어짐
#   - 둘째 줄 ~ R+1: '#' 또는 ''인 C 문자

# 2. 출력
#   - 덩어리 수 

# 3. 문제 해결
#   - 행과 열로 이루어진 농부 존에서 풀 덩어리의 개수를 세자. -> 인접 행렬 그래프?
#   - 각 덩어리는 하나의 '#' 또는 두 개의 '#'로 나오는데,
#   - 두 개의 '#'은 한 행에 연달아 나올 수도 있고, 두 행에 같은 열에 나올 수 있다. -> 상하좌우 확인하기
#   -> 행*열 2차원 배열로 초기화하고 '#'이 있는지 확인하고 카운트하기
#   -> 상하좌우로 인접한 '#'은 한 덩어리로 보고 한 번만 카운트한다.

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
pasture = [list(input().strip()) for _ in range(r)] # 입력값 2차원 배열로 담기

# 상하좌우로 인접한 '#'을 확인하는 함수
def search(x, y):
    pasture[x][y] = '.' # 확인한 곳은 '.'으로 변경
    direction = [(0,-1), (0,1), (-1,0), (1,0)] # 상하좌우 확인을 위해 
    for dx, dy in direction:
        nx, ny = x+dx, y+dy # 상하좌우로 이동해 인접한 곳에 '#'확인
        if 0<=nx<r and 0<=ny<c and pasture[nx][ny] == '#':
            search(nx, ny) # 재귀 함수 호출
    
count = 0
for x in range(r):
    for y in range(c):
        if pasture[x][y] == '#':
            search(x, y)
            count += 1 # 한 덩어리씩 카운트 증가

print(count)