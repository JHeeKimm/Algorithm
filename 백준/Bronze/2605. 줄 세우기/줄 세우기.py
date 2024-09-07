# 1. 입력
# 첫째 줄: 학생의 수(100 이하)
# 둘째 줄: 학생들이 뽑은 번호(0 또는 자연수)

# 2. 로직
# 각 학생이 뽑은 번호만큼 이동해서 줄 서는 순서를 정한다.

# 3. 출력: 학생들이 최종적으로 줄을 선 순서를 공백을 두고 출력한다.

n = int(input())
numbers = list(map(int, input().split()))

# 최종적으로 줄을 선 순서를 저장할 리스트 초기화
line = []

for student in range(1, n + 1):  # 학생 번호는 1부터 n까지 진행
    move_index = numbers[student - 1]  # 현재 학생이 뽑은 번호
    line.insert(len(line) - move_index, student)  # 이동할 곳으로 삽입

print(' '.join(map(str, line)))
