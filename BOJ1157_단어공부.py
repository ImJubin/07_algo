'''
1. 단어 모두 하나로 통일(upper)
2. set 중복문자 제거. 무슨 문자 있는지 i가 돌면서 집어넣기
3. 빈리스트 마련 > i가 돌면서 카운트 > 빈 리스트에 수를 넣음
4. 최댓값 두개 이상이면 "?", 아니면 최댓값
'''

word  = input().upper()
word_list = list(set(word))
cnt_list = []

for i in word_list:
    cnt = word.count(i)
    cnt_list.append(cnt)
    
if cnt_list.count(max(cnt_list)) >=2:
    ans = '?'
    
else:
    ans = word_list[cnt_list.index(max(cnt_list))]


print(ans)
