# 1번 퀘스트 수행하면 1개 스톤 활성화 되고, 기존에 활성화된 스톤이 없기 때문에 경험치 0
# 2번 퀘스트 수행하면 1개 더 스톤 활성화 되고, 기존에 활성화된 스톤 1개 있기 때문에 200 추가
# 3번 퀘스트 수행하면 스톤이 총 2개까지 활성화 가능하니까, 활성화된 스톤 2개에 300씩 추가
# -> 정렬해서 작은 경험치의 퀘스트부터 수행
# -> k만큼 활성화 추가 가능
# -> 현재 수행하는 퀘스트의 스톤은 활성화되면서 경험치가 0이 되니 이만큼은 빼주고, 
#    활성 스톤 수에 경험치를 곱해준 값을 더한다

n, k = map(int, input().split())
exp = sorted(list(map(int, input().split())))

max_sum = 0
count = 0 # 활성 스톤 수 증가시킬 변수
for i in range(n):
    
    if k > count:
        count += 1
        max_sum -= exp[i]
    max_sum += exp[i]*count

print(max_sum)