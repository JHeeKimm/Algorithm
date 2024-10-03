# 1. 입력
#   - 3명의 팀원들의 3개의 정보가 한 줄씩 주어짐
#   - 해결한 문제 개수 P, 입학 연도 Y, 성씨 S가 공백으로 주어짐

# 2. 출력
#   - 입학 연도를 100으로 나눈 나머지를 오름차순으로 정렬해서 이어 붙인 문자열 출력
#   - 성씨 첫글자를 해결한 문제가 많은 사람 순으로 나열한 문자열 출력

# 3. 문제 해결
#   - 각 입학 연도를 계산하고 배열에 담고 오름차순 정렬해서 붙인다
#   - 해결한 문제 수와 성씨 첫글자를 같이 담고, 문제 수 기준으로 정렬하고 순서대로 각 성씨 첫글자를 가져온다

t = [input().split() for _ in range(3)]

year = []
solved = []
for i in range(3):
    year.append(int(t[i][1]) % 100)
    solved.append([int(t[i][0]), t[i][2][0]])

year.sort() # 오름차순 정렬
solved.sort(key=lambda x:-x[0]) # 문제 수 기준으로 내림차순 정렬

name = []
for i in range(3):
    name += solved[i][1] # 첫글자만 가지고 와서 따로 담아줌

print(''.join(list(map(str, year))))
print(''.join(name))