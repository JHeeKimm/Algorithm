import sys
input = sys.stdin.readline # 수정1

n, m = map(int, input().split())
song = {} # 아는 노래 담을 딕셔너리

for _ in range(n):
    song_info = input().split()
    title = song_info[1]
    notes = ''.join(song_info[2:5])
    song[notes] = '?' if notes in song else title

for _ in range(m):
    try_song = ''.join(input().split()) # 시도할 노래 입력 받기
    print(song.get(try_song, '!'))