from collections import deque

N, M, V = map(int, input().split())
adj = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)

def dfs(v):
    visited[v] = 1
    print(v, end=" ")

    for i in range(1, N+1):
    # ㄱ. i 지점을 방문하지 않았고
        # ㄴ. v 현 지점과 i 다음 지점이 연결 상태인 경우
        if not visited[i] and adj[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque()
    
    print(v, end=" ")
    visited[v] = 2
    q.append(v)
    while q:
        # q에서 뺄 때 방문처리 하면 중복 발생 가능성 존재
        cur_pos = q.popleft()
        for i in range(1, N+1):
            if visited[i] == 1 and adj[cur_pos][i] == 1:
                print(i, end=" ")
                visited[i] += 1
                q.append(i)


# 인접 행렬 입력 받기
for i in range(M):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

dfs(V)
print()
bfs(V)