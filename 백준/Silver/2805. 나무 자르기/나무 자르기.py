# 1. 입력
#   - 첫째 줄: 나무의 수 N, 상근이가 원하는 나무의 길이 M, 
#   - 둘째 줄: 나무의 높이

# 2. 출력
#   - 적어도 M미터의 나무를 위해 절단기에 설정할 수 있는 최대 높이

# 3. 문제 해결
#   - 절단기에 높이 H를 지정하면 톱날이 땅으로부터 H미터 올라간다
#   - 그 다음, 한 줄에 연속해있는 나무를 모두 절단한다
#   -> 절단한 길이들이 M이 되게 하는 절단기 설정 높이 최댓값 구하기 
#   -> 분류에서 이분 탐색이라길래 이분 탐색이 뭔지 검색해봄
#   -> 오름차순으로 정렬한 리스트의 가운데 값을 기준으로 왼쪽, 오른쪽 탐색하기인거 같은데..
#   -> 여기선 최소 나무길이와 최대 나무길이의 가운데 값

import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
tree_h = list(map(int, input().split()))

start = 1
end = max(tree_h) # 나무 최대 높이가 절단기 최대 높이
while start <= end: 
    mid = (start+end)//2 # 가운데 값을 자르는 설정 높이로 둔다
    total = 0 # 가져갈 나무 길이

    for h in tree_h:
        if h > mid: # 나무 높이가 가운데 값보다 크면
            total += (h-mid) # 잘린 부분 total에 넣기
    if total < m: # 가져갈 나무 길이가 안 채워졌으면
        end = mid-1 # 더 자르기 위해 설정 높이 낮춰주기
    else:
        start = mid+1 # 가져갈 나무 길이가 같거나 넘으면 설정 높이 올려주기

print(end) # end가 절단기 설정 최대 높이