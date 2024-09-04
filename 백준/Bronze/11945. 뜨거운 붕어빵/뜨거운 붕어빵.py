# 1. 입력
# 첫째 줄 : N과 M(0≤N,M≤10)
# 둘째 줄부터 N개의 줄 : 각 줄에 ‘0‘ 또는 ‘1’이 총 M개(‘0‘은 공백, ‘1’은 붕어빵)
# 2. 로직 : 각 줄의 문자열을 좌우로 뒤집어서 출력하는 것을 반복한다.
# 3. 출력 : 뒤집힌 문자열 출력

# 첫째 줄 입력 받기
N, M = map(int, input().split())

# 각 줄을 리스트로 저장(순회하기 위해)
bread = []
for _ in range(N):
    row = input() # 둘째 줄부터 입력 받기
    bread.append(row)
    
# 각 줄을 순회하며 역순으로 출력
for row in bread:
    print(row[::-1])