# 1. 입력
#   - 첫째 줄: 정환이 음을 아는 노래의 개수 N, 
#             정환이 맞히기를 시도할 노래의 개수 M이 공백으로 구분되어 주어짐
#   - 둘째 줄 ~ N개의 줄: 
#       아는 노래 제목의 길이 T, 제목 S, 음이름이 공백으로 구분되어 주어짐
#   - N+2 줄 ~ M개의 줄: 맞히길 시도할 노래의 첫 세 음
# 2. 출력
#   - 동일한 노래가 1개면 해당 '노래 제목'을 출력
#   - 노래 제목이 2개 이상이면 '?', 없다면 '!'

# 3. 문제 해결
#   - 아는 노래와 맞히기 시도할 노래의 첫 세 음이 동일한지 확인
#   -> 노래 제목과 첫 세 음을 딕셔너리에 담고 
#   -> 맞히기 시도 시 해당 음과 비교

n, m = map(int, input().split())
song = {}

for _ in range(n):
    # 아는 노래 길이, 제목, 음이름 입력 받기
    t, s, a1, a2, a3, a4, a5, a6, a7 = input().split()
    notes = [a1, a2, a3] # 첫 세 음만 리스트로 저장
    song[s] = notes # key가 노래 제목, value가 첫 세 음

for _ in range(m):
    try_song = input().split()
    count = 0
    title =''

    for i in song:
        if song[i] == try_song:
            count += 1
            title = i

    if count == 1:
        print(title)
    elif count >= 2:
        print('?')
    else:
        print('!')