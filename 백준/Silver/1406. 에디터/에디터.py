# 1. 입력
#   - 첫째 줄: 문자열 (길이가 N, 영소문자)
#   - 둘째 줄: 명령어 개수 M (1 <= M <= 500,000) 
#   - 셋째 줄 ~ M개의 줄: 명령어

# 2. 출력
#   - 모든 명령어 수행 후 문자열 출력 

# 3. 문제 해결
#   - 명령에 따라 처리
#       - L: 커서 왼쪽으로 한 칸 이동 (커서가 문장 맨 앞이면 무시)
#       - D: 커서 오른쪽으로 한 칸 이동 (커서가 문장 맨 뒤면 무시)
#       - B: 커서 왼쪽에 있는 문자 삭제 (커서가 문장 맨 앞이면 무시)
#       - P $: $라는 문자를 커서 왼쪽에 추가
#   -> 커서의 위치를 고려하기 위해 두 개의 스택을 두고, 
#   -> 스택의 요소를 움직이며 명령 처리


import sys

s1 = list(input())
s2 = []

n = int(input())

for _ in range(n):
    c = sys.stdin.readline().strip().split()

    if c[0] == 'L' and s1:
        s2.append(s1.pop())
    elif c[0] == 'D' and s2:
        s1.append(s2.pop())
    elif c[0] == 'B' and s1:
        s1.pop()
    elif c[0] == 'P':
        s1.append(c[1])
    
print(''.join(s1+s2[::-1]))