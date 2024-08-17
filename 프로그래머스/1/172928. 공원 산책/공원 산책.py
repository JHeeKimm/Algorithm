def solution(park, routes):
    w = len(park[0])
    h = len(park)
    
    x, y = 0, 0
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j
                
    direction_map = {'N':(-1, 0), 'S':(1, 0), 'W':(0, -1), 'E':(0, 1)}
    
    for r in routes:
        d, s = r.split(' ') # 방향, 스텝
        xx, xy = x, y # 이동 전의 현재 위치 저장
        
        for i in range(int(s)): # 스텝만큼 이동
            nx = x + direction_map[d][0]
            ny = y + direction_map[d][1]
            
            # 경계 내에 있고 장애물이 없다면 새 값으로 업데이트
            if 0<=nx<=h-1 and 0<=ny<=w-1 and park[nx][ny] != 'X':
                x, y = nx, ny
            else:
                x, y = xx, xy # 이동이 어렵다면 이동 전의 위치로 돌아가고
                break # 즉시 반복문 종료
            
    return [x, y]