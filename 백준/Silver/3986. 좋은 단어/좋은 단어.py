# 1. 입력
# - 첫째 줄: 명령의 수 N (1<=N<=100)
# - 둘째 줄 ~ N개의 줄: A와 B로만 이루어진 단어가 한 줄에 하나씩 주어짐

# 2. 출력: 좋은 단어의 수

# 3. 문제 해결
#   - 단어 위로 아치형 곡선을 그어 같은 글자끼리 (A는 A끼리, B는 B끼리) 쌍을 짓는다고 한다.
#   - 좋은 단어인지 확인하고 카운트한다. 
#       - 만약 선끼리 교차하지 않으면서 
#       - 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝을 지을 수 있는 경우
#   -> A와 B의 개수가 각각 짝수여야 함
#   -> 하나씩 짝을 짓고 제거해나가기

n = int(input())
count = 0

for _ in range(n):
    s = input().strip()
    stack = []

    a = s.count('A')
    b = s.count('B')
    # A와 B의 개수가 짝수인 경우만 처리 
    if a%2 == 0 and b%2 == 0:
        for c in s:
            if stack and stack[-1] == c:
                stack.pop() # 짝을 이루면 stack에서 제거
            else:
                stack.append(c) # 짝을 이루지 못하면 stack에 추가

        if not stack: # stack에 남아있지 않으면 카운트 증가
            count += 1

print(count)