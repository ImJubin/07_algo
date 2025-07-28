'''
0. 빈자리 세팅
1. xy 자리 바꿔서 하우상좌로 (프린트할때 yx로 바꿔서)
2. 처음 좌표 찍기
3. 델타로 돌기
4. 범위 안, 방문 안했으면 > 1로 바꾸기
5. count가 k 일 때 , a.b 좌표 출력
'''

C,R = map(int,input().split())
K = int(input())

arr = [[0]*C for _ in range (R)]

    
if K <= R*C:
    dr = [-1, 0, 1, 0]  # 상, 우, 하, 좌
    dc = [0, 1, 0, -1]

    dir = 0
    x, y = 0, R-1  # 시작 좌표: 좌하단
    cnt = 1

    while True:
        # 1. 현재 지점에 count를 찍고
        arr[y][x] = cnt

        if cnt == K:
            print(x+1, R-y)
            break

        cnt += 1
        # 2. 다음 지점 좌표를 찾아 이동
        ny = y+dr[dir]
        nx = x+dc[dir]


        # 밖을 벗어나거나 이미 채워진 값은 이동하면 안 됨
        if nx < 0 or nx >= C or ny < 0 or ny >= R or arr[ny][nx] != 0:
            dir = (dir+1)%4
            ny = y + dr[dir]
            nx = x + dc[dir]

        y = ny
        x = nx 

else:
    print(0)

