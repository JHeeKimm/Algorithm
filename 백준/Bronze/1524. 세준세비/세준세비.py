# 1. 입력
#   - 첫째 줄: 테스트 케이스 개수 T
#   - 각 테스트 케이스 첫째 줄: 세준이 병사 수 N, 세비 병사 수 M
#   - 각 테스트 케이스 둘째 줄: 세준이의 병사들의 힘
#   - 각 테스트 케이스 셋째 줄: 세비의 병사들의 힘

# 2. 출력
#   - 각 테스트 케이스에 대한 승자 출력
#   - 세준이가 이기면 'S', 세비가 이기면 'B', 둘다 아니면 'C'

# 3. 문제 해결
#   - 각 전투 중 제일 약한 병사가 죽는다.
#   - 제일 약한 병사가 여러 명이고, 제일 약한 병사들이 모두 같은 편이면 그 중 한 명이 죽는다.
#   - 제일 약한 병사가 여러 명이고, 양 편에 모두 있다면, 세비의 제일 약한 병사 중 한 명이 죽는다.
#   - 전쟁은 한 명의 병사를 제외하고 모두 죽었을 때 끝난다.

#   -> 세진과 세비 병사의 힘을 비교해서 죽는 병사 빼기.
#   -> 세진이 남아있는지 세비가 남아있는지 둘 다 안 남아있는지 확인하고 출력하면 되겠다.
#   -> 줄바꿈으로 구분해 입력을 받아와야 하는데.. input()을 한 번 더 넣어주면 되려나
#   -> 수가 작을 수록 약하고 클 수록 강하니 정렬 필요하겠다

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    input()
    n, m = map(int, input().split())
    sejun = sorted(list(map(int, input().split())))
    sebi = sorted(list(map(int, input().split())))

    while len(sejun) != 0 and len(sebi) != 0: 
        if sejun[0] >= sebi[0]:
            sebi.pop(0)
        else:
            sejun.pop(0)

    if len(sebi) == 0:
        print('S')
    elif len(sejun) == 0:
        print('B')
    else: 
        print('C')