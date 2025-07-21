'''

5
20 10 35 30 7

'''

N = int(input())
num  = list(map(int,input().split()))
maxval = float('-inf')
minval = float('inf')

for i in range(N):
    if maxval < num[i]:
        maxval = num[i]

    if minval > num[i]:
        minval = num[i]

print(minval, maxval)