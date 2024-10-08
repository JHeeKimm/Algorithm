# 1. 입력
#   - 수의 개수 N(1 ≤ N ≤ 500,000) 단, N은 홀수이다.
#   - 그 다음 N개의 줄: 정수

# 2. 출력
#   - 첫째 줄에는 산술평균(소수점 이하 첫째 자리에서 반올림한 값)
#   - 둘째 줄에는 중앙값
#   - 셋째 줄에는 최빈값(여러 개 있을 때에는 최빈값 중 두 번째로 작은 값)
#   - 넷째 줄에는 범위

# 3. 문제 해결
#   - 수들을 리스트에 담고 각 통계 처리를 하면 되겠다.
#   - 최빈값을 그냥 mode import 해서 했더니 틀렸단다
#   - 최빈값이 여러 개 있을 때 두 번째로 작은 값을 처리해줘야한다.

import sys
input = sys.stdin.readline

n = int(input())
list = [int(input()) for _ in range(n)]

# 산술평균
print(round(sum(list)/n))

# 중앙값
list.sort()
print(list[n//2])

# 최빈값
mode_dict = {}
for l in list:
    if l not in mode_dict:
        mode_dict[l] = 1
    else:
        mode_dict[l] += 1 # 각 수에 대해 카운트

max_mode = max(mode_dict.values())
max_list = []
for key, value in mode_dict.items():
    if value == max_mode: # 최빈값이면 해당 수를 리스트에 담기
        max_list.append(key)

if len(max_list) == 1:
    print(max_list[0])
else:                  # 최빈값이 여러 개 있을 경우
    print(max_list[1]) # 두 번째로 작은 값 출력

# 범위
print(max(list)-min(list))