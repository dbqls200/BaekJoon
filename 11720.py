# 11720번 - 숫자의 합

n = int(input())
arr = [0] * n
num = input()
hap = 0

for n in num:
    hap += int(n)

print(hap)
