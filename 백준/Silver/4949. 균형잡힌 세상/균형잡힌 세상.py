# 1. 입력
# - 각 문자열: 영문 알파벳, 공백, '()', '[]'로 이루어짐. '.'으로 끝남.(len<=100)

# 2. 출력: 'yes' or 'no'

# 3. 문제 해결
#   - 각 줄마다 해당 문자열이 균형을 이루고 있는지 판별해야 함.
#   - '()', '[]' 균형 확인
#   - '.'은 종료 지점
#   -> 괄호 속 괄호의 균형도 맞아야하기 때문에 stack에 추가하고 제거하는 방법 사용

while True:
    s = input()
    stack = []

    if s == '.':
        break
        
    for i in s:
        if i == '(' or i == '[': # 여는 괄호면 stack에 추가
            stack.append(i)
        elif i == ')': # 닫는 괄호면 확인 필요
            if stack and stack[-1] == '(': # stack이 있고, 마지막 요소가 '('이면 제거 
                stack.pop()
            else: # stack 비어있거나, 여는 괄호 짝이 없으면 stack에 추가
                stack.append(i)
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break

    if not stack: print('yes')
    else: print('no')