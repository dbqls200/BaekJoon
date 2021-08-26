# 1152번 - 단어의 개수

t = input()
cnt = 0

if t[0] != ' ':
    cnt += 1
    
for i in range(1, len(t)):
    if t[i] != ' ' and t[i - 1] == ' ':
        cnt += 1

print(cnt)
