# 1. 입력
# 첫째 줄: 펼쳐진 카드의 개수 `N`(1 ≤ N ≤ 100,000)
# 둘째 줄부터 `N`개의 줄에 걸쳐: 카드의 정보
# -> 문자열 `S`(STRAWBERRY, BANANA, LIME, PLUM 중 하나)와 과일의 개수 `X`(1 ≤ X ≤ 5)가 공백으로 구분되어 주어짐

# 2. 로직
# 한 종류 이상의 과일이 정확히 5개 있는 경우 종을 쳐야 한다.
# -> 같은 종류의 과일 카드 개수가 총 5개인지 확인

# 3. 출력
# 같은 종류의 과일 개수가 총 5개면 "YES", 아니면 "NO"

n = int(input())

STRAWBERRY = BANANA = LIME = PLUM = 0

for _ in range(n):
    fruit, cnt = input().split()
    
    if fruit == 'STRAWBERRY':
        STRAWBERRY += int(cnt)
    elif fruit == 'BANANA':
        BANANA += int(cnt)
    elif fruit == 'LIME':
        LIME += int(cnt)
    elif fruit == 'PLUM':
        PLUM += int(cnt)

if STRAWBERRY==5 or BANANA ==5 or LIME==5 or PLUM==5:
    print('YES')
else:
    print('NO')