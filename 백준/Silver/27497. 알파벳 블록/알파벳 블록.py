# 1. 입력
# - 첫째 줄: 버튼을 누른 횟수 N (1<=N<=1,000,000)
# - 둘째 줄 ~ N개의 줄: 누른 버튼에 대한 정보(1|2|3 문자)
#   - 1 c(문자): 문자열 맨 뒤에 c(문자) 블록 추가
#   - 2 c(문자): 문자열 맨 앞에 c(문자) 블록 추가
#   - 3: 가장 나중에 추가된 블록 제거

# 2. 출력: 완성된 문자열 출력 (빈 문자열인 경우 0 출력)

# 3. 문제 해결
#   - 둘째 줄부터 N번 동안, 한 줄씩 읽으며 입력 값을 확인하고 문자열 완성 -> 앞뒤 양방향 처리해야하므로 deque 사용
#       - 1이면 맨 뒤 추가 -> append()
#       - 2면 맨 앞 추가 -> appendleft()
#       - 3이면 가장 나중에 추가된 문자 삭제 
#           -> 앞에 추가했는지, 뒤에 추가했는지에 따라 pop() 또는 popleft()
#           -> 앞에 추가했는지, 뒤에 추가했는지에 따라 pop() 또는 popleft()
#           -> 문자가 앞에서 추가됐는지, 뒤에서 추가됐는지의 정보를 담아주는 리스트 필요
#   - 빈 문자열이라면 0 출력

from collections import deque

n = int(input())
dq = deque()
stack = []

for _ in range(n):
    btn = input().split() # 버튼 정보 받기(앞추가/뒤추가, 문자 | 제거)

    if btn[0] == '1': 
        dq.append(btn[1])
        stack.append([btn[1], 1]) # 앞 뒤 구분하기 위해 리스트로 묶어서 stack에 추가
    elif btn[0] == '2': 
        dq.appendleft(btn[1])
        stack.append([btn[1], 2])
    elif btn[0] == '3' and dq: 
        if stack[-1][1] == 1: # stack의 마지막 요소의 앞/뒤 구분 숫자 판별
            dq.pop()
            stack.pop()
        elif stack[-1][1] == 2:
            dq.popleft()
            stack.pop()
        
    
if not dq: print('0')
else: print(''.join(dq))
