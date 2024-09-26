# 1. 입력
#   - 첫째 줄: 명령 수  (1<=N<=10,000)
#   - 둘째 줄 ~ N개의 줄: 각 명령

# 2. 출력
#   - 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력 

# 3. 문제 해결
#   - 명령에 따라 처리
#       - push X: 정수 X 추가
#       - size: 스택에 들어있는 정수의 개수를 출력
#       - empty: 스택이 비어있으면 1, 아니면 0을 출력

#       - pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력
#       - top: 스택의 가장 위에 있는 정수 출력
#       --> 만약 스택에 들어있는 정수가 없는 경우에는 -1 출력

import sys
from collections import deque

n = int(input())
stack = deque()

for _ in range(n):
    c = sys.stdin.readline().split()

    if c[0] == 'push':
        stack.append(c[1])
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
    elif c[0] == 'pop':
        if len(stack) == 0: print(-1)
        else: 
            print(stack.pop())
    elif c[0] == 'top':
        if len(stack) == 0: print(-1)
        else: print(stack[-1])