# 2941번 - 크로아티아 알파벳

s = input()
cnt = 0

if s == ' ':
    cnt = 0
    
elif len(s) == 1:
    cnt = 1
    
else:
    cnt = 1
    for i in range(1, len(s)):
        if s[i].isalpha() == False:
            if s[i - 1] == 'z' and s[i - 2] == 'd':
                cnt -= 1
            continue

        
        elif s[i] == 'j':
            if s[i - 1] == 'l' or s[i - 1] == 'n':
                continue
            cnt += 1
        
        else:
            cnt += 1

print(cnt)

