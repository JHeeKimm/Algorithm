# 1. 입력
#   - 테스트 케이스의 개수 N
#   - 공백 한 칸으로 구분된 X1, X2, ..., XN

# 2. 출력
#   -  X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력

# 3. 문제 해결
#   - Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
#   - 좌표 압축이란? 좌표를 정렬하고 이를 순서로 표현한 것
#   - 각 값을 정렬해서 인덱스를 매기고 값의 원래 나열 순서에 맞게 그 인덱스를 출력해주자
#   - 같은 값에 대해 동일한 순서를 매겨야하니 중복을 없애고 매겨야겠다

import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
x_sort = sorted(set(x))

x_dict = dict() # key: x값, value: 정렬된 인덱스값
for i in range(len(x_sort)): # 중복 없앤 길이만큼 반복
    x_dict[x_sort[i]] = i # 정렬된 값에 인덱스 매기기

for i in x:
    print(x_dict[i], end=' ') # 원래 순서에 공백 두고 인덱스 출력
