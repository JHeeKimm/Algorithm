# 1. 입력
# 1-1. 첫째 줄: 주의 개수 `N`(1 <= N <= 50)
# 1-2. 둘째 줄부터: 근무표
# - 각 주는 4개의 줄로 표현된다
# - 첫째 줄은 각 날의 08:00~12:00(4시간)에 근무하는 사람의 이름 또는 '-', 
# - 둘째 줄은 12:00~18:00(6시간), 셋째 줄은 18:00~22:00(4시간), 넷째 줄은 22:00~08:00(10시간)을 나타낸다. 
# - '-'는 근무자가 없음을 의미한다. 
# => 4개의 시간대 x `N`주

# 2. 로직
# 2-1. 각 주차별 근무자의 근무 시간을 계산한다.
# 2-2. 각 근무자의 근무 시간을 합산해서 총 근무 시간을 구한다.
# 2-3. 최대 근무 시간과 최소 근무 시간의 차이가 12시간 이하인지 확인한다.

# 3. 출력
# 그 차이가 12시간 이하이면 “Yes”를 아니면 “No”를 출력한다. 
# 단, 아무도 근무하지 않을 경우 공평한 것으로 간주한다.

# 입력 받기
n = int(input())

shift_times = [4, 6, 4, 10] # 근무 시간대
work_times = {} # 근무자별 총 근무 시간 딕셔너리 초기화

# 각 주별 근무표 처리
for week in range(n):
    for shift in range(4):
        workers = input().strip().split()
        
        # 각 근무자의 근무 시간 합산
        for worker in workers:
            if worker != '-':
                work_times[worker] = work_times.get(worker, 0) + shift_times[shift]

hours = list(work_times.values())

# 아무도 근무하지 않은 경우
if not hours:
    print("Yes")
elif max(hours) - min(hours) <= 12: # 근무시간 최대-최소 차이가 12시간 이하인지 확인
    print("Yes")
else: 
    print("No")