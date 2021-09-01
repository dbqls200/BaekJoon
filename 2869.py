# 2869번 - 달팽이는 올라가고 싶다

a, b, v = map(int, input().split())
result = (v - b) / (a - b)

print(int(result) if result == int(result) else int(result) + 1)
