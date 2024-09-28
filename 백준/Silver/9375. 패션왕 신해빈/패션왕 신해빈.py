# 1. 입력
#   - 첫째 줄: 테스트 케이스
#   - 둘째 줄: 해빈이가 가진 의상의 수 N
#   - ~ N개의 줄: 그 의상의 이름, 종류 (알파벳 소문자)

# 2. 출력
#   - 각 테스트 케이스에 대해 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우

# 3. 문제 해결
#   - 로직 접근이 어려워서 구글링 했다..
#   -> 상의 a개, 하의 b개 -> (a+1(상의 안입는 경우)) * (b+1(하의 안입는 경우)) - 1(모두 안입는 경우)

import sys

input = sys.stdin.readline
t = int(input()) # 테스트 케이스 수

for _ in range(t):
    n = int(input()) # 각 테스트 케이스의 의상 수
    clothes = dict() # key 의상 종류, value 의상 개수 저장할 딕셔너리 초기화

    for _ in range(n):
        name, type = input().rstrip().split() # 의상 이름과 종류 입력 받기

        if type not in clothes.keys():
            clothes[type] = 1
        else:
            clothes[type] += 1

    result = 1
    for i in clothes.values():
        result *= (i+1)

    print(result-1)

