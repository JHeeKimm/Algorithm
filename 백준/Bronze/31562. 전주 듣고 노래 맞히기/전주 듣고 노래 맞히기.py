from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
song = {} # 아는 노래 담을 딕셔너리

for _ in range(n):
    # 아는 노래의 제목 길이, 제목, 음이름 입력 받기
    t, s, a1, a2, a3, a4, a5, a6, a7 = input().split()
    # 아는 노래 담기
    song[s] = [a1, a2, a3] # key가 노래 제목, value가 첫 세 음

for _ in range(m):
    try_song = input().split() # 시도할 노래 입력 받기
    count = 0
    title = ''

    # 아는 노래 딕셔너리에서 일치하는 것이 있다면 카운트 증가, 해당 제목으로 재할당
    for i in song:
        if song[i] == try_song:
            count += 1
            title = i

    if count == 1: # 일치하는 노래가 1개면 제목 출력
        print(title)
    elif count >= 2: # 일치하는 노래가 2개 이상이면 ? 출력
        print('?')
    else:
        print('!')  # 일치하는 노래가 없으면 ! 출력