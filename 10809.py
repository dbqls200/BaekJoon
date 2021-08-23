# 10809번 - 알파벳 찾기

s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    print(s.find(i), end = ' ')
