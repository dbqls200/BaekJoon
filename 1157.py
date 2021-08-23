# 1157번 - 단어 공부
import sys

s = sys.stdin.readline().rstrip().upper()
s_cnt = list(set(s))
cnt_list = []

for i in s_cnt:
    cnt = s.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    index = cnt_list.index(max(cnt_list))
    print(s[index])
