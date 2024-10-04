# 1. 입력
#   - 테스트 케이스의 개수 T
#   - 각 테스트 케이스의 첫째 줄: 지원자의 수 N
#   - 각 테스트 케이스의 둘째 줄 ~ : 각 지원자의 서류심사 성적 순위, 면접 성적 순위

# 2. 출력
#   - 각 테스트 케이스에 대해 선발 가능한 신입사원의 최대 수

# 3. 문제 해결
#   - A 지원자의 성적이 B 지원자 성적보다 서류, 면접 순위가 모두 떨어지면 A 탈락
#   - 서류 1등이 면접 1등이 아닐 수 있다.
#   - 서류 1등을 기준으로 서류 1등의 면접 순위보다 더 높은 지원자 뽑기

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    rank = sorted([list(map(int, input().split())) for _ in range(n)]) # 각 테스트 케이스의 서류,면접 순위 담기

    count = 1 # 가장 순위 높은 사람은 뽑힐거니까 1로 시작
    max_first = rank[0][1] # 정렬했을 때 가장 순위 높은 사람
    for i in range(1, n): # 두 번째 사람부터 면접 순위 비교
        if max_first > rank[i][1]:
            count += 1
            max_first = rank[i][1]

    print(count)