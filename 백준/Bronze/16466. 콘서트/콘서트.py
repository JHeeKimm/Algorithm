# 1. 입력
#   - 첫째 줄: 1차 티켓팅에서 팔린 티켓 수 N
#   - 둘째 줄: 1차 티켓팅에서 팔린 티켓 번호 A가 N개 주어짐

# 2. 출력
#   - 2차 티켓팅에서 가질 수 있는 티켓 중 가장 작은 번호 출력

# 3. 문제 해결
#   - 티켓 번호가 1부터 시작하고, 주어진 번호가 중간에 빠진 수가 있을 수 있다.
#   - 일단 정렬을 해야겠고.. 빠진 번호 중 가장 작은 값이거나
#   - 빠진 값이 없다면 주어진 수 중 가장 큰 값의 다음 값일텐데
#   - 그냥 하나씩 늘리면서 확인하는 수밖에 없나

import sys
input = sys.stdin.readline

n = int(input())
tickets = sorted(list(map(int, input().split())))

for i in range(n):
    if tickets[i] != i+1: # 중간에 빠진 번호 중 있는지 확인
        print(i+1) # 티켓 번호가 1부터 시작하므로 i+1
        exit()

print(tickets[-1]+1) # 빠진 번호가 없다면 마지막 값에 +1