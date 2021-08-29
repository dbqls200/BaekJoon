# 10250번 - ACM 호텔

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    ch = n % h
    cw = n // h + 1

    if ch == 0:
        ch = h
        cw -= 1
        
    print(ch * 100 + cw)
