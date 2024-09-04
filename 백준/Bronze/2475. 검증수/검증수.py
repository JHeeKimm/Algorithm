# 1. 입력 : 5개의 숫자 (각각 공백으로 구분됨)
# 2. 로직 : 각 숫자를 제곱한 후, 그 값들을 합하고 10으로 나눈 나머지를 구한다.
# 3. 출력 : 계산된 나머지 값 (검증수)
numbers = map(int, input().split())
result = 0
for n in numbers:
    result += n**2
print(result % 10)
