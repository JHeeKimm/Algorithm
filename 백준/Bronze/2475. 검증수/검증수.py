# 1. 입력 : 5자리의 숫자
# 2. 로직 : 각 숫자를 제곱한 수들을 합하고 10으로 나눈 나머지가 검증수다.
# 3. 출력 : 검증수

numbers = list(map(int, input().split()))
result = 0
for n in numbers:
    result += n**2
print(result % 10)