# 2675번 - 문자열 반복

t = int(input())

for i in range(t):
    result = ''
    r, s = map(str, input().split())
    r = int(r)
    
    for j in s:
        result += j * r
        
    print(result)
