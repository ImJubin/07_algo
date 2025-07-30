'''
w 너비
h 높이
si start i
sj start j

1)

'''
N = int(input())
arr = [[0]*1001 for _ in range(1001)]

for n in range(1, N+1):
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        for j in range(sj, sj+w): #색종이 면적구하기
            arr[i][j] = n


for n in range(1, N+1):
    cnt = 0
    for i in arr:
        cnt += i.count(n)
    print(cnt)