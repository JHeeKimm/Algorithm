# 1. 입력
#   - 첫째 줄: 명령 수 N (1<=N<=10,000)
#   - 둘째 줄 ~ N개의 줄: 각 명령

# 2. 출력
#   - 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력 

# 3. 문제 해결
#   - 명령에 따라 처리
#       - push X: 정수 X 추가
#       - size: 큐에 들어있는 정수의 개수를 출력
#       - empty: 큐가 비어있으면 1, 아니면 0을 출력

#       - pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력
#       - front: 큐의 가장 앞에 있는 정수를 출력
#       - back: 큐의 가장 뒤에 있는 정수를 출력
#       --> 만약 큐에 들어있는 정수가 없는 경우에는 -1 출력

import sys
from collections import deque

n = int(input())
q = deque()

for _ in range(n):
    c = sys.stdin.readline().split()

    if c[0] == 'push':
        q.append(c[1])
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        if len(q) == 0: print(1)
        else: print(0)
    elif c[0] == 'pop':
        if len(q) == 0: print(-1)
        else: 
            print(q.popleft())
    elif c[0] == 'front':
        if len(q) == 0: print(-1)
        else: print(q[0])
    elif c[0] == 'back':
        if len(q) == 0: print(-1)
        else: print(q[-1])
