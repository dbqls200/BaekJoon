# 1712번 - 손익분기점

a, b, c = map(int, input().split())
result = 0

if b >= c:
    print(-1)
else:
    result = a / (c - b)

    print(int(result) + 1)
