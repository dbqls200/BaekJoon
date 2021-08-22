# 1110번 - 더하기 사이클

n = int(input())
result = n
cnt = 0

while True:
    res = result % 10
    res1 = result // 10
    result = (res * 10) + ((res1 + res) % 10)
    cnt += 1

    if n == result:
        break

print(cnt)
