# 1. 입력: N (1 ≤ N ≤ 100)
# 2. 로직
# 2-1. 첫 번째부터 N번째 줄까지는 별의 개수가 증가한다.
# 2-2. N+1번째부터 마지막 줄까지는 별의 개수가 감소한다.
# 3. 출력: 별 + 공백 + 별 한 줄씩 출력

N = int(input())

# 별의 개수가 1부터 N까지 1씩 증가하면서 반복
for i in range(1, N+1):
    stars = '*'*i
    spaces = ' '*((N-i)*2)
    print(stars + spaces + stars)

# 별의 개수가 N-1부터 1까지 1씩 감소하면서 반복
# 역방향으로 반복되기 때문에 종료값을 0으로 해야 1까지 반복할 수 있음
for i in range(N-1, 0, -1):
    stars = '*'*i
    spaces = ' '*((N-i)*2)
    print(stars + spaces + stars)