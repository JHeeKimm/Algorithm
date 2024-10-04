# 1. 입력
#   - 단어 개수 N
#   - 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어짐

# 2. 출력
#   - 조건에 따라 정렬하여 단어들 출력

# 3. 문제 해결
#   - 길이가 짧은 것부터, 길이가 같으면 사전 순으로, 중복없이..
#   - 람다를 사용하면 길이 기준과 사전 순으로 같이 정렬할 수 있다


import sys
input = sys.stdin.readline

n = int(input())
words = set()

for _ in range(n):
    word = input().strip()
    words.add((word, len(word))) # set 함수에 단어와 길이 같이 담기

sorted_words = sorted(words, key=lambda x:(x[1], x[0])) # 길이 기준, 사전 순으로 정렬

for word in sorted_words:
    print(word[0])