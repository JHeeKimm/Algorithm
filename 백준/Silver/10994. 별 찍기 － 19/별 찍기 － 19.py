# 1. 입력 : N(1 ≤ N ≤ 100)

# 2. 로직
# 2-1. (4*N-3) x (4*N-3) 크기의 2차원 배열 만들고 공백으로 채운다
# 2-2. 별 채우기
# 2-2-1. length가 1이면, 1개의 별 출력
# 2-2-2. 위, 아래, 왼쪽, 오른쪽 테두리 채우기
# 2-2-3. 테두리를 제외하고 채울 공간이 있을 때만 재귀 호출로 채우기

# 3. 출력 : 첫째 줄부터 차례대로 별 출력

n = int(input())
length = 4*n-3
stars = [[' ']*length for _ in range(length)] # 배열 초기화

def add_star(x, y, length):
    if length == 1:
        stars[x][y] = '*'
        return
    
    # 테두리 채우기
    for i in range(length):
        stars[x][y+i] = '*' # 위 테두리
        stars[x+(length-1)][y+i] = '*' # 아래 테두리
        stars[x+i][y] = '*' # 왼쪽 테두리
        stars[x+i][y+(length-1)] = '*' # 오른쪽 테두리
        
    # 재귀 호출로 채우기
    if length-4 > 0: # 테두리를 제외하고 채울 공간이 있을 때만 재귀 호출
        add_star(x+2, y+2, length-4) # 공백을 두고 채워야하니 x+2, y+2로 이동

# 함수 초기 호출
add_star(0, 0, length)

# 한 줄씩 출력
for row in stars:
    print(''.join(row))