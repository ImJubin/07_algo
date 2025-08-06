dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N = int(input())
graph = [input() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
cnt = 0
cnts = []

def dfs(r, c):
    global cnt 

    cnt += 1
    visited[r][c] = 1

    for dir in range(4):
        nr = r+dr[dir]
        nc = c+dc[dir]
        # 아래 조건 중 하나라도 걸리면, 의미 없음
        # ㄱ. 범위 초과 or
        # ㄴ. 연결되어 있지 않음 or
        # ㄷ. 이미 방문했음
        if 0 > nr or nr >= N or 0 > nc or nc >= N or graph[nr][nc] == "0" or visited[nr][nc] == 1:
            continue
        dfs(nr, nc)

for i in range(N):
    for j in range(N):

        if graph[i][j] != "1" or visited[i][j] == 1:
            continue

        cnt = 0
        dfs(i, j)
        cnts.append(cnt)

print(len(cnts))
cnts.sort() #오름차순
for i in range(len(cnts)):
    print(cnts[i]) #한 줄씩 출력