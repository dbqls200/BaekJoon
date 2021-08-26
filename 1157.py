# 1157번 - 단어 공부

s = input().upper()
cnt = []

for i in set(s):
    cnt.append(s.count(i))

idx = [i for i, x in enumerate(cnt) if x == max(cnt)]

if len(idx) > 1:
    print("?")
else:
    print(list(set(s))[cnt.index(max(cnt))])


    

