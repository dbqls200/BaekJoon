# 1316번 - 그룹 단어 체커

n = int(input())
cnt = 0

for i in range(n):
    s = input()
    check = []
    a = '0'
    for j in s:
        if j != a:
            check.append(j)
        a = j
    if len(check) == len(set(check)):
        cnt += 1

print(cnt)
