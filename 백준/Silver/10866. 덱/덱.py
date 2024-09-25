# 1. 입력
# - 첫째 줄: 명령의 수 N (1<=N<=10,000)
# - 둘째 줄 ~ N개의 줄: 8가지의 명령 중 1개와 정수 또는 명령만

# 2. 출력: 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# 3. 문제 해결
#   - 둘째 줄부터 N번 동안, 한 줄씩 읽으며 명령 처리
#       - push_front X: 정수 X를 덱의 앞에 추가 -> appendleft()
#       - push_back X: 정수 X를 덱의 뒤에 추가 -> append()

#       - pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력 -> 출력하고 popleft()
#       - pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력 -> 출력하고 pop()
#       - front: 덱의 가장 앞에 있는 정수를 출력
#       - back: 덱의 가장 뒤에 있는 정수를 출력
#        --> 만약 덱에 들어있는 정수가 없는 경우에는 -1 출력

#       - size: 덱에 들어있는 정수의 개수를 출력
#       - empty: 덱이 비어있으면 1을, 아니면 0을 출력
#   => 출력 명령에만 출력할 것!

import sys
from collections import deque

n = int(input())
dq = deque()

for _ in range(n):
    c = sys.stdin.readline().split()

    if c[0] == 'push_front':
        dq.appendleft(c[1])
    elif c[0] == 'push_back':
        dq.append(c[1])
    elif c[0] == 'pop_front':
        if not dq:
            print(-1)
        else: 
            print(dq[0])
            dq.popleft()
    elif c[0] == 'pop_back':
        if not dq:
            print(-1)
        else: 
            print(dq[-1])
            dq.pop()
    elif c[0] == 'front':
        if not dq:
            print(-1)
        else: 
            print(dq[0])
    elif c[0] == 'back':
        if not dq:
            print(-1)
        else: 
            print(dq[-1])
    elif c[0] == 'size':
        print(len(dq))
    elif c[0] == 'empty':
        if not dq:
            print(1)
        else: 
            print(0)