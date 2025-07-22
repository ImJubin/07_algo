'''

'''

N = int(input())
Ai = list(map(int, input().split()))
B,C = map(int, input().split())

# 올림 하려면 C-1 한만큼 더해주기 (그럼 나머지 생겨서 버려지지않으니까. 몫이 +1되니까 )

ans = N
for n in Ai:
    if n-B>0: # 총감독 맡고도 부감독도 맡아야 하는 경우면
        ans += (n-B+(C-1))//C

print(ans)
