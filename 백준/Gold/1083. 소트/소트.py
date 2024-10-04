# 1. 입력
#   - 첫째 줄: 배열 크기 N
#   - 둘째 줄: 배열의 원소들(모두 다른 정수)
#   - 셋째 줄: 교환 가능 횟수 S

# 2. 출력
#   - 소트한 결과가 사전순으로 가장 뒷서는 것을 출력

# 3. 문제 해결
#   - s만큼 교환이 가능한데, arr[0]과 arr[1] 교환 -> arr[2]와 arr[3] 교환 하는 식
#   -> 사전순으로 가장 뒤에 오게 하는 것이.. 최대한 큰 수가 앞에 오도록 하는 것이라고요?!

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n):
    max_val = max(arr[i:min(n, i+s+1)])
    max_idx = arr.index(max_val)
    for j in range(max_idx, i, -1):
        arr[j], arr[j-1] = arr[j-1], arr[j] # 스와프
    s -= (max_idx-i)
    if s <= 0: break

print(*arr)