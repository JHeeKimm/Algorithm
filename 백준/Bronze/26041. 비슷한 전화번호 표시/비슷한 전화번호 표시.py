# n개의 전화번호가 공백으로 구분된 문자열 A에서
# 전화번호 B와 다르면서, B를 접두사로 갖는 전화번호의 개수 출력하기

a = list(input().split())
b = input()

count = 0
for i in range(len(a)):
    if a[i] == b:
        continue
    elif (a[i].startswith(b)): 
        count += 1

print(count)