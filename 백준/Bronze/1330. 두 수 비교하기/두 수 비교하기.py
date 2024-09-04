# 입력 받기
# input()으로 받아온 입력값은 문자열이기 때문에 int로 변환해줘야 한다.
# 문자열의 각 값을 변환해주기 위해 map을 사용한다.
a, b = map(int, input().split())

# 3개의 조건에 따라 출력해야하므로 if, elif문을 사용한다.
if a > b:
    print('>')
elif a < b:
    print('<')
else: # else로도 할 수 있겠지만 조건을 명시하기 위해 elif 사용함
    print('==')