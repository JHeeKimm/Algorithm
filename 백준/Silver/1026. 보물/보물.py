# 1. 입력
#   - 첫째 줄: N
#   - 둘째 줄: A에 있는 N개의 수 (0~100)
#   - 셋째 줄: B에 있는 N개의 수

# 2. 출력
#   - S의 최솟값 (S = A[0] × B[0] + ... + A[N-1] × B[N-1])

# 3. 문제 해결
#   - A의 수를 재배열해서 S의 최솟값 만들기. B는 재배열하면 안 된다.
#   - 가장 작은 수와 가장 큰 수를 곱해서 더하면 최솟값이 나오겠다.
#   - A는 오름차순 정렬하고, B는 max()로 계산 해주고 제거하는 식으로 하면 되겠다.

n = int(input())
a = sorted(list(map(int, input().split()))) # a 정렬해서 리스트로 받기
b = list(map(int, input().split()))

s = 0
for i in range(n):
    max_b = max(b)
    s += a[i]*max_b
    b.remove(max_b)

print(s)