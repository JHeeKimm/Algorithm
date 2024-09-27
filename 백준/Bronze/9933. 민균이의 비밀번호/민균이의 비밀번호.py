# 1. 입력
#   - 첫째 줄: 단어의 수 N (2<=N<=100)
#   - 둘째 줄 ~ N개의 줄: 파일에 적힌 단어 (2<길이<14, 알파벳 소문자, 홀수)

# 2. 출력
#   - 비밀번호의 길이와 가운데 글자를 공백을 두고 출력

# 3. 문제 해결
#   - 주어진 단어 중 하나는 민균이의 비밀번호이다.
#   - 올바른 비밀번호와, 뒤집어져있는 비밀번호가 있다.
#   -> 회문인 경우
#   -> 한 단어가 다른 단어의 뒤집은 문자열과 같은 경우

n = int(input())
file = []

for _ in range(n):
    word = input().rstrip()
    
    if word == word[::-1]:  # 단어가 회문인 경우
        print(len(word), word[len(word)//2])
    elif word[::-1] in file:  # 뒤집은 문자열이 이미 존재하는 경우
        print(len(word), word[len(word)//2])
    else:
        file.append(word)  # 뒤집은 문자열이 존재하지 않으면 파일에 추가
        