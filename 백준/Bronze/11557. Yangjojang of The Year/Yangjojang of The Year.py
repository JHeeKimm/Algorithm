# 1. 입력
#   - 첫 줄: 테스트 케이스 개수 T
#   - 각 테스트 케이스 첫 줄: 학교 수 N
#   - 각 테스트 케이스 N개의 줄: 학교 이름, 한 해 소비한 술의 양 

# 2. 출력
#   - 각 테스트 케이스마다 한 줄에 걸쳐 술 소비가 가장 많은 학교 이름 출력

# 3. 문제 해결
#   - 학교 이름을 key, 술의 양을 value로 담는다
#   - value끼리 비교해서 가장 큰 value의 key를 반환해보자

from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dict = defaultdict(int)

    for _ in range(n):
        university, soju = input().rstrip().split()
        dict[university] = int(soju) # 학교 이름을 key, 술의 양을 value로 담기

    print(max(dict, key=dict.__getitem__))