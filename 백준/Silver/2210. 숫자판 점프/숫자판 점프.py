# 1. 입력
#   - 다섯 개의 줄에 다섯 개의 정수로 숫자판이 주어짐

# 2. 출력
#   - 만들 수 있는 서로 다른 여섯 자리의 수들의 개수 출력

# 3. 문제 해결
#   - 5x5 숫자판의 임의의 위치에서 인접한 네 방향으로 다섯 번 이동했을 때,
#   - 각 칸에 적힌 숫자를 붙여 만든 서로 다른 6자리 수...
#   - 한 번 거쳤던 칸을 다시 거쳐도 된다? 이건 뭐지..
#   -> 네 방향이라 했으니 좌표 문제인 것 같다

board = [list(input().split()) for _ in range(5)] # 입력 받기
num_set = set() # 서로 다른 여섯 자리 수들을 담을 예정

directions = [(0,-1), (0,1), (-1,0), (1,0)]

def dfs(x, y, num):
    if len(num) == 6: # 자릿수가 6자리가 되면 탈출
        num_set.add(num)
        return 
        
    for dx, dy in directions: 
        nx, ny = x+dx, y+dy # 상하좌우 방향 이동
        
        if 0<=nx<5 and 0<=ny<5: # 범위 벗어나지 않는 경우
            dfs(nx, ny, num+board[nx][ny]) # 6자리가 될 때까지 재귀

# 입력 값을 확인해서 함수 호출
for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(num_set))