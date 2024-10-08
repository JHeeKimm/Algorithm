# 1. 입력
#   - 첫째 줄: 전체 케이스의 개수 N
#   - 둘째 줄 ~ N개의 줄: 케이스

# 2. 출력
#   - 각 케이스마다 "Case #x: 뒤집은 단어들" 형식으로 출력

# 3. 문제 해결
#   - 각 케이스마다 단어별로 입력을 받는다.
#   - 뒤집어서 출력 -> [::-1]

n = int(input())

for i in range(n):
    words = input().split()
    # f-string 사용해 변수와 문자열 출력
    # [::-1] 슬라이싱 사용해 역순으로 출력
    print(f'Case #{i+1}:', ' '.join(words[::-1])) 